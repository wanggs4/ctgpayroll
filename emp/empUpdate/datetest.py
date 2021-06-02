import datetime
from chinese_calendar import is_workday

def datetest():
    date = datetime.datetime.now().date()
    #date = datetime.datetime (2020, 8, 9)
    if is_workday(date):
        print("工作日")
    else:
        print("非工作日")


datetest()
