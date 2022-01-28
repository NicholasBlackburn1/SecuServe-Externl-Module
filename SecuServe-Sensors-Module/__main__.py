""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import zmq
from utils import consoleLog
from utils import const

from zigbee2mqtt import Zigbee2MQTT

context = zmq.Context(io_threads=4)
sender = context.socket(zmq.PUB)

# the main menthod that runs 
async def main():
    consoleLog.PipeLine_init("Initing Zmq..... ")
    # enables stuff to be sent on zmq
    sender.bind(const.zmq_send)

    consoleLog.info("Starting Zigbee module.....")

    z2m = Zigbee2MQTT(base_topic="/zigbee2mqtt",)
    

    