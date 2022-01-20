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

    mainDevice = None
    network = None

    #Sets up Zwave device
    def setupZwaveGateWay(self,device):
        # Initialise openzwave.
        consoleLog.info("setting up Zwave Options")

        self.mainDevice = ZWaveController(device, user_path=".")
        self.mainDevice.set_console_output(False)
        self.mainDevice.lock()

        self.network = ZWaveNetwork(self.mainDevice)

        consoleLog.PipeLine_Ok("setup Zwave options successfully...")

    

    # when node updates
    def node_update(network, node):
         consoleLog.Warning('Node update : {}.'.format(node))

    # when valuse update
    def value_update(network, node, value):
        consoleLog.Warning('Value update : {}.'.format(value))

    # when Control Network updates
    def ctrl_message(state, message, network, controller):
       consoleLog.info('Controller message : {}.'.format(message))

    # starts the zwave netowrk 
    def startNetwork(self):
        self.network.start()
        
        


    # Connect to events
    def value_updated(network, node, value):
        now = datetime.now().isoformat()
        consoleLog.PipeLine_Data("%s: Value updated node_id: <%d>, label <%s> new value <%s> instance %d" % ( now, node.node_id, value.label, str(value.data), value.instance))


    #allowwws me to run stuff for the sensors
    def pullData(self):
        consoleLog.info("Startiting network data from zwave")
       
        while self.network.state != self.network.STATE_READY:
            sleep(1)
            
        
