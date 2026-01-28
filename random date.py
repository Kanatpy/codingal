import random
import time

def getrandomdate(start_date, end_date):
    print("printing random date between", start_date,"and",end_date)
    random_gen = random.random()
    date_format = "%m/%d/%Y"

    start_time = time.mktime(time.strptime(start_date, date_format))
    end_time = time.mktime(time.strptime(end_date, date_format))

    randtime = start_time + random_gen * (end_time-start_time)
    randdate = time.strftime(date_format, time.localtime(randtime))
    return randdate

#start_time , end_time = eval(input("enter two dates with commas in between")) 

print("random date =",getrandomdate(str("1/1/2016"), str("12/31/2018")) )