import datetime, time

today = datetime.datetime.now()

print((round(float(today.microsecond)) * (round(float(today.second)) ** round(float(today.microsecond)))) % 10)

'''
print(today)

print(today.time())
print(today.date())
print(today.weekday()) # 0 Monday 1 Tuesday 2 Wednesday 3 Thursday 4 Friday 5 Saturday 6 Sunday

print(today.hour)
print(today.minute)
print(today.second)
print(today.microsecond)
print(today.day)
print(today.month)
print(today.year)
'''
'''
while True:
    today = datetime.datetime.now()
    time_args = (str(today.time()).split(':'))
    print(f" Clock - {time_args[0]} hours {time_args[1]} minutes {round(float(time_args[2]))} seconds      ", end="\r")
    time.sleep(1)
'''