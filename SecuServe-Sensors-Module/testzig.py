import asyncio
import utils.consoleLog as log

# There are many different radio libraries but they all have the same API
from zigpy_znp.zigbee.application import ControllerApplication


class MainListener:
    """
    Contains callbacks that zigpy will call whenever something happens.
    Look for `listener_event` in the Zigpy source or just look at the logged warnings.
    """


    dev = None

    def __init__(self, application):
        log.PipeLine_Ok("starting app....")
        self.application = application

    def device_joined(self, device):
        log.Warning(f"Device joined: {device}")
        self.dev = device

    def attribute_updated(self, device, cluster, attribute_id, value):
        log.Warning(f"Received an attribute update {attribute_id}={value}"
              f" on cluster {cluster} from device {device}")


async def main():
    log.info("starting stuff initing...")
    app = ControllerApplication(ControllerApplication.SCHEMA({
        "database_path": "../SecuServeFiles/device.db",
        "device": {
            "path": "/dev/ttyUSB0",
        }
    }))

    listener = MainListener(app)
    app.add_listener(listener)

    #.add_device(MainListener.dev,MainListener.dev.)
   

    await app.startup(auto_form=True)

    # Permit joins for a minute
    await app.permit(60)
    await asyncio.sleep(60)

    # Just run forever
    await asyncio.get_running_loop().create_future()


if __name__ == "__main__":
    asyncio.run(main())