
#EAFP example --> Easier to Ask Forgiveness than permission
#先做了出錯再處理
#python更傾向於錯誤發生之後再來處理，看起來危險
#但如果例外機制得當，程式碼就不會那麼繁瑣，棒易於閱讀
#只有出現錯誤時才需要針對錯誤來處理

def call_vale(string):
    try:
        return float(string)
    except ValueError:
        if string=="":
            return 0
        else:
            return None
