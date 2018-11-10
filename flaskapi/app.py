#!flask/bin/python
 

import time, os, sys
import inspect
from os import environ as env
#import shade

from flask import Flask, jsonify, render_template, request
import subprocess
import create as C #import cow
import delete as D
import ansible_master as A
import fileupload_otherserver as F
app = Flask(__name__)

#### convert existing server to ansible_master api

@app.route('/QTLaaS/api/create_ansiblemaster', methods=['GET'])
def createansible():
    A.ansiblemaster()
    return "message"

#### Create new VM  api

@app.route('/QTLaaS/api/create', methods=['GET'])
def create():
    servername = request.args.get('server')
    C.vmcreate(servername)
    return "message"

#### delete  VM api

@app.route('/QTLaaS/api/delete', methods=['GET'])
def delete():
    servername = request.args.get('server')
    print(servername)
    D.vmdelete(servername)
    return "message"


#### file upload other server api    
@app.route('/uploader', methods = [ 'GET' , 'POST'])
def upload_file():
    if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      F.uploadserver()
      return 'file uploaded successfully'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0',debug=True)

