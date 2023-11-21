
import pandas as pd
import csv

class LoaderData:

    def read_data_csv(self, path_file: str, endpoint: str):

        print(f"It will be loaded the data from {path_file}")
        if endpoint == "departments":
            dataframe_data = pd.read_csv(path_file, names=["id", "department"])
            print("Data loaded successfully")
            return dataframe_data
        elif endpoint == "jobs":
            dataframe_data = pd.read_csv(path_file, names=["id", "job"])
            print("Data loaded successfully")
            return dataframe_data
        elif endpoint == "hired_employees":
            dataframe_data = pd.read_csv(path_file, names=["id", "name", "datetime", "department_id", "job_id"])
            print("Data loaded successfully")
            return dataframe_data
        else:
            print("There is an Error")


