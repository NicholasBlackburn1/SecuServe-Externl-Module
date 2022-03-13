""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import asyncio
import time
import zmq

# There are many different radio libraries but they all have the same API

from zigpy_znp.zigbee.application import ControllerApplication
from utils import consoleLog as log
from utils import const

from pipeline import MainListener


context = zmq.Context(io_threads=4)
sender = context.socket(zmq.PUB)


# the main menthod that runs 
# 
# 

#TODO: get de
# There are many different radio libraries but they all have the same API
from zigpy_znp.zigbee.application import ControllerApplication


# man methond 
async def main():
    log.info("starting stuff initing...")
    app = ControllerApplication(ControllerApplication.SCHEMA({
        "database_path": "../SecuServeFiles/device",
        "device": {
            "path": "/dev/ttyUSB0",
        }
    }))

    listener = MainListener.MainListener(app)
    app.add_listener(listener)
    MainListener.MainListener.app = app
  
   

    
    
  
    await app.startup(auto_form=True)

    # Permit joins for a minute
    await app.permit(60)
    await asyncio.sleep(60)

    # Just run forever
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())
    

