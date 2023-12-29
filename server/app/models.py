from extensions import db


class Departments(db.Model):
    """Custom class"""
    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(255), nullable=False)


class Jobs(db.Model):
    """Custom class"""
    id = db.Column(db.Integer, primary_key=True)
    job = db.Column(db.String(255), nullable=False)


class HiredEmployees(db.Model):
    """Custom class"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    datetime = db.Column(db.String(255), nullable=False)
    department_id = db.Column(db.Integer, nullable=False)
    job_id = db.Column(db.Integer, nullable=False)

