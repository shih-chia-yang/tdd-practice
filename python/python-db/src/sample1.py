import sqlite3

#參數代換：可以使用?佔位等踸，取得後面參數tuple依序取值代入 
#適合動態產生sql敘述，比較安全
# 使用:變數名稱,將變數當做鍵值，後dict中取值代入
def create_table(table_name,syntax):
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    result=cursor.execute("select name from sqlite_master where type='table' and name='{0}'".format(table_name))
    print(result.fetchall())
    if result.fetchall().count ==0:
        cursor.execute(syntax)
    else:
        cursor.execute("""insert into people (name,count) values('Bob',1)""")
    con.commit()
    con.close()

# fetchall()會一次取得select查詢到的所有資料
# fetechone()只會取得一筆紀錄
# fetchmany()取得n筆資料
def select_datas(table_name,filter=None,count=0):
    con = sqlite3.connect('example.db')
    cursor = con.cursor()
    searchSql=f'select * from {table_name}'
    if bool(filter) is True:
        searchSql+=f' where {filter}'
    result=cursor.execute(searchSql)
    if count != 0:
        datas=result.fetchmany(count)
    else:
        datas=result.fetchall()
    return datas

def main():
    create_sytax="""create table people (
                         id integer primary key,
                         name text,
                         count integer)"""
    create_table("people",create_sytax)
    
    print(select_datas("people"))
    print(select_datas("people", " name like 'bob' "))

if __name__=="__main__":
    main()