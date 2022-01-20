""""
Main class of the Sensors modules
TODO: NEED TO GET MY ZWAVE SUFF 
"""

import zmq
from utils import consoleLog
from utils import const

context = zmq.Context(io_threads=4)
sender = context.socket(zmq.PUB)

# the main menthod that runs 
def main():
    consoleLog.PipeLine_init("Initing Zmq..... ")
    # enables stuff to be sent on zmq
    sender.bind(const.zmq_send)

    consoleLog.info("Starting Zwave module.....")

    