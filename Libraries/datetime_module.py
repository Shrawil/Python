import datetime, time

'''
print(today)

print(today.time())
print(today.date())
print(today.weekday())

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