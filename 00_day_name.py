print('Введіть дату в форматі: ХХ.ХХ.XXXX:\n')
day, month, year = map(int, input().split('.'))
a = ((14 - month) / 12)
y = year - int(a)
m = month + 12*int(a) - 2
day_num = (day + int(y) + int(y/4) - int(y/100) + int(y/400) + int((31*m) /12)) % 7
if day_num == 0:
    day_name = "Sunday"
elif day_num == 1:
    day_name = "Monday"
elif day_num == 2:
    day_name = "Tuesday"
elif day_num == 3:
    day_name = "Wednesday"
elif day_num == 4:
    day_name = "Thursday"
elif day_num == 5:
    day_name = "Friday"
elif day_num == 6:
    day_name = "Saturday"

print(day_name)
