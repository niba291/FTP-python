#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
# from classEmail             import classEmail
from classException         import classException 
# CLASS======================================================================================================================
class classGeneral:
# VAIRABLES==================================================================================================================
# INIT=======================================================================================================================
    def __init__(self): 
        pass

    def eventException(self, ex):
        try:
            # objEmail        = classEmail()
            objEx           = classException(ex)
            # objEmail.send({
            #     "to"        : "lectoresdelmanga.errors@gmail.com",
            #     "subject"   : "Error rank 1",
            #     "body"      : str(objEx.getMessageElement())
            # })
            return objEx.getMessageJson()
        except Exception as ex:
            print(ex)

    def responseCode(self, code = 0, response = ""):
        try:
            match code:
                case 200:
                    return { 
                        "error"     : False, 
                        "code"      : 200, 
                        "response"  : response
                    }
                case 301:
                    return { 
                        "error"     : True, 
                        "code"      : 301, 
                        "response"  : response
                    }
        except Exception as ex:
            return self.eventException(ex);

    def getType(self, element):
        try:            
            return str(type(element)).replace("<class", "").replace(">","").replace("'","").strip().lower()
        except Exception as ex:
            return self.eventException(ex)

    def validateJSON(self, data):
        try:
            if self.getType(data) == "dict":
                return True
            return False
        except Exception as ex:
            return self.eventException(ex)
# CLOSE CLASS================================================================================================================