"""get DOB and time of birth from user and calculate current age and if current day is their birthday then wish them 'happy birthday'"""
from datetime import datetime

def date_validation(dob_str,timeOfBrith):
   datetime_format = "%Y/%m/%d %H:%M"

   dob_with_time_str = f"{dob_str} {timeOfBrith}"
   dob = datetime.strptime(dob_with_time_str, datetime_format)
   current_date = datetime.now()

   years = abs(current_date.year - dob.year)
   months = abs(current_date.month - dob.month)
   days = abs(current_date.day - dob.day)    
   return years, months, days , dob

Date_of_birth = input("Enter your date of birth(format[YYYY/MM/DD]): ")
Time_of_birth = input("Enter your time of birth(format[HH:MM]): ")
age_years, age_months, age_days ,dob = date_validation(Date_of_birth,Time_of_birth) 

print(f"Days passed since born: {age_years} years, {age_months} months, and {age_days} days.")
today = datetime.now()
if today.month == dob.month and today.day == dob.day:
   print("Happy Birthday!")



# from datetime import datetime
# import math
# def calculate_fee(min_taken):
#    if min_taken < 15:
#       return 0
#    if min_taken <= 60:
#       return 100
#    # hours = math.ceil(min_taken/60)
#    hours = int(min_taken//60)
#    fee = 100 + (hours - 1)*150
#    return fee
# def convert_to_date(str_datetime):
#    format = '%Y/%m/%d %H:%M'
#    result = datetime.strptime(str_datetime,format)
#    return result

# str_entry_time = '2024/11/30 08:10'
# str_exit_time = '2024/12/01 08:10'

# entry_time = convert_to_date(str_entry_time)
# exit_time = convert_to_date(str_exit_time)

# total_hours = exit_time - entry_time
# total_minutes = total_hours.total_seconds()//60
# total_fee = calculate_fee(total_minutes)
# print(f"You have parked for :{total_minutes} and so the fee is :{total_fee}")