"""
this class is for setting up the pipeline for sensor data management 
set up sensors, and pull data from them


what this pipeline does is when it pulls from sensors convert it into a message to zmq that could be used in main pipeline 
"""


from utils import consoleLog as log 
import time 
from datetime import datetime

class SensorPipeline(object):


    #this allows me to set up and init the pipeline
    def setupPipeline(self,sender, recv, poller):

        self.sendProgramStatus(sender,"starting Pipeline....","Initing Pipeline",datetime.now())
        log.info("Starting to settup Sensor Pipeline")


    
    
    def pullData(self, sender, recv, puller,zig):
        
        pass





    
     # Sends Program Status to Socket
    def sendProgramStatus(self, sender, status, pipelinePos, currenttime):
        log.Debug("sending Program status to zmq socket")
        sender.send_string("PIPELINE")
        sender.send_json(
            {
                "status": str(status),
                "pipelinePos": str(pipelinePos),
                "time": str(currenttime),
            }
        )
        time.sleep(0.5)
        log.PipeLine_Ok("Sent Program status to zmq socket")