self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE

postData = self.getCGIParametersFormData ()

dt = ""
if "usertxt" in postData:
    dt = "<p> Data transferred: %s </p>" % postData["usertxt"]

output ('''
<html>
%s
<form method="post">
    </p>Enter some text</p><input name="usertxt" type="text"\>
    <input type="submit" value="submit your text">
</forms>
</html>
''' % dt)