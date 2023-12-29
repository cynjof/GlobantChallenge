import requests
import responses


class TestApp:
    @responses.activate
    def test_departments(self, client, get_departments):
        responses.add(
            responses.POST,
            "/departments",
            json=get_departments,
            status=200
        )

        response = client.post("/departments", json=get_departments)
        assert response.status_code == 200

    @responses.activate
    def test_jobs(self, client, get_jobs):
        responses.add(
            responses.POST,
            "/jobs",
            json=get_jobs,
            status=200
        )
        response = client.post("/jobs", json=get_jobs)
        assert response.status_code == 200

    @responses.activate
    def test_hired_employees(slef, client, get_employees):
        responses.add(
            responses.POST,
            "/hired_employees",
            json=get_employees,
            status=200
        )
        response = client.post("/hired_employees", json=get_employees)
        assert response.status_code == 200
