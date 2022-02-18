""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import asyncio
import zmq
from utils import consoleLog
from utils import const

from digi import xbee
from digi.xbee.devices import XBeeDevice

context = zmq.Context(io_threads=4)
sender = context.socket(zmq.PUB)

# the main menthod that runs 
# 
# 
def main():
    consoleLog.PipeLine_init("Initing Zmq..... ")
    # enables stuff to be sent on zmq
    sender.bind(const.zmq_send)

    consoleLog.info("Starting Zigbee module.....")
    device = XBeeDevice("/dev/ttyUSBO", 9600)
    device.open()
    
    consoleLog.Warning("got data from zigbee devices"+device.read_data())


    


if __name__ == "__main__":
    main()