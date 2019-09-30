import daemon.DBIO as DBIO
import datetime
import logging
import daemon.GlobalFuncs as GF
import sys

class DemoDB (DBIO.DBIO):
    def __buildTables__ (self):
        try:
            dbVersion = self.sqlRtnResults('select version from db_version')[0]['version']
            logging.info('DBIO.__buildTables__ DB version detected : ' + str(dbVersion))
        except Exception as ex:
            super().__buildTables__()
            super().__updateDB__()
            dbVersion = self.sqlRtnResults('select version from db_version')[0]['version']

        if (dbVersion == 1.0):
            # update from version 1.0 to 1.1
            logging.info('DBIO.__buildTables__ Create Table: demo')
            self.sqlNoResults("create table if not exists demo (id numeric, info text)")
            self.commit()

        # if (dbVersion == x.x):
            # TODO : future SQL to create tables, indexes here

    def __updateDB__ (self):
        try:
            dbVersion = self.sqlRtnResults('select version from db_version')[0]['version']
            if dbVersion < self.version:
                if dbVersion == 1.0:
                    logging.info ("Updating db from version 1.0 to 1.1")
                    # todo : add SQL update data in tables
                    self.sqlNoResults("update db_version "
                                      "set version   = ?,"
                                      "    timestamp = ?", (1.1,datetime.datetime.now()))
                    dbVersion = 1.1
                    self.commit ()

                # if dbVersion == x.x:
                #   TODO : future updates here
        except Exception as ex:
            logging.error('DBIO.updateDB failure ' + str(ex))
            sys.exit(1)

DB = DemoDB(dbFilename=GF.Config.getSettingStr('demo/DB_FILENAME', DBIO.DB_NAME),
            version=GF.Config.getSettingValue('demo/DB_VERSION', DBIO.DB_VERSION),
            sqlexec_maxtime=GF.Config.getSettingValue('demo/DB_SQLEXEC_MAXTIME', DBIO.SQLEXEC_MAXTIME),
            sqllock_maxtime=GF.Config.getSettingValue('demo/DB_SQLLOCK_MAXTIME', DBIO.SQLLOCK_MAXTIME))
