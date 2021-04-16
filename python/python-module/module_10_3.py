# import 敘述的三種形式
#1.匯入後即可使用，但並須以 模組名稱.物件名稱存取
import sys
#2.選擇特定模組
from sys import stdin,stdout
#3. 匯入並同時更改名稱
from sys import stdin as teststdin
#4 匯入模組所有名稱
# 如果2個模組定義了同一個名稱，並且都以import *方式匯入，則會出現名稱衝突
#此時第二個模組將取代第一個模組名稱
from sys import *
