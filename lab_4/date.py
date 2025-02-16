# task-1 
import datetime
cur_date = datetime.datetime.now()
after_five_day = cur_date - datetime.timedelta(days=5)
print(after_five_day)


# task-2
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tommorow = today + datetime.timedelta(days=1)

print(yesterday.strftime("%Y-%B-%d"))
print(today.strftime("%Y-%B-%d"))
print(tommorow.strftime("%Y-%B-%d"))


# task-3
import datetime
cur_date = datetime.datetime.now()
print(cur_date.replace(microsecond=0))


# task-4
import datetime
firstdate = datetime.datetime(2025, 2, 12, 0, 0, 25)
seconddate = datetime.datetime(2025, 2, 12, 0, 0, 0)
print(abs(firstdate - seconddate).total_seconds())

