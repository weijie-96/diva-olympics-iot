#!/usr/bin/python

import time
import sys
import os


localip = os.popen("hostname -I | awk '{print $1}'").read()
localip = localip.replace('\n', '').replace('r', '')
print ("{\"time\":\"%s\",\"iplocal\":\"%s\"}" % (time.ctime(), localip))
