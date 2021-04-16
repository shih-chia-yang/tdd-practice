import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
# 使用keys() method取得資料庫中所有鍵的清單
print(r.keys())
r.set('hello', 'world')
print(r.get('hello'))
r.incr('counter')
print("first time call : ",r.get('counter'))
r.incr('counter')
print("second time call : " ,r.get('counter'))

#將list儲存為redis資料庫中的值
example_list=["one"]
r.rpush("words","one")
r.rpush("words","two")
# lrange 類似python slice功能，可以取出範圍內list中的元素，-1表示list的結尾
#還可以使用lpush()從list左側增加值，也可以使用lindex()以索引來取得一個值
print(r.lrange("words",0,-1))
# 呈現list長度
print(r.llen("words"))
#lpush從左側增加元素
r.lpush("words","zero")
print(r.lrange("words",0,-1))
#使用index取出list中的元素
print(r.lindex("words",1))
#值的保存期限
#redis特別適合用於快取，是因為能夠為鍵值對設定到期時間。
#該時間過後，鍵和值將會自動被刪除
r.setex("timed",10,"10 second") #-->設定10秒後到期
#取得timed 鍵到期前的剩餘時間(以秒為單位)
print(r.ttl("timed"))
#取得timed鍵到期前的剩餘時間(以毫秒為單位)
print(r.pttl("timed"))