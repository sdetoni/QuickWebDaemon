self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE

import logging
import os
cwd = os.getcwd()

logging.info ("working dir:"+str(cwd))
vars = {'myVar': 'Blah Blah', 'count': 100, 'test':'helloworld'}
self.templateRun('temp_test.html', vars)