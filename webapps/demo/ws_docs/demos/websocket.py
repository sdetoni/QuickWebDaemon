self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE

import logging
import os
cwd = os.getcwd()

logging.info ("working dir:"+str(cwd))

# enter web socket receive/response loop ...
while True:
    msg = self.ws_WaitMessage()

    # TODO : Add user parsing/processing of message here
    self.output(f"Server received msg {msg}")

