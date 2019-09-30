self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE

import logging
import os
cwd = os.getcwd()

logging.info ("working dir:"+str(cwd))
# set my variables used by loaded template
vars = {'myVar': '.PY Loaded Template',
        'count': 100,
        'test':'helloworld'}
self.templateRun('py_loaded_template.html', vars)
