def GetTimeArray(prompt):
    while True:
        try:
            time_str = input(prompt).split()
            hours, minutes = map(int, time_str)
            if 0 <= hours <= 23 and 0 <= minutes <= 59:
                return hours, minutes
            else:
                print("Error! Invalid time range. Please enter valid time.")
        except ValueError:
            print("Error! Enter time in HH MM format.")

def AddTimeArray(departure_time, trip_time):
    total_minutes = departure_time[1] + trip_time[1] + (departure_time[0] + trip_time[0]) * 60
    arrival_hours, arrival_minutes = divmod(total_minutes, 60)
    return arrival_hours % 24, arrival_minutes

def DisplayTimeArray(prompt, arrival_time):
    print(prompt)
    print(f"{arrival_time[0]:02d}:{arrival_time[1]:02d}")

# Main script
dt = GetTimeArray("Enter Departure Time: ")
tt = GetTimeArray("Enter Trip Time: ")
at = AddTimeArray(dt, tt)
DisplayTimeArray("Arrival Time:", at)

