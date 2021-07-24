print('Введіть дату в форматі: ХХ.ХХ.XXXX:\n')
day, month, year = map(int, input().split('.'))
a = ((14 - month) / 12)
y = year - int(a)
m = month + 12*int(a) - 2
day_number = (day + int(y) + int(y/4) - int(y/100) + int(y/400) + int((31*m) /12)) % 7
if day_number == 0:
    day_name = "Sunday"
elif day_number == 1:
    day_name = "Monday"
elif day_number == 2:
    day_name = "Tuesday"
elif day_number == 3:
    day_name = "Wednesday"
elif day_number == 4:
    day_name = "Thursday"
elif day_number == 5:
    day_name = "Friday"
elif day_number == 6:
    day_name = "Saturday"

print(day_name)
