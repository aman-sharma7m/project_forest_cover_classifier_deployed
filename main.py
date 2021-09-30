from flask import Flask,request,render_template
from flask import Response
import os
from wsgiref import simple_server
from flask_cors import CORS,cross_origin
import numpy as np
import pandas as pd
from application_logging import logger
from training_Validation_Insertion import train_validation
from trainingModel import trainModel



app=Flask(__name__)
CORS(app)


@app.route('/',methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')


@app.route('/train',methods=['POST'])
@cross_origin()
def trainRouteClient():
    try:
        if request.json['folder_path'] is not None:
            path=request.json['folder_path']
            train_valObj=train_validation(path)

            train_valObj.train_validation()

            trainModelObj=trainModel()
            trainModelObj.trainingModel()

    except KeyError:
        return Response('error Ocurred %s'% KeyError)
    except ValueError:
        return Response('error Occured %s'% ValueError)
    except Exception as e:
        return Response('Error Ocurred %s' % e)
    return Response('Training Successfull!!!')



@app.route('/predict',methods=['POST'])
@cross_origin()
def predictRouteClient():
    pass



# port=int(os.getenv('PORT',5001))
# if __name__=='__main__':
#     host='0.0.0.0'
#     httpd=simple_server.make_server(host,port,app)
#     httpd.serve_forever()
