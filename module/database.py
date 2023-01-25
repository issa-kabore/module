from module import LOGGER

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database


def get_connector(kind: str):
    if kind not in ["mysql", "sqlite"]:
        raise ValueError(f"Unknown connector '{kind}'. Only 'mysql' or 'sqlite'")
    elif kind == "mysql":
        return f"mysql+mysqlconnector://"
    elif kind == "sqlite":
        return f"sqlite:///"


Base = declarative_base()


class DataBase(object):
    def __init__(self, connector="mysql", dbname="dbaname", user="root", password="password", host="localhost",
                 port=3306, overwrite=False):
        self.Base = Base
        self.name = dbname
        self.url = get_connector(
            connector) + f"{user}:{password}@{host}:{port}/{dbname}" if connector == "mysql" else get_connector(
            connector) + f"{dbname}"

        self.engine = self.connect()
        if not database_exists(self.url):
            create_database(self.url)
            LOGGER.info(f"Database {self} created.")
        else:
            LOGGER.info(f"Database {self} already exist.")
            if overwrite:
                create_database(self.url)
                LOGGER.info(f"Database {self} overwrited.")

        self.session = sessionmaker()
        self.session.configure(bind=self.engine)
        self.s = self.session()

        self.tables = list()
        self.tables_names = list()
        self.nb_tables = len(self.tables)
        # self.Base.metadata.create_all(self.engine)

    def connect(self):
        try:
            engine = create_engine(self.url)
            LOGGER.info(f"Connected to the {self.url}.")
            return engine
        except Exception as ex:
            raise ValueError("Connection Failed due to the following error: \n", ex)

    def commit(self):
        self.s.commit()

    def close(self):
        self.s.close()
        LOGGER.info(f"Connexion closed.")

    def __repr__(self):
        return f"DataBase(name={self.name!r})"

    def create_table(self, table):
        if table.name not in self.tables_names:
            self.tables.append(table)
            self.tables_names.append(table.name)
            self.Base.metadata.create_all(self.engine, [table])
            self.nb_tables += 1
            LOGGER.info(f"Table '{table.name}' created.")
        else:
            LOGGER.info(f"Table '{table.name}' already exist.")

    def drop_table(self, table):
        if table.name in self.tables_names:
            self.Base.metadata.drop_all(self.engine, [table], checkfirst=True)
            self.nb_tables -= 1
            self.tables.remove(table)
            self.tables_names.remove(table.name)
            LOGGER.info(f"Table '{table.name}' deleted.")
        else:
            LOGGER.info(f"Table '{table.name}' not found.")
            # raise error

    def insert(self, table, **record):
        if table not in self.tables:
            raise ValueError(f"Table '{table}' not found in {self}")

        try:
            statement = table.insert().values(**record)
            r = self.engine.execute(statement)
            LOGGER.info(f"Record inserted into '{table.name}'.")

        except Exception as ex:
            raise ValueError("Insertion Failed due to the following error: \n", ex)
        #
        # self.s.add(record)
        # self.commit()

    def show_tables(self):
        # return self.Base.metadata.tables.keys()
        return self.engine.table_names()

    def get_tables(self):
        self.tables = ""
        return True
