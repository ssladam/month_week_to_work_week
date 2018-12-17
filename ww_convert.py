#Working with a retailer database, they returned dates into month-named-week values. I needed to convert these into
#  something more usable & easier to sort. The following code shows how to convert into WW format.

#This code assumes your column headers are text strings as outlined below:
col = '2017 Apr WK 1'
col = '2017 Mar WK 4'
col = '2017 Mar WK 5'

from datetime import datetime, timedelta

def convertToWorkWeek(x):
    weekdict = {}
    for col in x:
        date_week = datetime.strptime(col, '%Y %b WK %d')
        week_no = (date_week.day - 1)
        startdate=0
        #What is the actual first day in the month?
        for i in range(1,8):
            d = datetime(date_week.year, date_week.month, i)
            #mod the day by 7, since Target considers Sunday the start of the week
            #  python calls monday day 1, and sunday 7. mod(7) keeps other days
            #  as 1..6, but now Sunday is 0
            if d.day - (d.isoweekday()%7) > 0:
                startdate=d
                break
    
        #if the month doesn't start on a sunday, we need to shift BACK by one week
        if(datetime(date_week.year, date_week.month, 1).weekday() != 6 and startdate.day >= 2):
            startdate = startdate - timedelta(days=7)
    
        date_week = startdate + timedelta(days=7*week_no) #now equals date of first full week in month
        workweek = str(date_week.isocalendar()[0]) + "WW" + str("{0:0>2}".format(date_week.isocalendar()[1]))
        weekdict[col] = workweek
    del col, date_week, week_no, startdate, i, d, workweek
    return weekdict
