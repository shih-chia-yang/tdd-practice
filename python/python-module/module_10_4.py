#模組搜尋路徑
#path變數定義python去那些資料夾尋找模組
import sys
print(sys.path)

#自己定義的模組要放那裡
#需具備3個條件
#1. 將模組放在sys.path變數所設定的目錄中
#最簡單，但也是最不應該選擇的選項，因為sys.path變數隨著作業系統、python版本不同
#2. 將所有模組放在與主程式相同的目錄中
#3. 建立一個或多個目錄來儲存模組，並修改sys.path變數，使其包含模組所在的目錄 
#適用多個程式會使用到同一個模組
# 1.在python程式碼中修改sys.path變數，加入模組的路徑，但缺點是路徑寫死在程式中
#，更改時必須每個程式都修改
#2.設定PYTHONPATH環境變數，但不是所有電腦的使用者都能修改環境變數
#3.將模組所在目錄放在一個副檔名為.pth的任意檔案中，python會自動讀取.pth檔，將裡面
#的目錄加入成為預設的搜尋路徑
#設置PYTHONPATHSISP環境變數，請參閱python文件中安裝和使用的部份
#(docs.python.org/3/using/cmdine.html)
# .pth檔比較安全，將.pth移動到新版資料夾，或是重建.pth檔，想了解有關使用.pth檔，請參閱
#(docs.python.org/3/library/site.html)
