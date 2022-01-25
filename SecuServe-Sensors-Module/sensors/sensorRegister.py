"""
this is the class to register and configure the sensors for zwave
"""

from  time import sleep
from openzwave.network import ZWaveNetwork
from openzwave.controller import ZWaveController
from utils import consoleLog
from datetime import datetime
from pydispatch import dispatcher

class sensorRegister(object):

  

