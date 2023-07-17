#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
import sys
import os
import datetime
from tabulate import tabulate
# CLASS======================================================================================================================
class classException:
# VAIRABLES==================================================================================================================
    exc_type                = None    
    exc_obj                 = None
    exc_tb                  = None
    fname                   = None
    strSheet                = None
    strMessage              = None
    jsonMessage             = None
    dataMessage             = None
    headersMessage          = None
    nameApp                 = "FtpPython"  
# INIT=======================================================================================================================
    def __init__(self, ex): 
        self.exc_type, self.exc_obj, self.exc_tb = sys.exc_info()
        self.fname          = os.path.split(self.exc_tb.tb_frame.f_code.co_filename)[1]    
        self.strSheet       = str(self.fname)
        self.jsonMessage    = { 
                                "status"    : -1, 
                                "exception" : type(ex).__name__, 
                                "message"   : str(ex)
                            }
        self.dataMessage    = [self.nameApp, self.strSheet, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), str(self.exc_tb.tb_lineno), type(ex).__name__, str(ex)]
        self.headersMessage = ["APP", "FILE", "DATE", "LINE", "EXCEPTION", "MESSAGE"]        
        self.strMessage     = tabulate([self.dataMessage], self.headersMessage)

    def getMessageElement(self):
        return [self.headersMessage, self.dataMessage]

    def getMessage(self):
        return self.strMessage
    
    def getMessageJson(self):
        return self.jsonMessage
# CLOSE CLASS================================================================================================================