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