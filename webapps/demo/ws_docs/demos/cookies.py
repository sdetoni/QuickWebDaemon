self = eval('self'); output = self.output # this code is cosmetic to remove the red syntax highlight error from the pycharm IDE

import urllib

cookieID  = 'myCookieID'
tstCookie = self.sessionCookieJar[cookieID].value if cookieID in self.sessionCookieJar else None

if not tstCookie:
    # header & cookie directives must come first before any HTML output
    self.do_HEAD(otherHeaderDict={'Set-Cookie': cookieID + '=' + urllib.parse.quote_plus('Hello World Cookie')})

    output ("<p>Cookie Not Set!</p>")
    output("<p>Sending Cookie ...</p>")
    output("<a href='#' onclick='window.location.reload()'>Reload to view cookie</a>")
else:
    # header & cookie directives must come first before any HTML output
    self.do_HEAD(otherHeaderDict={'Set-Cookie': cookieID + '='})

    output("<p>Cookie Value was : " + urllib.parse.unquote_plus(tstCookie) +"</p>")
    output("<p>Cleared Cookie ...</p>")
    output("<a href='#' onclick='window.location.reload()'>Reload to set cookie</a>")