import datetime

today = datetime.datetime.now()

print(today)
print(today - datetime.timedelta(days = 5))
print(today - datetime.timedelta(days = 1))
print(today + datetime.timedelta(days = 1))
print(datetime.datetime.now().replace(second = 0, microsecond=0))

date1 = datetime.datetime(2021, 4, 3, 3, 34, 43)
date2 = datetime.datetime(2024, 3, 13, 13, 44, 45)
print(date2.timestamp() - date1.timestamp())
