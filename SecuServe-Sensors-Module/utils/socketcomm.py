"""
this file is for socket communication dev it holds all the methods required to call stuff with scokets
TODO: to send logs over network 
"""


import consoleLog 
import time



# Sends Program Status to Socket
def sendProgramStatus(self, sender, status, currenttime):
    consoleLog.Debug("sending Program status to zmq socket")
    sender.send_string("SENSORS")
    sender.send_json(
        {
            "status": str(status),
            "time": str(currenttime),
        }
    )
    time.sleep(0.5)
    consoleLog.PipeLine_Ok("Sent Program status to zmq socket")


# this sends the device that joined the network to the zmq socket
def sendSensorInfoOnJoin(self, sender, ieee, ieeenum, network, currenttime):
    consoleLog.Debug("sending Sensor info to zmq socket")
    sender.send_string("SENSOR")
    sender.send_json(
        {
            "ieee": str(ieee),
            "ieenum": str(ieeenum),
            "network": str(network),
            "time": str(currenttime),
        }
    )
    time.sleep(0.5)
    consoleLog.PipeLine_Ok("Sent Sensor info to zmq socket")


# captured sensor data senst over the etwrok
def sendSensorCapturedData(self, sender, ieee, network, sensordata, currenttime):
    consoleLog.Debug("sending Sensor info to zmq socket")
    sender.send_string("SENSOR")
    sender.send_json(
        {
            "ieee": str(ieee),
            "network": str(network),
            "sensor_data": str(sensordata),
            "time": str(currenttime),
        }
    )
    time.sleep(0.5)
    consoleLog.PipeLine_Ok("Sent Sensor info to zmq socket")
