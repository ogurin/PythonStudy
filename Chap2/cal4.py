from calendar import  TextCalendar

year = int(input("年を入力してください：　"))
month = int(input("月を入力してください：　"))

cal = TextCalendar(6)
cal.prmonth(year, month)

cal_str = cal.formatmonth(year, month)
print(cal_str)