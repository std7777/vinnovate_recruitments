import sqlite3
from config import DATABASE

def get_db():
    return sqlite3.connect(DATABASE)
