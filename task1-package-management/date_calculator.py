import datetime
def defference_days__between_dates(date1,date2):
  """ 
     Function to culculate the number of days between two dates
     we have parameters:
     date1(str): the first date in "YYYY-MM-DD"format.
     date2(str): the second date in "YYYY-MM-DD" format.
     
     Returns:
     int: the number of daye betweeen two entered dates.
     """
  try:
    # fistr convert string dates to datetime objects.
    date1=datetime.datetime.strptime(date1,"%Y-%m-%d")
    date2=datetime.datetime.strptime(date2,"%Y-%m-%d")
    # Calculate differnce of days
    defference_days= abs((date2-date1).days)
    return defference_days
  except ValueError:
    print(f"Error: prints enter the date in this format 'YYYY-MM-DD'.")
    return None
date1=input("enter first date:")
date2= input("enter second date:")
number_days = defference_days__between_dates(date1,date2)
print(f"the difference between two entered dates is {number_days} days")
