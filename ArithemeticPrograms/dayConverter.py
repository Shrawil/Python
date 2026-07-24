num = int(input("Enter number of days : "))

years = num // 365
days = num % 365

months = days // 30
days = days % 30

weeks = days // 7
days = days % 7

print(f"{years} years {months} months {weeks} weeks {days} days in {num} days.")
