from datetime import datetime
from application_logging import logger
from Training_Raw_data_validation.rawValidation import Raw_Data_validation
from DataTypeValidation_Insertion_Training.DataTypeValidation import dBOperation
from DataTransform_Training.DataTransformation import dataTransform

class train_validation:
    def init(self,path):
        self.log_writer=logger.App_Logger()
        self.file_object=open('Training_Logs/Training_Main_log.txt','a+')
        self.raw_data=Raw_Data_validation(path)
        self.dBOperation=dBOperation()
        self.dataTransform=dataTransform()


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
            self.log_writer.log(self.file_object, "Starting Data Transforamtion!!")
            # replacing blanks in the csv file with "Null" values to insert in table
            self.dataTransform.addQuotesToStringValuesInColumn()

            self.log_writer.log(self.file_object, "DataTransformation Completed!!!")

            self.log_writer.log(self.file_object,"Creating Training_Database and tables on the basis of given schema!!!")

            # create database with given name, if present open the connection! Create table with columns given in schema
            self.dBOperation.createTableDb('Training',column_names)
            self.log_writer.log(self.file_object,"Table creation Completed!!")
            self.log_writer.log(self.file_object, "Insertion of Data into Table started!!!!")
            # insert csv files in the table
            self.dBOperation.insertIntoTableGoodData('Training')
            print("insert complete")
            self.log_writer.log(self.file_object, "Insertion in Table completed!!!")
            self.log_writer.log(self.file_object, "Deleting Good Data Folder!!!")
            # Delete the good data folder after loading files in table
            self.raw_data.deleteExistingGoodDataTrainingFolder()
            self.log_writer.log(self.file_object, "Good_Data folder deleted!!!")
            self.log_writer.log(self.file_object, "Moving bad files to Archive and deleting Bad_Data folder!!!")
            # Move the bad files to archive folder
            self.raw_data.moveBadFilesToArchiveBad()
            self.log_writer.log(self.file_object, "Bad files moved to archive!! Bad folder Deleted!!")
            self.log_writer.log(self.file_object, "Validation Operation completed!!")
            self.log_writer.log(self.file_object, "Extracting csv file from table")
            # export data in table to csvfile
            self.dBOperation.selectingDatafromtableintocsv('Training')
            self.file_object.close()

        except Exception as e:
            self.file_object.close()
            raise e

