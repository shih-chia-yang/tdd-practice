class Temprature:
    def __init__(self):
        self._temp_fahr=0
    
    #唯讀
    @property
    def temp(self):
        return (self._temp_fahr-32)*5/9
    
    @temp.setter
    def temp(self,new_temp):
        self._temp_fahr=new_temp*9/5+32


t=Temprature()
print(t._temp_fahr)
print(t.temp)#自動將華氏溫度_tmep_fahr中的0轉換為攝氏

t.temp=34
print(t._temp_fahr)
print(t.temp)