import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

class Preprocessor:
    """
            This class shall  be used to clean and transform the data before training.

            Written By: iNeuron Intelligence
            Version: 1.0
            Revisions: None

    """
    def __init__(self,file_object,log_object):
        self.file_object=file_object
        self.logger_object=log_object

    def enocdeCategoricalvalues(self, data):
        data["class"] = data["class"].map(
            {"Lodgepole_Pine": 0, "Spruce_Fir": 1, "Douglas_fir": 2, "Krummholz": 3, "Ponderosa_Pine": 4, "Aspen": 5,
             "Cottonwood_Willow": 6})

        return data

    def handleImbalanceDataset(self, X, y):
        sample = SMOTE()
        X, y = sample.fit_resample(X, y)

        return X, y

    def scaleData(self, data):
        scalar = StandardScaler()

        num_data = data[
            ["elevation", "aspect", "slope", "horizontal_distance_to_hydrology", "Vertical_Distance_To_Hydrology",
             "Horizontal_Distance_To_Roadways", "Horizontal_Distance_To_Fire_Points"]]
        cat_data = data.drop(
            ["elevation", "aspect", "slope", "horizontal_distance_to_hydrology", "Vertical_Distance_To_Hydrology",
             "Horizontal_Distance_To_Roadways", "Horizontal_Distance_To_Fire_Points"], axis=1)
        scaled_data = scalar.fit_transform(num_data)

        num_data = pd.DataFrame(scaled_data, columns=num_data.columns, index=num_data.index)

        final_data = pd.concat([num_data, cat_data], axis=1)

        return final_data


