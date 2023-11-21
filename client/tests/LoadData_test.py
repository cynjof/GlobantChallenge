import pandas as pd
import pytest
from scripts.LoadData import LoadData


class TestYourClass:
    @classmethod
    def setup_class(cls):
        # Initialize an instance of YourClass with the path to a test CSV file
        cls.your_instance = LoadData('/home/cynthia/PycharmProjects/GlobantChallenge/sources/departments.csv')

    def test_ingest_data_successful(self):
        # Call the ingest_data method
        result = self.your_instance.ingest_data()

        # Assert that the result is a DataFrame
        assert isinstance(result, pd.DataFrame)

    def test_ingest_data_file_not_found(self):
        # Set the path to a non-existent file
        self.your_instance.path_file = '/home/cynthia/PycharmProjects/GlobantChallenge/departments.csv'

        # Call the ingest_data method and expect it to raise FileNotFoundError
        with pytest.raises(FileNotFoundError):
            self.your_instance.ingest_data()

