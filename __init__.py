import feedparser
import xmltodict
import requests
import collections
from mycroft import MycroftSkill  #, intent_file_handler
from mycroft.skills.core import intent_handler, intent_file_handler
from mycroft.audio import wait_while_speaking
from datetime import datetime, date
from shapely.geometry import Point, Polygon
from mycroft.configuration import ConfigurationManager as config

from .swi_resources import SWI_SERVICES

class SevereWeatherInformation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.monitoring = False
        self.update_interval = 600
        self.severity = ""
        self.urgency = ""
        self.certainty = ""
        self.service_id = ""
        self.service = {}
        self.location_filter = ""
        self.location_text = ""
        self.alerts = []
        self.status = "stopped"

    def initialize(self):
        self._setup()
        self.settings.set_changed_callback(self.on_websettings_changed)
        #self.log.info("config: {}".format(ConfigurationManager.get()))

    def on_websettings_changed(self):
        self.log.debug("websettings changed")
        self._setup()

    def _setup(self):
        self.service = {}
        service_id = self.settings.get('service', '')
        language = self.settings.get('language', 'en')
        if service_id and ":" not in service_id:
            service_id = "{}:{}".format(service_id, language)
        if service_id in SWI_SERVICES.keys():
            self.service = SWI_SERVICES[service_id]
        self.log.info("service = {}".format(self.service))
        #handling of custom configuration
        if service_id == "ZZZ:zzz":
            custom_url = self.settings.get('custom_url', '')
            if custom_url:
                self.service['url'] = custom_url
                self.service['lang'] = language
            else:
                self.service = {}

        self.severity = self.settings.get('severity', 'Extreme')
        self.urgency = self.settings.get('urgency', 'Immediate')
        self.certainty = self.settings.get('certainty', 'Observed')

        self.location_filter = self.settings.get('location_filter', '')
        self.location_text = self.settings.get('location_text', '')

        self.alerts = []
        self.status = "stopped"

        self.log.info("severity {} urgency {} certainty {}".format(self.severity, self.urgency, self.certainty))
        if self.settings.get('auto_alert', False) and self.service:
            self.monitoring = True
            self.update_interval = self.settings.get("update_interval", 10) * 60
            self.schedule_repeating_event(handler=self.auto_alert_handler, when=datetime.now(), frequency=self.update_interval, name='Meteoalert')
            self.log.info("auto_alert on, update_interval {} seconds".format(self.update_interval))
        else:
            self.monitoring = False
            self.cancel_scheduled_event('SevereWeatherInformation')
            self.log.info("auto_alert off")

    def _check_for_alerts(self):
        self.alerts = {}
        self.log.info("url: {}".format(self.service['url']))
        self.log.info("header: {}".format(self.service['hdr_feed']))
        feed = feedparser.parse(self.service['url'], request_headers=self.service['hdr_feed'])
        #self.log.info(feed)
        #self.log.info("CAP v{}".format(self.get_cap_version(feed)))
        self.alerts = self.get_filtered_alerts(feed.entries, max_entries=5)

    @intent_file_handler('information.weather.severe.intent')
    def handle_information_weather_severe(self, message):
        self._check_for_alerts()
        if self.alerts:
            first_message = True
            for alert in self.alerts:
                headline = ""
                description = ""
                info = self.get_alert_info_by_lang(alert, language=self.service['lang'])
                if info:
                    if "headline" in info.keys():
                        #self.log.info(info["headline"])
                        headline = info["headline"]
                    elif "title" in info.keys():
                        #self.log.info(info["title"])
                        headline = info["title"]
                    if "summary" in info.keys():
                        #self.log.info(info["summary"])
                        description = info["summary"]
                    elif "description" in info.keys():
                        #self.log.info(info["description"])
                        description = info["description"]
                    if first_message and headline and description:
                        self.speak_dialog("alerts")
                        first_message = False
                        self.status = "speaking"
                    if headline and description:
                        wait_while_speaking()
                        if self.status == "speaking":
                            self.speak(headline)
                        if self.status == "speaking":
                            self.speak(description)
                else:
                    self.log.info("???")

        else:
            self.log.info("no alerts!")
            self.speak_dialog("noalerts")

        #self.speak_dialog('information.weather.severe')

    def auto_alert_handler(self):
        pass

    def is_cap_entry(self, entry):
        k = entry.keys()
        if ("cap_sent" in k) and ("cap_status" in k) and ("cap_msgtype" in k):
            return True
        return False

    def get_cap_alert_link(self, links):
        caplink = ""
        for li in links:
            #print(l)
            # cap+xml has priority, use alternate only if cap+xml link not found
            if "application/cap+xml" in li.type:
                caplink = li.href
            elif ("alternate" in li.rel) and (not caplink):
                caplink = li.href
        self.log.debug("caplink: {}".format(caplink))
        return caplink

    def get_cap_version(self, feed):
        cap_version = ""
        self.log.debug(feed)
        if "namespaces" in feed.keys():
            for k, v in feed.namespaces.items():
                if "urn:oasis:names:tc:emergency:cap:" in v:
                    cap_version = v[-3:]
        else:
            self.log.debug("no namespace")
        return cap_version

    def get_cap_namespace(self, feed):
        cap_ns = ""
        for k, v in feed.namespaces.items():
            if "urn:oasis:names:tc:emergency:cap:" in v:
                cap_ns = k
        return cap_ns

    def get_filtered_alerts(self, entries, status="Actual",
                            msgType="Alert,Update", scope="Public",
                            sent=date.today(), expires=date.today(),
                            max_entries=999):
        alerts = []
        debugcount = 0
        for e in entries:
            debugcount += 1
            if debugcount > 99:
                break
            # when entry contains CAP data do some quick filtering without
            # loading and parsing the actual CAP alert
            if self.is_cap_entry(e):
                self.log.info("CAP entry")
                if (e.cap_status not in status) or (e.cap_msgtype not in msgType):
                    self.log.info(e.id)
                    self.log.info("status: {} msgtype: {}".format(e.cap_status,
                                  e.cap_msgtype))
                    continue
                if not ((self._get_datetime(e.cap_sent).date() == sent) or
                        (self._get_datetime(e.cap_expires).date() >= expires)):
                    self.log.info(e.id)
                    self.log.info("sent: {} expires: {}".format(e.cap_sent,
                                                                e.cap_expires))
                    continue
                if "cap_severity" in e.keys() and e.cap_severity not in self.severity:
                    continue
                if "cap_urgency" in e.keys() and e.cap_urgency not in self.urgency:
                    continue
                if "cap_certainty" in e.keys() and e.cap_certainty not in self.certainty:
                    continue

            caplink = self.get_cap_alert_link(e.links)
            self.log.debug(caplink)
            # fix for Spain, first link is download of compressed feed
            if ".tar.gz" in caplink:
                continue

            r = requests.get(caplink, headers=self.service['hdr_atom'])
            if r.status_code != 200:
                self.log.info("request status: {}".format(r.status_code))
                continue

            a = xmltodict.parse(r.content.decode("utf-8"),
                                namespaces={'cap': None})
            if "alert" not in a.keys():
                self.log.info("no alert")
                continue
            alert = a["alert"]
            info = self.get_alert_info_by_lang(alert, language=self.service['lang'])
            if not info:
                continue

            if not self.is_cap_entry(e):
                if (alert["status"] not in status) or (alert["msgType"] not in msgType):
                    self.log.info("status: {} msgtype: {}".format(alert["status"], alert["msgType"]))
                    continue

                if "expires" in info.keys():
                    if not ((self._get_datetime(alert["sent"]).date()==sent) or
                            (self._get_datetime(info["expires"]).date()>=expires)):
                        self.log.info("sent: {} expires: {}".format(alert["sent"], info["expires"]))
                        continue
                else:
                    if not ((self._get_datetime(alert["sent"]).date()==sent)):
                        self.log.info("sent: {} ".format(alert["sent"]))
                        continue
                if "severity" in info.keys() and info["severity"] not in self.severity:
                    continue
                if "urgency" in info.keys() and info["urgency"] not in self.urgency:
                    continue
                if "certainty" in info.keys() and info["certainty"] not in self.certainty:
                    continue

            # location filtering
            if self.location_filter == "geoloc":
                lon = config.get()['location']['coordinate']['longitude']
                lat = config.get()['location']['coordinate']['latitude']
                if not self.in_geo_location(info, longitude=lon, latitude=lat):
                    self.log.info("skipping for reason: geoloc")
                    continue
            elif self.location_filter == "areadesc" and self.location_text:
                if not self.in_geo_location(info, areadesc=self.location_text):
                    self.log.info("skipping for reason: areadesc - {}".format(self.location_text))
                    continue
            elif self.location_filter == "areadesc" and self.location_text:
                if not self.in_geo_location(info, geocodevalue=self.location_text):
                    self.log.info("skipping for reason: geocode - {}".format(self.location_text))
                    continue

            # all filters criterias passed, add alert to result list
            self.log.info("add alert {}".format(alert["identifier"]))
            alerts.append(alert)
            if len(alerts) == max_entries:
                break
        return alerts

    def get_alert_info_by_lang(self, alert, language="en-GB,en-US"):
        # print(type(alert["info"]))
        if type(alert["info"]) is list:
            for i in alert["info"]:
                if i["language"] in language:
                    return i
        elif type(alert["info"]) is collections.OrderedDict:
            if "language" in alert.keys() and alert["info"]["language"] in language:
                return alert["info"]
            else:  # only one info-item found, use it regardless of language?
                return alert["info"]
        return None

    def in_geo_location(self, info, longitude=None, latitude=None, areadesc="",
                        geocodename="", geocodevalue=""):
        infoareas = self._get_iterable(info["area"])
        for area in infoareas:
            # print("{} {}".format(type(area),area))
            if longitude and latitude and "polygon" in area.keys():
                points = []
                for lola in area["polygon"].split(" "):
                    lonlat = lola.split(",")
                    lon = lonlat[0]
                    lat = lonlat[1]
                    points.append((float(lon),float(lat)))
                polygon = Polygon(points)
                point = Point(longitude, latitude)
                within = point.within(polygon)
                # TODO consider EXCLUDE_POLYGON
                # print("within = {}".format(within))
                return within
            if areadesc and "areaDesc" in area.keys():
                if areadesc.lower() in area["areaDesc"].lower():
                    # TODO: fuzzy matching?
                    return True
            if geocodename and geocodevalue and "geocode" in area.keys():
                geocodes = self._get_iterable(area["geocode"])
                for gc in geocodes:
                    if "valueName" in gc and "value" in gc \
                        and geocodename.lower() in gc["valueName"].lower() \
                        and geocodevalue.lower() in gc["value"].lower():
                        return True
            if geocodevalue and "geocode" in area.keys():
                geocodes = self._get_iterable(area["geocode"])
                for gc in geocodes:
                    if "value" in gc and geocodevalue.lower() in gc["value"].lower():
                        return True
        return False

    def stop(self):
        self.status = "stopped"
        self.log.info("Meteoalert stop")

    def _get_iterable(self, object):
        iterable = []
        if type(object) is list:
            iterable = object
        elif type(object) is collections.OrderedDict:
            iterable.append(object)
        # print("iterable {}".format(iterable))
        return iterable

    def _get_datetime(self, dt_string):
        # "YYYY-MM-DDThh:mm:ssXzh:zm" -> "YYYY-MM-DDThhmmssXzhzm" for easier pattern matching
        dt_object = datetime.strptime(dt_string.replace(':', ''), "%Y-%m-%dT%H%M%S%z")
        return dt_object

def create_skill():
    return SevereWeatherInformation()
