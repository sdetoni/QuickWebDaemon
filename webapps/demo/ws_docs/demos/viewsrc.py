self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE
import os
import html

postData = self.getCGIParametersFormData ()

if "page" in postData:
    f            = os.path.basename(__file__)
    p            = self.path.split('?')[0].split (f)[0]
    viewsrcPath  = os.path.abspath(self.homeDir + p)
    fileViewPath = os.path.abspath(viewsrcPath + '/' + postData["page"])

    if not fileViewPath.startswith(viewsrcPath):
        output ("invalid path")
        exit(0)

    if (("out_html" in postData) and (postData["out_html"].lower() == 'y')):
        output('<html><pre>')
        with open(fileViewPath, 'r') as file:
                output(html.escape(file.read(), quote=True))
        output('</pre></html')
    else:
        with open(fileViewPath, 'r') as file:
                output(file.read())