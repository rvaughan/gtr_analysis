import json

from sqlalchemy import create_engine, Column, Integer, DateTime
from sqlalchemy import MetaData, Text
from sqlalchemy.dialects.postgresql import JSON, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import CreateSchema


def main():
    # Read in user configs
    with open('config.json') as f:
        conf = json.load(f)

    # Assign to local variables
    user = conf['user']
    host = conf['host']
    port = conf['port']
    passw = conf['passw']
    schema = conf['schema']
    database = conf['database']

    # Base object that remains aware
    # of subclasses
    Base = declarative_base()

    # Table specifications
    class Project(Base):
        """Define the Project object schema"""
        __tablename__ = 'projects'
        __table_args__ = {"schema": schema}
        pkey = Column(Integer, primary_key=True, autoincrement=True)
        abstract_text = Column(Text)
        created = Column(DateTime)
        grant_cat = Column(Text)
        href = Column(Text)
        health_categories = Column(JSONB)
        id = Column(Text)
        identifiers = Column(JSONB)
        lead_org_dpt = Column(Text)
        links = (Column(JSONB))
        potential_impact = Column(Text)
        researchActivities = Column(JSONB)
        research_subjects = Column(JSONB)
        research_topics = Column(JSONB)
        status = Column(Text)
        title = Column(Text)

    # Table specifications
    class Person(Base):
        """Define the Project object schema"""
        __tablename__ = 'persons'
        __table_args__ = {"schema": schema}
        pkey = Column(Integer, primary_key=True, autoincrement=True)
        created = Column(DateTime)
        first_name = Column(Text)
        href = Column(Text)
        id = Column(Text)
        links = Column(JSONB)
        surname = Column(Text)

    # Table specifications
    class Publication(Base):
        """Define the Publication object schema"""
        __tablename__ = 'publications'
        __table_args__ = {"schema": schema}
        pkey = Column(Integer, primary_key=True, autoincrement=True)
        abstract_text = Column(Text)
        created = Column(DateTime)
        href = Column(Text)
        id = Column(Text, primary_key=True)
        links = Column(JSONB)
        title = Column(Text)
        pub_type = Column(Text)
        journal_title = Column(Text)
        doc = Column(JSONB)
        published_date = Column(DateTime)
        url = Column(Text)
        vol = Column(Text)
        doi = Column(Text)
        issue = Column(Text)
        author = Column(Text)

    # Table specifications
    class Organisation(Base):
        """Define the Organisation object schema"""
        __tablename__ = 'organisations'
        __table_args__ = {"schema": schema}
        pkey = Column(Integer, primary_key=True, autoincrement=True)
        addresses = Column(JSONB)
        created = Column(DateTime)
        href = Column(Text)
        id = Column(Text, primary_key=True)
        links = Column(JSONB)
        name = Column(Text)

    class Fund(Base):
        """Define the fund object schema"""
        __tablename__ = 'funds'
        __table_args__ = {"schema": schema}
        pkey = Column(Integer, primary_key=True, autoincrement=True)
        category = Column(Text)
        href = Column(Text)
        links = Column(JSONB)
        value_pounds = Column(Integer)
        start = Column(DateTime)
        end = Column(DateTime)

    # Connection string using config options
    conn_str = 'postgresql:{}//{}:@{}:{}/{}'.format(passw,
                                                    user,
                                                    host,
                                                    port,
                                                    database)

    db = create_engine(conn_str)
    engine = db.connect()

    # Check the table and schema don't already exist
    # If not create them
    # TODO Check for individual tables and create as necessary
    if not engine.dialect.has_table(engine, "projects", schema=schema):
        engine.execute(CreateSchema(conf['schema']))
        Base.metadata.create_all(engine)         # Create a table if

if __name__ == "__main__":
    main()