"""
TODO: get this module to send stuff down the zmq pipeline to commuicate with db module 
"""


import utils.consoleLog as log
import asyncio
from zigpy import types as t



class MainListener:
    """
    Contains callbacks that zigpy will call whenever something happens.
    Look for `listener_event` in the Zigpy source or just look at the logged warnings.
    """


    dev = None
    app = None

    def _ieee_to_number(self, ieee):
        ieee_string = str(t.EUI64(map(t.uint8_t, ieee)))
        return int(ieee_string.replace(':', ''), 16)

    def _get_device_by_ieee(self, ieee_to_find):
        for ieee, dev in self.app.devices.items():
            if self._ieee_to_number(ieee) == ieee_to_find:
                return dev

    # rusnt at start upp
    def __init__(self, application):
        log.PipeLine_Ok("starting app....")
        self.application = application

# runs when stufff joins the netork 
    def device_joined(self, device):
        log.Warning(f"Device joined: {device}")
        
        self.dev = device

        # gets the information of the device 
        log.PipeLine_Data("device ieee" + str(device.ieee))
        log.PipeLine_Data("device network"+ str(device.nwk))
        log.PipeLine_Data(str({'ieee':str(device.ieee), 'network':str(device.nwk),'ieenum':str(self._ieee_to_number(device.ieee))}))
        
   

    # should update if it updates 
    def attribute_updated(self, device, cluster, attribute_id, value):
        log.Warning(f"Received an attribute update {attribute_id}={value}"
              f" on cluster {cluster} from device {device}")


    