"""
this is the base class for holding a sensor object 
for this module
"""
from utils import consoleLog as log 
import json 

class SensorBase(object):

    # sensor local vars
    _SensorName : str
    _SensorType : str
    _SensorAddress:str

    _SensorDefinition:str
    _SensorSupported:str
    _SenorSource:str

    _SensorEndPoints:str
    _SensorDateCode:str

    

    #* this is the base useage of the class
    def __init__(self,name:str,type:str, address:str, definition:str, supported:str, source:str, enpoints:str, datecode:str) -> list:

        self.setSensorname(name)




    # sets the sensor name for the nice sensor object
    def setSensorname(self,name:str) -> str:
        
        if name is None or "":
            log.Error("Cannot have a blank sensor name!")
            return TypeError("Sensor name cannot be blank")
        
        if name.isnumeric():
            log.Warning("Sensor can have number name but dont complain when you cant keep trak of them...")
            self._SensorName = name
        
        else:
            self._SensorName = name

    #sets the type of the sensor 
    def setSensorType(self,type:str) -> str:
        

        if type is None or "":

            log.Error("Cannot have a blank sensor type!")
            return TypeError("Sensor type cannot be blank")
        
        if type.isnumeric():

            log.Error("Cannot have a number sensor type!")
            return TypeError("Sensor type cannot be a number")

        else:
            self._SensorType = type


    # returns the address as and int 
    
    def setSensorAddress(self, address:str) -> str:


        if address is None or "":

            log.Error("Cannot have a blank sensor type!")
            return TypeError("Sensor type cannot be blank")
        

        if not address.isnumeric():

            log.Error("Sensor Address cannot be non numeric!")
            return TypeError("Sensor Address cannot be a string")

        if address.isnumeric():
            self._SensorAddress = address


    # saves the data passed into the sesor def 
    def setSensorDefinition(self, sensordef:str):

        if sensordef is None or "":
            log.Error("Cannot have a blank sensor def!")
            return TypeError("Sensor def cannot be blank")

        else:

            self._SensorDefinition = sensordef

    # set sensor supported status 
    def setSensorSupported(self, supported:str):
        
        if supported is None or "":
            log.Error("Cannot have a blank sensor support!")
            return TypeError("Sensor support cannot be blank")
        else:
                
            self._SensorSupported = supported

    
    
