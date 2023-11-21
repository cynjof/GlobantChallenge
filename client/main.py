import argparse

import numpy as np

from scripts.CallerApi import CallerApi
from scripts.TranformerData import TransformerData
from scripts.LoaderData import LoaderData

BATCH_SIZE = 1000


class ClientDBMigration:
    def get_config_params(self):
        parser = argparse.ArgumentParser(description='Migration DB')
        parser.add_argument('--path_file', dest='path_file', default=None)
        parser.add_argument('--endpoint', dest='endpoint')
        return parser

    def generete_batch(self, data_df):
        for start in range(0, len(data_df), BATCH_SIZE):
            end = min(len(data_df), start + BATCH_SIZE)
            chunk_df = data_df[start:end]
            yield chunk_df

    def call_client(self):
        # Get params
        parser = ClientDBMigration().get_config_params().parse_args()
        print(f"The path file to ingest: {parser.path_file}")
        data_df = LoaderData().read_data_csv(parser.path_file, parser.endpoint)

        # Clean dataframe
        cleaned_df = TransformerData().drop_index(data_df)
        cleaned_df = cleaned_df.replace({np.nan: None})

        # Parse dataframe to dict
        data_list_dict = TransformerData().parse_data_to_dict(cleaned_df)

        # Check amount of records
        if len(data_list_dict) > 1000:
            chunk_df = self.generete_batch(data_list_dict)
        else:
            chunk_df = data_list_dict

        # Redirection to the correct endpoint and call api
        if parser.endpoint == "departments":
            CallerApi().create_departments(chunk_df)
        elif parser.endpoint == "jobs":
            CallerApi().create_jobs(chunk_df)
        elif parser.endpoint == "hired_employees":
            CallerApi().create_hired_employees(chunk_df)
        else:
            print("Expected str endpoint argument. Please check the command")


if __name__ == '__main__':
    ClientDBMigration().call_client()
