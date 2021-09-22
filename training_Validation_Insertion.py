from datetime import datetime
from application_logging import logger
from Training_Raw_data_validation.rawValidation import Raw_Data_validation


class train_validation:
    def init(self,path):
        self.log_writer=logger.App_Logger()
        self.file_object=open('Training_Logs/Training_Main_log.txt','a+')
        self.raw_data=Raw_Data_validation(path)


    def train_validation(self):
        try:
            self.log_writer.log(self.file_object,'Start of Validation on files for training!!!')

            # extracting vlaues from training schema
            LengthOfDateStampInFile,LengthOfTimeStampInFile,column_names,noofcolumns=self.raw_data.valuesFromSchema()

            #1st check regex to validate filename
            regex=self.raw_data.manualRegexCreation()

            #validating file names of training files
            self.raw_data.validationFileNameRaw(regex,LengthOfDateStampInFile,LengthOfTimeStampInFile)

            #2nd check to check column length
            self.raw_data.validateColumnLength(noofcolumns)

            #3rd check to checkk any column is having missing values
            self.raw_data.validateMissingValuesInWholeColumn()

            self.log_writer.log(self.file_object,'Raw Data Validation Complete!!')

            self.log_writer.log(self.file_object,"Creating Training_Database and tables on the basis of given schema!!!")

            # create database with given name, if present open the connection! Create table with columns given in schema


        except Exception as e:
            self.file_object.close()
            raise e
