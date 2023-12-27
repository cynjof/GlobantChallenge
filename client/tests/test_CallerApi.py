import requests


class TestCallerApi():

    def test_create_departments(self, get_departments):
        response = requests.post(url="http://127.0.0.1:5000/departments", json=get_departments)
        assert response.status_code == 200

    def test_create_jobs(self, get_jobs):
        response = requests.post(url="http://127.0.0.1:5000/jobs", json=get_jobs)
        assert response.status_code == 200

    def test_create_hired_employees(self, get_employees):
        response = requests.post(url="http://127.0.0.1:5000/hired_employees", json=get_employees)
        assert response.status_code == 200
