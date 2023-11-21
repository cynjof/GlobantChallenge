import requests
import logging

API_JOBS = "http://192.168.1.5:5000/jobs"
API_DEPARTMENTS = "http://192.168.1.5:5000/departments"
API_EMPLOYEES = "http://192.168.1.5:5000/hired_employees"


class CallerApi:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

    def create_departments(self, data_json):
        for data in data_json:
            response = requests.post(url=API_DEPARTMENTS, json=data)
        return

    def create_jobs(self, data_json):
        for data in data_json:
            response = requests.post(url=API_JOBS, json=data)
        return

    def create_hired_employees(self, data_json):
        for data in data_json:
            print(data)
            response = requests.post(url=API_EMPLOYEES, json=data)
        return
