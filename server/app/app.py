from flask import Flask
from extensions import db
from routes import main

DATABASE_URI = "mysql+mysqlconnector://globant_migration_process:D5pbjbvuths@migration_db:3306/globant_db"


def create_app(database_uri=DATABASE_URI):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    db.init_app(app)

    return app



if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
