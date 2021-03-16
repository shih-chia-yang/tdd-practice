from requests import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,select,MetaData,Table
from sqlalchemy.ext.declarative import declarative_base
import dto_weather

base=declarative_base()

def db_init():
    dbpath='example.db'
    engine=create_engine('sqlite:///%s' % dbpath)
    # metadata=MetaData(engine)
    Session=sessionmaker(bind=engine)
    weather=dto_weather.Weather()
    session=Session()
    weather.__table__.create(bind=engine,checkfirst=True)
    # base.metadata.create_all(engine)
    return session



def insert(session,table,datas):
    for data in datas:
        city,start_time,end_time,avg_temp=data
        new_weather=table(city=city,start_time=start_time,end_time=end_time,avg_temp=avg_temp)
        session.add(new_weather)

def select(session,table):
    return session.query(table)