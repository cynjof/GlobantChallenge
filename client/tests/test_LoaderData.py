import pandas as pd
import pytest
from client.scripts.LoaderData import LoaderData


class TestLoaderData:
    @classmethod
    def setup_class(cls):
        # Initialize an instance of the class
        cls.data = LoaderData()

    def test_ingest_data_successful(self):
        # Call the read_data_csv method
        path_file = '/home/cynthia/PycharmProjects/GlobantChallenge/client/sources/departments.csv'
        result = self.data.read_data_csv(path_file, 'departments')

        # Assert that the result is a DataFrame
        assert isinstance(result, pd.DataFrame)

    def test_ingest_data_file_not_found(self):
        # Set the path to a non-existent file
        path_file = '/home/cynthia/PycharmProjects/GlobantChallenge/departments.csv'

        # Call the read_data_csv method and expect it to fail
        with pytest.raises(FileNotFoundError):
            self.data.read_data_csv(path_file, 'departments')

