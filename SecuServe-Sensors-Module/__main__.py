""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import asyncio
from datetime import datetime
import time
import zmq

# There are many different radio libraries but they all have the same API

from zigpy_znp.zigbee.application import ControllerApplication
from utils import consoleLog as log
from utils import const
from utils import socketcomm
from pipeline import MainListener


context = zmq.Context(io_threads=4)

sender = context.socket(zmq.PUSH)
recv = context.socket(zmq.PULL)

# zmq setup
sender.bind("tcp://"+"127.0.0.1:5002")
recv.connect("tcp://"+"127.0.0.1:5001")


# the main menthod that runs 

#TODO: set up devices that join to be saved to database via the databse module 
# There are many different radio libraries but they all have the same API
from zigpy_znp.zigbee.application import ControllerApplication


# man methond 
async def main():
    log.info("starting stuff initing...")
    socketcomm.sendProgramStatus(socketcomm,sender,"Starting Sensors module...",str(datetime.now))
    
    app = ControllerApplication(ControllerApplication.SCHEMA({
        "database_path": "../SecuServeFiles/device",
        "device": {
            "path": "/dev/ttyUSB0",
        }
    }))

    listener = MainListener.MainListener(app)
    app.add_listener(listener)

    MainListener.MainListener.app = app
    MainListener.MainListener.socket = sender
  
   

    
    
  
    await app.startup(auto_form=True)

    # Permit joins for a minute
    await app.permit(60)
    await asyncio.sleep(60)

    # Just run forever
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
    

