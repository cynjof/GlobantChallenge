from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    'SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://globant_migration_process:D5pbjbvuths@migration_db:3306/globant_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


class Departments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(255), nullable=False)


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(255), nullable=False)


class HiredEmployees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)


@app.route('/departments', methods=['POST'])
def add_department():
    if request.method == 'POST':
        departments_list = request.get_json()
        for dep in departments_list:
            print(dep)
            department_row = Departments(id=dep["id"],
                                        department=dep["department"])

            db.session.add(department_row)
        db.session.commit()
        return "TODO OK", 201
    else:
        print("There is an error")


@app.route('/jobs', methods=['POST'])
def add_jobs():
    if request.method == 'POST':
        jobs_list = request.get_json()
        for job in jobs_list:
            job_row = Jobs(id=job["id"],
                           job=job['job'])
            db.session.add(job_row)
        db.session.commit()
        return "TODO OK", 201
    else:
        print("There is an error")


@app.route('/hired_employees', methods=['POST'])
def add_hired_employees():
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
        return "TODO OK", 201
    else:
        print("There is an error")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
