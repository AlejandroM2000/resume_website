import os

from flask import Flask, render_template
import psycopg2 
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__, instance_relative_config=True,template_folder='templates/html')

# def get_db_connection():
#     conn = psycopg2.connect(host='localhost',
#                             port=os.getenv('DB_PORT'),
#                             database=os.getenv('DB_NAME'),
#                             user=os.getenv('DB_USER'),
#                             password=os.getenv('DB_PASSWORD'))
#     return conn


# @app.route('/')
# def index():
#     conn = get_db_connection()
#     cur = conn.cursor()
#     cur.execute('SELECT * FROM users;')
#     users = cur.fetchall()
#     cur.close()
#     conn.close()
#     return render_template('index.html', users=users)



db = SQLAlchemy()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes
        db.create_all()  # Create sql tables for our data models

        return app