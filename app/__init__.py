"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaa39e7avj5o488mtig-a.oregon-postgres.render.com",
        database="todo_108f",
        user="todo_108f_user",
        password="LLq4mlTqpYnX6dmyGn5b1YHIPSSDO2Ki")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
