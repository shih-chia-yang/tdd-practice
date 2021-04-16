module 是一個包含python程式碼的檔案
通常module定義了一組相關的python 函式、變數或類別，而module name =file name

package是一個包含python程式的目錄(資料夾)。
通常套件中包含一組相關的程式檔案(module)
package name=root directory name


package中所有的目錄中都包含一個名為__init__.py檔，此檔案有2個用途：
1. python要求目錄中必須包含__init__.py檔，才能將這個目錄識別為套件的目錄。這個要求可防止其他不屬於套件的python程式碼目錄被意外匯入
2. 第一次匯入套件時，python會自動執行__init__.py檔，所有您可以將套件複始化的程式碼放在__init__.py檔

- 如果套件不需要初始化的動作，那麼您不需要在__init__.py檔放入任何內容，只需要一個空的__init__.py檔 


- __all__定義import *要匯入的名稱

- 套件不應使用太多層的目錄結構，除了非常龐大的程式碼之外，一般情況沒有必要這樣做，對於大多數套件，只需一個最上層的目錄即可，稍微複雜的狀況，兩層式的套件架構應該足以有效地處理，如tim peters的[the zen of python]提到的[flat is better than nested]（平舖勝於嵌套)
- 雖然可以特意__all__屬性不列出某些名稱，以便讓from . import *不會匯入，但這將導致名稱不一致的問題，如要隱藏名稱，使用_開頭來命名，將它們設為私有名稱