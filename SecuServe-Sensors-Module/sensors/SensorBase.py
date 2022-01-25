"""
this is the base class for holding a sensor object 
for this module
"""
from utils import consoleLog as log 

class SensorBase(object):

    # sensor local vars
    _SensorName : str
    _SensorType : str
    _SensorAddress:int

    _SensorDefinition:list
    _SensorSupported:bool
    _SenorSource:str

    _SensorEndPoints:list
    _SensorDateCode:str

    

    #* this is the base useage of the class
    def __init__(name:str,type:str, address:int, definition:list, supported:bool, source:str, enpoints:list, datecode:str) -> None:
        super().__init__()



    # sets the sensor name for the nice sensor object
    def setSensorname(self,name:str):
        
        if name is None or "":
            log.Error("Cannot have a blank sensor name!")
            return TypeError("Sensor name cannot be blank")
        
        if name.isnumeric():
            log.Warning("Sensor can have number name but dont complain when you cant keep trak of them...")
            self._SensorName = name
        
        else:
            self._SensorName = name
    
            


    