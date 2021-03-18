import sqlite3

def create_table(table_name,syntax):
    con = sqlite3.connect('weather.db')
    cursor = con.cursor()
    result=cursor.execute("select name from sqlite_master where type='table' and name='temperature'".format(table_name))
    if result.fetchone() is None:
        cursor.execute(syntax)
    con.commit()
    con.close()

def insert(tablename,*datas):
    con = sqlite3.connect('weather.db')
    cursor = con.cursor()
    command="""insert into {0} 
     ( id,city,date,temperature,count)
      values(?,?,?,?,?)""".format(tablename)
    cursor.execute(command,(datas[0],datas[1],datas[2],datas[3],datas[4]))
    con.commit()
    con.close()

def select (table_name):
    con = sqlite3.connect('weather.db')
    cursor = con.cursor()
    result=cursor.execute(f'select * from {table_name}')
    return result.fetchall()