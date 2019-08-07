#!/bin/bash

sudo apt-get update

#libgeos-dev is required for Shapely
sudo apt-get install -yq libgeos-dev
exit 0
