- [函式庫參考文件](docs.python.org/zh-tw/3/library/index.html)


- 資料處理模組

|模組|功能與使用時機|
|--|--|
|string|存取字串常數的定義，例如string.whitespace定義了python視為空白的字元|
|re|使用正規表達搜尋與替文字|
|struct|以結構化資料讀寫二進位檔案|
|difflib|比對2個文字檔的差異處，建立patch檔或diff檔|
|textwrap|透過分隔線或空格來格式化文字段落|

- 資料型別模組

|模組|功能與使用時機|
|--|--|
|datetime,calendar|日期與時間|
|collections|容器型別|
|enum|列舉型別|
|array|高效率的數值類型陣列|
|sched|事件排程器|
|queue|同步佇列類別|
|copy|淺層與深層拷貝|
|pprint|資料美化列印|
|typing|為變數、函式參數和傳回值加上型別宣告的提示|

- 數值與數學模組

|模組|功能與使用時機|
|--|--|
|numbers|抽象化的數值base class|
|math,cmath|實數與複數運算的數學函式|
|decimal|精準的十進制浮點數|
|statistics|統計相關的函式|
|fractions|有理數運算|
|random|產生隨機亂機|
|itertools|用來建立類似range()的多種產生器|
|functools|提供多種可將函式作為參數的函式|
|operator|提供一組與標準算符功能類似的函式|

- 檔案、路徑、與資料庫

|模組|功能與使用時機|
|--|--|
|os.path|處理相對路徑與絕對路徑名稱|
|pathlib|以物件導向的方式處理路徑名稱|
|fileinput|用來逐行處理多個檔案的內容|
|filecmp|比對檔案和目錄|
|tempfile|產生暫存檔案和目錄|
|glob,fnmatch|用萬用字元匹配目錄與檔案名稱|
|linecache|以行為單位隨機存取文字檔內容|
|shutil|進階的檔案系統操作|
|pickle,shelve|將python物件轉換為資料結構寫入檔案|
|sqlite3|使用sqlite資料庫|
|zlib,gzip,bz2,zipfile,tarfile|檔案壓縮|
|csv|讀寫csv檔|
|configparser|讀寫windows系統常用的ini設定檔|

- 存取作業系統服務

|模組|功能與使用時機|
|--|--|
|os|與作業系統相關的函式|
|io|處理各種不同類別i/o的工具|
|time|時間存取和轉換|
|optparse|解析命令列參數選項|
|logging|python的日誌檔記錄工具|
|getpass|讓使用者輸入密碼|
|curses|終端機的特殊字元處理與顯示|
|platform|存取底層的作業系統與硬體識別資料|
|ctypes|載入c語言所寫的函式庫|
|select|等待i/o讀寫操作完成|
|threading|多執行緒|
|multiprocessing|多行程|
|subprocess|呼叫外部程式並取得執行結果|

- 網路伺服器與客戶端功能

|模組|功能與使用時機|
|--|--|
| socket,ssl|網路客戶端、ssl加密包裝器|
|email|電子郵件和mime處理|
|json|json編碼器和解碼器|
|mailbox|處理各種格式的電子郵件信箱檔案|
|mimetypes|檔案名稱與mime類型的對應表|
|base64,binhex,binascii,quopri,uu|使用各種編碼對檔案或網路串流進行編碼/解碼|
|html.parser,html.entities|解析html和xhtml|
|xml.parsers.expat,xml.dom,xml.sax,xml.etree.ElementTree|各種xml解析器和工具|
|cgi,cgitb|http伺服器執行外部程式的閘道介面|
|wsgiref|http伺服器執行外部python程式的閘道介面|
|urllib.request,urllib.parse|連線url，取得並解析伺服器回應的資料|
|ftplib,poplib,imaplib,nntplob,smtplib,telnetlib|各種網際網路協定的客戶端工具|
|socketserver|網路伺服器|
|http.server|http伺服器|
|xmlrpc.client,xmlrpc.server|xml-rpc客戶端和伺服器|

- 開發和除錯工具

|模組|功能與使用時機|
|--|--|
|pydoc|將docstring彙整成純文字文件或html文件|
|doctest|依照docstring裡面的測試準則(test case)進行測試|
|unittest|單元測試(unit testing)框架|
|test.support|用於測試的公用程式|
|pdb|python 除錯器|
|profile,cProfile|python執行分析器，用來統計程式各個部份的執行次數和執行時間|
|timeit|測試小片段程式碼的執行時間|
|trace|追蹤或回溯那一個python敘述發生錯誤或異常|
|sys|與python解譯器相關的參數和功能|
|atexit|用來定python解釋器終止時會自動執行的程式|
|`__future__`|內含較新版本才有的新功能定義，可讓您在較舊版本的python中使用新版python才有的功能|
|gc|垃圾(不再使用的物件)收集器的操作介面|
|inspect|取得記憶體中現有物件的即時資訊|
|imp|存取已匯入模組的內部資訊|
|zipimport|從zip壓縮檔匯入模組|
|modulefinder|尋找python程式檔所使用的所有模組|