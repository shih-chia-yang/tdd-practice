#try:
#  程式主體
#except LookupError as error:
#   處理LookupError例外
#except IndexError as  error:
#   處理IndexError例外

#當發生IndexError時，會被第一個LookupError補獲，因為IndexError繼承LookupError
#導致第二個except子句永遠不會被用到，這個例外會被歸類在第一個except子句中
#將2個位置對調，第一個子句會處理IndexError例外，第二個子句處理除了IndexError的任何LookupError例外