# Importing necessary library.
from datetime import datetime


# Function which gets the current time.
# This is important for the entire program to run correctly as this program is time dependant.
# This converts the time recieved into appropriate string format just like that in the zoom messages, so that this generated 
# string can later be compared to the time strings extracted from messages.
def get_current_time():
    now = datetime.now()
    hrs = now.strftime("%H")
    mins = now.strftime("%M")
    hrs = int(hrs)
    Time = None
    if hrs > 12:
        hrs = hrs-12
        hrs = str(hrs)
        if int(hrs) >9:
            Time = hrs+":"+mins+" PM"
        else:
            Time = "0"+hrs+":"+mins+" PM"
    elif hrs > 9 and hrs <=11:
        hrs = str(hrs)
        Time = hrs+":"+mins+" AM"
    elif hrs == 12:
        hrs = str(hrs)
        Time = hrs+":"+mins+" PM"
    else:
        hrs= str(hrs)
        Time = "0"+hrs+":"+mins+" AM"
    if Time == f"00:{mins} AM":
        Time = f"12:{mins} AM"
    return Time


# Function which gets the current year, month, day and also time all together, just in the format followed by zoom meeting's 
# details messages.
# Converts the month to the months 3 letter abbrevation, and time similar to the pattern in Zoom Meeting's details messages.
# Returns a complete concatenated string "schedule" of Month, Day, Year, and Time in similar fashion as that in the Zoom Meeting's 
# details messages.
def get_current_datetime():
    now = datetime.now()


    month = now.month
    month = int(month)
    if month == 1:
        month = "Jan"
    elif month == 2:
        month = "Feb"
    elif month == 3:
        month = "Mar"
    elif month == 4:
        month = "Apr"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "Jun"
    elif month == 7:
        month = "Jul"
    elif month == 8:
        month = "Aug"
    elif month == 9:
        month = "Sep"
    elif month == 10:
        month = "Oct"
    elif month == 11:
        month = "Nov"
    elif month == 12:
        month = "Dec"


    day = now.day
    day = str(day)
    day += ","


    year = now.year
    year = str(year)


    hrs = now.strftime("%H")
    mins = now.strftime("%M")
    hrs = int(hrs)
    Time = None
    if hrs > 12:
        hrs = hrs-12
        hrs = str(hrs)
        if int(hrs) >9:
            Time = hrs+":"+mins+" PM"
        else:
            Time = "0"+hrs+":"+mins+" PM"
    elif hrs > 9 and hrs <=11:
        hrs = str(hrs)
        Time = hrs+":"+mins+" AM"
    elif hrs == 12:
        hrs = str(hrs)
        Time = hrs+":"+mins+" PM"
    else:
        hrs= str(hrs)
        Time = "0"+hrs+":"+mins+" AM"
    if Time == f"00:{mins} AM":
        Time = f"12:{mins} AM"
    
    schedule = month+" "+day+" "+year+" "+Time
    return schedule