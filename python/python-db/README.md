# 存取SQLite、Redis、MongoDB

- 使用SQLite3資料庫
    - 因為sqlite3內建於python3標準函式庫，可以在任何有python的機器上使用，不必額外安裝
- sqlite3將其所有紀錄儲存在本機的SQLite資料庫檔案中，因此不需要伺服器，而PostgreSQL、MySQL、其他大型資料庫需要安裝資料庫伺服器提供用戶端連線。
- 詳細請參閱https://docs.python.org/3/library/sqlite3.html

## 防止sql injection 攻擊
採用參數代換的方式，用?佔位等號來放入sql敘述，因為sqlite3函式庫在將外部資料代換?符號之前，會自動將外部資料內的特殊符號與語法轉義讓其失效

- 預設情況sqlite3資料庫的任何異動不會立即儲存到資料庫，必須執行Connection物件的commit() method才會儲存。異動失敗時，可以選擇回復原來的資料，沒有執行commit()就執行close()關閉資料庫連線的話，所有更改都會遺失。應養成習慣在關閉資料庫連線之前執行commit()

|操作|sqlite3|
|--|--|
|建立資料庫連線|conn=sqlite3.connect(filename)|
|建立Cursor物件|cursor=conn.cursor()|
|透過Cursor物件執行查詢|cursor.execute(query)|
|取得查詢結果|cursor.fetchall(),cursor.fetchmany(n),cursor.fetchone() for row in cursor:|
|儲存資料庫異動|conn.commit()|
|關閉連結| conn.close()|

## [[orm]]

## 使用Alembic追蹤資料庫版本

```bash
pip3 install alembic
```

## noSQL 
- Redis儲存Key-Value資料庫, Redis官方網站推薦方法是redis-py

```bash
pip3 install redis
```

- 執行Redis伺服器

1. 使用docker容器是啟動和執行Redis伺服器的最快速、最簡單的方式

```bash
docker run -p 6379:6379 redis
```

2. linux系統，請使用yum或apt系統套件管理程式

3. [redis相關文件](https://redislabs.com)、[redis-py](https://redis-py.readthedocs.io)


- mongo儲存文件資料庫
MongoDB的文件是以BSON(二連制json)的格式儲存，因此文件看起來像json物件或python字典, 一個使用者帳號在MongoDB中是這樣儲存的
```json
{
    username:'flag',
    password:'123',
    age:'35',
    eamil:'xxx@flag.com.tw',
    address:'xxx',
}
```
MongoDB使用主從式的叢集架構，只要新增多個節點就可以擴展儲存空間與處理能力，所以具有同時處理數十億個文件的速度。
MongoDB很適合用於需要經常擴展、散佈大量資料，而且資料欄位複雜、不固定的場合，不過除了這種狀況之外、通常不建議採用MongoDB

- 使用docker容器
```bash
docker run -p 27017:27017 mongo
```

- 安裝pymongo函式庫
```bash
pip3 install pymongo
```

1. 除了insert_one(),find_one(),update_one(),replace_one(),delete_one()，同一個命令可涵蓋處理多筆資料，如find_many()和update_many()。
2. MongoDB還支援索引以提高效能，並且有多種方法可以對資料進行分組、計數、聚合，還有內建的mapreduce()方法可以使用。
3. 詳細使用方式、請參見pyMongo[線上文件](https://api.mongodb.com/python/current/) 


- 重點整理

|資料庫種類|適用套件|套件類型|
|--|--|--|
|SQLite資料庫| sqlite3|內建|
|以ORM存取多種關連式資料庫|SQLAlchemy|第三方|
|搭配ORM追蹤關連式資料庫的版本|Alembic|第三方|
|Redis資料庫|redis|第三方|
|MongoDB資料庫|pymongo|第三方|