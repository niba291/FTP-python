#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
import os
from ftplib         import FTP
from classGeneral   import classGeneral 
# CLASS======================================================================================================================
class classFTP:
    server      = "ftp.digitaldevsolutions.cl"
    user        = "admin@digitaldevsolutions.cl"
    password    = "administration/*-123"
    port        = 21
    ftp         = None
    objGeneral  = classGeneral()

    def __init__(self): 
        try:
            self.ftp = FTP()
            self.ftp.connect(self.server, self.port)
            self.ftp.login(self.user, self.password)
        except Exception as ex:
            self.objGeneral.eventException(ex)

    def close(self):
        try:
            return self.ftp.close()
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def welcome(self):
        try:
            return self.ftp.getwelcome()
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def directory(self):
        try:
            return self.ftp.pwd()
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def createDirectory(self, name = ""):
        try:
            if(str(name) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'name'"
                }

            return {
                "error"     : False,
                "response"  : self.ftp.mkd(name)
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)
    
    def deleteDirectory(self, name = ""):
        try:
            if(str(name) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'name'"
                }

            return {
                "error"     : False,
                "response"  : self.ftp.rmd(name)
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def changeDirectory(self, path = ""):
        try:
            if(str(path) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'path'"
                }
                
            return {
                "error"     : False,
                "response"  : self.ftp.cwd(path)
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def listDirectory(self):
        try:
            response    = []

            for file in self.ftp.mlsd():
                response.append(file)

            return {
                "error"     : False,
                "response"  : response
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)
    
    def deleteFile(self, file = ""):
        try:
            if(str(file) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'file'"
                }
            
            return {
                "error"     : False,
                "response"  : self.ftp.delete(file)
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def uploadFile(self, path = ""):
        try:
            if(str(path) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'path'"
                }

            file        = path.split("\\")
            fileName    = file[-1]
            file        = open(path, "rb")
            response    = self.ftp.storbinary("STOR " + fileName, file)
            file.close()
            return {
                "error"     : False,
                "response"  : response
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def uploadFolder(self, path = ""):
        try:
            files    = os.listdir(path)
            os.chdir(path)
            for file in files:
                print(file)
                if os.path.isfile(file):
                    fileChild   = open(file, "rb")
                    self.ftp.storbinary("STOR %s" % file, fileChild)
                    fileChild.close()
                elif os.path.isdir(file):
                    self.createDirectory(file)
                    self.changeDirectory(file)
                    self.uploadFolder(file)
            self.changeDirectory("..")
            os.chdir("..")
        except Exception as ex:
            return self.objGeneral.eventException(ex)

    def rename(self, old = "", new = ""):
        try:
            if(str(old) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'old'"
                }

            if(str(new) == ""):                
                return {
                    "error"     : True,
                    "response"  : "Not existing 'new'"
                }

            return {
                    "error"     : False,
                    "response"  : self.ftp.rename(old, new)
                }
        except Exception as ex:
            return self.objGeneral.eventException(ex)
    
    def getFile(self, path = ""):
        try:

            # with open('nombre_texto_local.txt', 'w') as local_file:  # Abre un archivo de texto localmente para escritura
            #     response = ftp.retrlines('RETR texto.txt', local_file.write)
            #     if response.startswith('226'):  # Transferencia completa
            #         print('Transferencia completa')
            #     else:
            #         print('Error de transferencia. El archivo puede estar incompleto o corrupto.')
            # Para archivos binarios
            file    = open(path, "wb")
            self.ftp.retrbinary("RETR " + path, local_file.write)
                # ftp.retrbinary('RETR imagen.png', local_file.write)
            
            return {
                "error"     : False,
                "response"  : response
            }
        except Exception as ex:
            return self.objGeneral.eventException(ex)
# CLOSE CLASS================================================================================================================
aux = classFTP()
print(aux.uploadFolder(os.getcwd()))
# print(aux.uploadFile(os.getcwd()+"\main.py"))
