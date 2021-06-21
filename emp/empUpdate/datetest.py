import datetime
import MySQLdb
from chinese_calendar import is_workday

def datetest():
    date = datetime.datetime.now().date()
    #date1 = datetime.datetime (2020, 8, 9)
    # date = datetime.datetime.now().weekday() +1
    print(date)
    if is_workday(date):
        print(str(date)+"工作日")
    else:
        print(str(date)+"非工作日")
    # if date == 4:
    #     print("今天星期四")
    # else:
    #     print("今天不是星期四")

def mytest():
    sql = ("CALL emp_update_dept();")
    sql2 =("CALL emp_update_dept_h();")
    print(sql)
    if sql == "":
        print("111111")
        if sql2 =="":
            print("333333")
        else:
            print("44444")
    else:
        print("22222")


datetest()
