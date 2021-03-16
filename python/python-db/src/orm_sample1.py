from requests import Session
from sqlalchemy import create_engine,select,MetaData,Table,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbpath='example.db'
engine=create_engine('sqlite:///%s' % dbpath)
metadata=MetaData(engine)
people=Table('people',metadata,
                        Column('id',Integer,primary_key=True),
                        Column('name',String),
                        Column('count',Integer),
                        )
Session=sessionmaker(bind=engine)
session=Session()
metadata.create_all(engine)

people_insert=people.insert().values(name='test',count=2)
print(str(people_insert))
session.execute(people_insert)
session.commit()

session.execute(people_insert,[{'name':'jill','count':15},{'name':'joe','count':10}])
session.commit()
result=session.execute(select([people]))
for row in result:
    print(row)

# c 表示 name 是people資料表中的欄位(column)
result1 =session.execute(select([people]).where(people.c.name=='jill'))
for row in result1:
    print(row)

result2=session.execute(people.update().values(count=20)
                                        .where(people.c.name=='jill'))
session.commit()
result3 =session.execute(select([people]).where(people.c.name=='jill'))
for row in result3:
    print(row)

#將資料庫對映到類別
base =declarative_base()
class People(base):
    __tablename__="people"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    count=Column(Integer)

results =session.query(People).filter_by(name='jill')
for person in results:
    print(person.id,person.name,person.count)

#新增資料時，用類別建立個新的資料物件，加到session物件
new_person=People(name='jane',count=5)
session.add(new_person)
session.commit()

results =session.query(People).all()
for person in results:
    print(person.id,person.name,person.count)

#更新
jill=session.query(People).filter_by(name='jill').first()
print(jill.name,jill.count)
jill.count=22
session.add(jill)
session.commit()
results=session.query(People).all()
for person in results:
    print(person.id,person.name,person.count)

#刪除
jane=session.query(People).filter_by(name='jane').first()
session.delete(jane)
session.commit()
jane=session.query(People).filter_by(name='jane').first()
print(jane)