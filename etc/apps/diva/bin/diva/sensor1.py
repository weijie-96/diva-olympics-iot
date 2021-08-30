#!/usr/bin/python

import time
import sys
import os
import grovepi
import math

sensor_reading1 = 1234.5
sensor_reading2 = 5432.1

print ("{\"time\":\"%s\",\"reading1\":%f,\"reading2\":%f}" % (time.ctime(), sensor_reading1, sensor_reading2))
