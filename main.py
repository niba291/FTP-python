#!/usr/bin/env python
# -*- coding: utf-8 -*-
# IMPORT=====================================================================================================================
import os
import sys
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
# VARIABLES==================================================================================================================
json                    = None
app                     = Flask(__name__)
CORS(app)
# FUNCTION===================================================================================================================
@app.route("/listFolder", methods = ["POST"])
def listAvatars():
    # obj     = controllerAvatar()    
    # return self.objGeneral.responseCode(301, "Not existing 'name'")
    return jsonify({"status": 0, "response": "d"}), 200
# CONFIG=====================================================================================================================
if __name__ == "__main__":
    app.run(debug=True, port=5000)