#  Python 3 - Date & Time
#Tick
def tickTask():
    # !/usr/bin/python3
    import time;  # This is required to include time module.

    ticks = time.time()
    print("Number of ticks since 12:00am, January 1, 1970:", ticks)
#TimeTuple
def timeTupleTask():
    import time

    print(time.localtime())
#Getting current time
def getCurrentTime():
    # !/usr/bin/python3
    import time

    localtime = time.localtime(time.time())
    print("Local current time :", localtime)
#Getting formatted time
def getFormatTime():
    # !/usr/bin/python3
    import time

    localtime = time.asctime(time.localtime(time.time()))
    print("Local current time :", localtime)
#Getting calendar for a month
def getCalendarTime():
    import calendar

    cal = calendar.month(2016, 2)
    print("Here is the calendar:")
    print(cal)

# Enoxs TO-DO : The time Module: 1~12 ( add 2
# The time Module:
# Enoxs TO-DO : The calendar Module: ( 1~12
# The calendar Module:


if __name__ == '__main__':
    # tickTask()
    # timeTupleTask()
    # getCurrentTime()
    # getFormatTime()
    getCalendarTime()