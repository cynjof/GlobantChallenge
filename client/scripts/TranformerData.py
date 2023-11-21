import pandas as pd

class TransformerData:

    def drop_index(self, data_df):
        """
        Drop index of a pandas dataframe
        :param: dataframe
        :return: dataframe
        """
        cleaned_dataframe = data_df.reset_index(drop=True)
        return cleaned_dataframe

    def parse_data_to_dict(self, dataframe):
        """
        Parse pandas dataframe to a list of dict
        :param dataframe
        :return: list
        """
        list_dict = []
        for index, row in dataframe.iterrows():
            row_dict = row.to_dict()
            list_dict.append(row_dict)
        return list_dict
