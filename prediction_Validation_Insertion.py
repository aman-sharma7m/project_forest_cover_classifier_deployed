from datetime import datetime
from application_logging import logger
from Prediction_Raw_Data_Validation.predictionDataValidation import Prediction_Data_validation
from DataTypeValidation_Insertion_Prediction.DataTypeValidationPrediction import dBOperation
from DataTransformation_Prediction.DataTransformationPrediction import dataTransformPredict


class pred_Validation:
    def __init__(self,path):
        self.raw_data=Prediction_Data_validation(path)
        self.dataTransformation=dataTransformPredict()
        self.dBOperation=dBOperation()
        self.file_object=open('Prediction_Logs/Prediction_Log.txt','a+')
        self.log_writer=logger.App_Logger()

