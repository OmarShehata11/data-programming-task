from datetime import datetime
dep_time = input("Enter departure time (HH:MM): ")
arr_time = input("Enter arrival time (HH:MM): ")
dep_datetime = datetime.strptime(dep_time, "%H:%M")
arr_datetime = datetime.strptime(arr_time, "%H:%M")
trip_time = arr_datetime - dep_datetime
hours = trip_time.seconds//3600
minutes = (trip_time.seconds%3600)//60
print("Trip time: {} hrs and {} min".format(hours, minutes))
