import sys
sys.path.append('../../python')
from main_module import create_divider

create_divider("how much calorie eats today? print summary",1)

print("Today's date?")
current_date=input()

print("Breakfast calories?")
breakfast_cal=int(input())

print("Lunch calories?")
lunch_cal=int(input())

print("Dinner calories?")
dinner_cal=int(input())

print("Snack calories")
snack_cal=int(input())

cal_sum=breakfast_cal+lunch_cal+dinner_cal+snack_cal
print("Calorie contetn for "+current_date+":"+str(cal_sum))