import pytest
from client.scripts.TranformerData import TransformerData
import pandas as pd


class TestTransformerData:

    @classmethod
    def setup_method(cls):
        cls.data = TransformerData()

    def test_drop_index(self, set_index):
        test_index = self.data.drop_index(set_index)
        assert test_index.index.name is None

    def test_drop_index_to_fail(self, set_index):
        with pytest.raises(AssertionError):
            assert set_index.index.name is None

    def test_parse_data_to_dict(self, get_dataframe):
        dict_data = self.data.parse_data_to_dict(get_dataframe)
        assert type(dict_data) == list

    def test_parse_data_to_dict_to_fail(self, get_dataframe):
        modified_dataframe = get_dataframe.to_dict()
        with pytest.raises(AttributeError):
            dict_data = self.data.parse_data_to_dict(modified_dataframe)
            assert type(modified_dataframe) != pd.DataFrame

