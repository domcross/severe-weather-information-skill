from mycroft import MycroftSkill, intent_file_handler


class SevereWeatherInformation(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('information.weather.severe.intent')
    def handle_information_weather_severe(self, message):
        self.speak_dialog('information.weather.severe')


def create_skill():
    return SevereWeatherInformation()

