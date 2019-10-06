"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    def dec_month(month):
        if month == 12:
            return 1
        else:
            return month
    def dec_year (year, month):
        if month == 12:
            return next_year + 1
        else:
             return year
    
    if  month < 1 or month > 12:
        print ( month )
    elif year < 1 or year > 12:
        print (year)
    else:
        date1 = (datetime.date( dec_year(year, month), dec_month(month), 1))
        print(date1)
        
print(days_in_month(1982, 1)        

def is_valid_date(year, month, day):
       if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<=12 and 1<=day<= days_in_month(year, month):
           return True
      else:
           return False
      
  
   
print(is_valid_date(1982,9,11)

def days_between(year1, month1, day1, year2, month2, day2):
        date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2)and (date1<date2):
        difference=date2-date1
        print(difference.days)
        return difference.days

    else:        
        return 0 
   


def age_in_days(year, month, day):
       todays_date=datetime.date.today()
    if is_valid_date(year, month,day) and (age_in_days<todays_date):
        return days_between(age_in_days(year,month,day),todays_date(year,month,day))
    else:
        return 0
  

