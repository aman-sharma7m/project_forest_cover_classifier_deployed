from flask import Flask,request,render_template
from flask import Response
import os
from wsgiref import simple_server
from flask_cors import CORS,cross_origin
import numpy as np
import pandas as pd

app=Flask(__name__)
CORS(app)


@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/train',methods=['POST'])
@cross_origin()
def trainRouteClient():
    pass

@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRouteClient():
    pass



port=int(os.getenv('PORT',5001))
if __name__=='__main__':
    host='0.0.0.0'
    httpd=simple_server.make_server(host,port,app)
    httpd.serve_forever()
