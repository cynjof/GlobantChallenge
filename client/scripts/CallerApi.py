import requests
import logging

API_JOBS = "http://127.0.0.1:5000/jobs"
API_DEPARTMENTS = "http://127.0.0.1:5000/departments"
API_EMPLOYEES = "http://127.0.0.1:5000/hired_employees"


class CallerApi:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def create_departments(self, data_generator):
        """
        Call the API
        :param data_json: dict
        """
        for data in data_generator:
            print(data)
            response = requests.post(url=API_DEPARTMENTS, json=data)
        return

    def create_jobs(self, data_generator):
        """
        Call the API
        :param data_json: dict
        """
        for data in data_generator:
            response = requests.post(url=API_JOBS, json=data)
        return

    def create_hired_employees(self, data_generator):
        """
        Call the API
        :param data_json: dict
        """
        for data in data_generator:
            response = requests.post(url=API_EMPLOYEES, json=data)
        return
