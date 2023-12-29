import logging
from flask import jsonify, request, Blueprint
from extensions import db
from models import Departments, Jobs, HiredEmployees


main = Blueprint("main", __name__, cli_group=None)
logger = logging.getLogger(__name__)


class APIError(Exception):
    pass


@main.before_request
def log_request_info():
    logger.debug('Headers: %s', request.headers)
    logger.debug('Body: %s', request.get_data())


@main.route('/departments', methods=['POST'])
def add_department():
    """Insert data"""
    if request.method == 'POST':
        departments_list = request.get_json()
        for dep in departments_list:
            department_row = Departments(id=dep["id"],
                                        department=dep["department"])

            db.session.add(department_row)
        db.session.commit()
        response = [{'message': 'success'}]
        return jsonify(response), 200
    else:
        raise APIError("Bad Requests", 401)


@main.route('/jobs', methods=['POST'])
def add_jobs():
    """Insert data"""
    if request.method == 'POST':
        jobs_list = request.get_json()
        for job in jobs_list:
            job_row = Jobs(id=job["id"],
                           job=job['job'])
            db.session.add(job_row)
        db.session.commit()
        response = [{'message': 'success'}]
        return jsonify(response), 200
    else:
        raise APIError("Bad Requests", 401)


@main.route('/hired_employees', methods=['POST'])
def add_hired_employees():
    """Insert data"""
    if request.method == 'POST':
        hired_employees_list = request.get_json()
        for employee in hired_employees_list:
            employee_row = HiredEmployees(id=employee["id"],
                                          name=employee["name"],
                                          datetime=employee["datetime"],
                                          department_id=employee["department_id"],
                                          job_id=employee["job_id"])
            db.session.add(employee_row)
        db.session.commit()
        response = [{'message': 'success'}]
        return jsonify(response), 200
    else:
        raise APIError("Bad Requests", 401)
