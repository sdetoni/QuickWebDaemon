'''
####################################################
# Written by Steven De Toni 2019
####################################################
'''
import daemon.HTTPDaemon  as HTTPDaemon
import daemon.GlobalFuncs as GF
import socket
import sys
import logging

# handle default strings and utf8 and not 7bit ascii
#reload(sys)
#sys.setdefaultencoding('utf8')

# Main web server loop to init, run, shutdown
GF.DaemonRunningState = GF.DAEMON_RUNMODE_RUN
while GF.DaemonRunningState == GF.DAEMON_RUNMODE_RUN:
    # init Config, DB, and Logging
    GF.initGlobalFuncs("./config/daemon.cfg")

    thrdDaemon = False
    httpPort   = GF.Config.getSettingValue('HTTP_PORT')
    httpsPort  = GF.Config.getSettingValue('HTTPS_PORT')

    # Start the HTTP server and run as thread
    if httpPort:
        if httpsPort:
            thrdDaemon = True
        HTTPDaemon.startDaemon (host_name        = GF.Config.getSettingStr  ('HTTP_SERVERNAME',         socket.gethostname()),
                                port_number      = httpPort,
                                homeDir          = GF.Config.getSettingStr  ('HTTP_HOME_DIRECTORY',     './html'),
                                homeScriptName   = GF.Config.getSettingStr  ('HTTP_HOME_SCRIPT_NAME',   'index.py'),
                                mimeTypeFilename = GF.Config.getSettingStr  ('HTTP_MIMETYPES_FILENAME', './config/mimetypes.txt'),
                                serve_via_ssl    = False,
                                threaded         = thrdDaemon)

    # Start the HTTPS server, and run as a blocking process
    if httpsPort:
        HTTPDaemon.startDaemon (host_name        = GF.Config.getSettingStr  ('HTTP_SERVERNAME',         socket.gethostname()),
                                port_number      = GF.Config.getSettingValue('HTTPS_PORT',              4430),
                                ssl_server_pem   = GF.Config.getSettingStr  ('HTTPS_SSL_SERVER_PEM',    './config/server.pem'),
                                homeDir          = GF.Config.getSettingStr  ('HTTP_HOME_DIRECTORY',     './html'),
                                homeScriptName   = GF.Config.getSettingStr  ('HTTP_HOME_SCRIPT_NAME',   'index.py'),
                                mimeTypeFilename = GF.Config.getSettingStr  ('HTTP_MIMETYPES_FILENAME', './config/mimetypes.txt'),
                                serve_via_ssl    = True,
                                threaded         = False)

    # TODO: To shutdown HTTPDaemon, call GlobalFuncs.shutdownDaemon(), or GlobalFuncs.restartDaemon()

    logging.info (__name__+" : HTTP Daemon Shutdown ...")
    GF.shutdownGlobalFuncs()

    if GF.DaemonRunningState == GF.DAEMON_RUNMODE_RESTART:
        logging.info(__name__ + " : HTTP Daemon Restarting ...")
        GF.DaemonRunningState = GF.DAEMON_RUNMODE_RUN
