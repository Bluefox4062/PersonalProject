#import calendar

#print(calendar.__file__)

from calendar import month, isleap

print(month(2022, 9 ))

print(isleap(2025))     # 判斷是否為閏年