#!flask/bin/python
 

import time, os, sys
import inspect
from os import environ as env
#import shade

from flask import Flask, jsonify
import subprocess
import create as C #import cow
import delete as D

app = Flask(__name__)



@app.route('/QTLaaS/api/create', methods=['GET'])
def create():
    C.vmcreate()
    #data=subprocess.check_output(["cowsay","Hello student"])
    return "data"

@app.route('/QTLaaS/api/delete', methods=['GET'])
def delete():
    D.vmdelete()
    #data=subprocess.check_output(["cowsay","Hello student"])
    return "data"
    
if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)
