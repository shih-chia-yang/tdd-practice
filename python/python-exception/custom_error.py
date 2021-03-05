class MyError(Exception):
    pass

#這些參數以tuple形式傳遞給處理程序

try:
    raise MyError("發生未知錯誤","filename.path",3)
except MyError as error:
    message,path_name,num=error.args
    print(f'狀況:{message}; 參數：{path_name} 錯誤代碼：{num}')
