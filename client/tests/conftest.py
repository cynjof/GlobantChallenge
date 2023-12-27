import pytest
import pandas as pd
import requests

def pytest_configure():
    pytest.df_departments = pd.DataFrame({'id': [1, 5, 9], 'department': ['sales', 'account', 'rrhh']})
    pytest.list_dict_departments = [{"id": 1, "department": "sales"},
                                    {"id": 2, "department": "account"},
                                    {"id": 3, "department": "rrhh"}]
    pytest.list_dict_jobs = [{"id": 1, "job": "manager"},
                            {"id": 2, "job": "developer"},
                            {"id": 3, "job": "analyst"}]
    pytest.list_dict_employees = [{"id": 1, "name": "Celeste", "datetime": "2021-11-07T02:48:42Z", "department_id": 2, "job_id": 1},
                                {"id": 2, "name": "Roman", "datetime": "2022-11-07T02:48:42Z", "department_id": 1, "job_id": 3},
                                {"id": 3, "name": "Pedro", "datetime": "2023-11-07T02:48:42Z", "department_id": 2, "job_id": 2}]

@pytest.fixture()
def set_index():
    dataframe_copy1 = pytest.df_departments.copy()
    indexed_dataframe = dataframe_copy1.set_index("id")
    yield indexed_dataframe
    print("\n Fixture set_index done")

@pytest.fixture()
def get_dataframe():
    yield pytest.df_departments.copy()
    print("\n Fixture get_dataframe done")

@pytest.fixture()
def get_departments():
    yield pytest.list_dict_departments.copy()

@pytest.fixture()
def get_jobs():
    yield pytest.list_dict_jobs.copy()

@pytest.fixture()
def get_employees():
    yield pytest.list_dict_employees.copy()

