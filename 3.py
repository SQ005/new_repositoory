import string, os
if not os.path.exists("letters"):
   # os.makedirs("upper")
# for letter in string.ascii_uppercase:
#    with open(letter + ".txt", "w") as f:
#        f.writelines(letter)
   for letter in string.ascii_uppercase:
     os.remove(letter + ".txt")
# import datetime
# current_date_time = datetime.datetime.now
# current_time = current_date_time.time()
# print(current_time)
# current_date = datetime.date.today()
# current_date1 = datetime.datetime.now()
# current_date2 = datetime.datetime.today()
# print(current_date)
# print(current_date1)
# print(current_date2)


# import datetime

# current_date_time = datetime.datetime.now()
# current_time = current_date_time.time()
# print(current_time)

# attr = dir(datetime)
# print(attr)

# date = datetime.timedelta(days = 4, hours = 34, seconds = 112324)
# print(date)
# date1 = datetime.timezone  