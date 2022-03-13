""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import asyncio
import time
import zmq

# There are many different radio libraries but they all have the same API

from zigpy_znp.zigbee.application import ControllerApplication
from utils import consoleLog
from utils import const



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
    
    
    consoleLog.PipeLine_Ok("connected to zigbee usb ~")
    device.open(force_settings=True)
    
    consoleLog.info("operating mode of zigbee is "+device._get_operating_mode())
    # Get the network.
    xnet = device.get_network()

    xnet.start_discovery_process(deep=True, n_deep_scans=1)
    while xnet.is_discovery_running():
        time.sleep(0.5)

    # Get the list of the nodes in the network.
    nodes = xnet.get_devices()


    consoleLog.info("devices found "+str(nodes))

        
    consoleLog.Warning("got data from zigbee devices"+device.read_data())


    


if __name__ == "__main__":
    main()