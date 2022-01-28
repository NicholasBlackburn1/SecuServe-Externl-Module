"""
this is the file holds the Pipeline and controls Pipline
watch dog count to frozen 
"""
from asyncio.windows_utils import pipe
from enum import Enum


from zmq.sugar.frame import Message
from pipeline import videoRequired
from utils import consoleLog
from utils import const
from pipeline import state
import SensorPipeline as pipeline

from datetime import datetime, time


class States(Enum):
    IDLE = 0
    SETUP_PIPELINE = 1
    PULL_DATA = 2
    RUN_RECONITION = 4
    ERROR = 5


# Start of our state.States
class SetupPipeLine(state.State):
    """
    The state.State which Sets Up Whole opencv pipeline
    """

    def on_event(self, event, sender,receiver,poller):
        if event == States.SETUP_PIPELINE:
            pipeline.SensorPipeline.setupPipeline(pipeline.SensorPipeline(),sender,receiver,poller)
            self.next_state(States.PULL_DATA)

            return PullData()

        return self


class PullData(state.State):
    """
    The state.State which Trains the Reconized face Models
    """

    def on_event(self, event, sender,receiver,poller,zig):
        if event == States.PULL_DATA:
            pipeline.SensorPipeline.pullData(pipeline.SensorPipeline,sender,receiver,poller,zig)
          # pipeline.SensorPipeline.
            self.next_state(States.RUN_RECONITION)
            return RunReconitionPipeLine()

        return self


class RunReconitionPipeLine(state.State):
    """
    The state.State which Reconizes Faces
    """

    def on_event(self, event, sender,recv,poller,imagesocket):
        if event == States.RUN_RECONITION:
           

            if (videoRequired.RequiredCode.reconitionPipeline(videoRequired.RequiredCode(), sender,recv,poller,imagesocket) == States.ERROR):
                return Error()
         

        return self


class Idle(state.State):
    """
    The state.State which The program waits for a face to be spotted
    """

    def on_event(self, event, sender,receiver,poller,imagesocket):
        if event == States.IDLE:
            videoRequired.consoleLog.Warning("Idleing....")
            videoRequired.time.sleep(0.5)

        return self


class Error(state.State):
    """
    The state.State which The program waits for a face to be spotted
    """

    msg = None

    def __init__(self, message):
        self.msg = message

    def on_event(self, event, sender):
        if event == States.ERROR:
            videoRequired.consoleLog.Error("ERROR....")
            sender.send_string("ERROR")
            sender.send_json({"error": str(self.msg), "time": str(datetime.now())})
            return

        return self


class PipeLine(object):
    """
    A simple state.State machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self):
        """Initialize the components."""

        # Start with a default state.State.
        self.State = SetupPipeLine()

    def on_event(self, event, sender,receiver,poller,imagesocket):
        """
        This is the bread and butter of the state.State machine. Incoming events are
        delegated to the given state.States which then handle the event. The result is
        then assigned as the new state.State.
        """

        # The next state.State will be the result of the on_event function.
        self.State = self.State.on_event(event, sender,receiver,poller,imagesocket)

    def getCurrentStat(self):
        return self.State
