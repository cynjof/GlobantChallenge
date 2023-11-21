import pandas as pd
import pytest
from scrpits.LoaderData import LoaderData


class TestYourClass:
    @classmethod
    def setup_class(cls):
        # Initialize an instance of of the class
        cls.data = LoaderData('/home/cynthia/PycharmProjects/GlobantChallenge/sources/departments.csv')

    def test_ingest_data_successful(self):
        # Call the read_data_csv method
        result = self.data.read_data_csv()

        # Assert that the result is a DataFrame
        assert isinstance(result, pd.DataFrame)

    def test_ingest_data_file_not_found(self):
        # Set the path to a non-existent file
        self.data.path_file = '/home/cynthia/PycharmProjects/GlobantChallenge/departments.csv'

        # Call the read_data_csv method and expect it to fail
        with pytest.raises(FileNotFoundError):
            self.data.read_data_csv()

