import functools

import pytest
import os
from module.database import *


def remove(func):
    @functools.wraps(func)
    def wrapper(path):
        if os.path.exists(path):
            os.remove(path)
            LOGGER.info("Path '{Path}' already exist. Removing it")

    return wrapper


# @remove("database.db")
def test_create_db_sqlite():
    LOGGER.info('Testing utils')

    database = DataBase(connector="sqlite", dbname="database.db", overwrite=True)
    database.close()
    assert os.path.exists("database.db")
    os.remove("database.db")


def test_create_table():
    database = DataBase(connector="sqlite", dbname="database.db", overwrite=True)
    students = Table("students", database.Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50)),
                     Column('age', Integer),
                     Column('grade', String(15)),
                     extend_existing=True)
    database.create_table(students)
    database.close()
    assert "students" in database.tables_names
    assert students in database.tables
    os.remove("database.db")


def test_insert():
    database = DataBase(connector="sqlite", dbname="database.db", overwrite=True)
    students = Table("students", database.Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50)),
                     Column('age', Integer),
                     Column('grade', String(15)),
                     extend_existing=True)
    database.create_table(students)
    database.insert(students, id=1, name="issa", age=25, grade='master')
    assert "students" in database.tables_names
    assert students in database.tables
    assert len(database.s.query(students).all()) == 1
    database.close()
    os.remove("database.db")


def test_drp_table():
    database = DataBase(connector="sqlite", dbname="database.db", overwrite=True)
    students = Table("students", database.Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(50)),
                     Column('age', Integer),
                     Column('grade', String(15)),
                     extend_existing=True)
    database.create_table(students)
    database.drop_table(students)

    assert "students" not in database.tables_names
    assert students not in database.tables
    database.close()
    os.remove("database.db")