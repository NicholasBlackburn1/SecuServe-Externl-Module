"""
this is the class to register and configure the sensors for zwave
"""

from openzwave.network import ZWaveNetwork
from openzwave.controller import ZWaveController
class sensorRegister(object):

    mainDevice = None
    network = None

    #Sets up Zwave device
    def setupZwaveGateWay(self,device):
                # Initialise openzwave.
        self.mainDevice = ZWaveController(device, user_path=".")
        self.mainDevice.set_console_output(False)
        self.mainDevice.lock()
        self.network = ZWaveNetwork(self.mainDevice)

    # starts the zwave netowrk 
    def startNetwork(self):
        self.network.start()


    
        
    
