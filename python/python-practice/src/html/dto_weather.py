from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base=declarative_base()

class Weather(Base):
    __tablename__="weather"
    id=Column('id',Integer,primary_key=True)
    city=Column(String)
    start_time=Column(String)
    end_time=Column(String)
    avg_temp=Column(Float)

def main():
    dbpath='example.db'
    engine=create_engine('sqlite:///%s' % dbpath)
    Base.metadata.create_all(engine)

if  __name__=="__main__":
    main()
