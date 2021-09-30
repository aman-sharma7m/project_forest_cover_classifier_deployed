"""
This is the main work for training the model
prepared by:Aman
"""
from sklearn.model_selection import train_test_split
from data_ingestion import data_loader
from data_preprocessing import preprocessing
from data_preprocessing import clustering
from best_model_finder import tuner
from application_logging import logger
from file_operations import file_methods

class trainModel:
    def __init__(self):
        self.log_writer=logger.App_Logger()
        self.file_object=open('Training_Logs/ModelTrainingLog.txt','a+')
    def trainingModel(self):
        self.log_writer.log(self.file_object,"Start of the training !!")
        try:
            #getting the data from the source
            data_getter=data_loader.Data_Getter(self.file_object,self.log_writer)
            data=data_getter.get_data()

            # doing preprocessing
            preprocessor=preprocessing.Preprocessor(self.file_object,self.log_writer)

            data=preprocessor.enocdeCategoricalvalues(data)

            X=data.drop(['class'],axis=1)
            Y=data['class']

            X, Y = preprocessor.handleImbalanceDataset(X, Y)



            # Applying clusturing

            kmeans=clustering.KMeansClustering(self.file_object,self.log_writer)
            number_of_clusters=kmeans.elbow_plot(X)

            # divide into clusters
            X=kmeans.create_clusters(X,number_of_clusters)

            # create a new column in the dataset consisting of the corresponding cluster assignments.
            X['Labels'] = Y

            # getting the unique clusters from our dataset
            list_of_clusters = X['Cluster'].unique()

            """parsing all the clusters and looking for the best ML algorithm to fit on individual cluster"""


        except Exception:
            # logging the unsuccessful Training
            self.log_writer.log(self.file_object, 'Unsuccessful End of Training')
            self.file_object.close()
            raise Exception
