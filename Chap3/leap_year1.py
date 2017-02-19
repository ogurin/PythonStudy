import calendar

year = int(input("年を入力してください：　"))

if calendar.isleap(year):
    print("うるう年です")
else:
    print("うるう年でない")

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("うるうどしです")
else:
    print("うるうどしでないです")