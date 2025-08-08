# start time is in 12 hour format ending in AM or PM
# duration is in hours and minutes
# day is optional, it's the starting day of the week (case insensitive)

# output is should show (next day) after the time.
# if the result is more than a day, it should show (n days later) 
# where n is the num of days passed

# if the function is given the optional starting day
# then the output should display the day of the week as a result

# no python libraries needed to be imported

def add_time(start, duration, day):
    days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 
                        'Thursday', 'Friday', 'Saturday', 'Sunday']

    # parse start
    time_colon_pos = start.find(':')
    if time_colon_pos == -1:
        print(f'Invalid input: {start}')
        return
        
    time_hour = int(start[:time_colon_pos])
    time_min = int(start[time_colon_pos + 1 : time_colon_pos + 3])

    try:
        _, meridian = start.split()
    except ValueError:
        print(f'Invalid input: {start}')
        return
    meridian = meridian.upper()

    # validate start
    if not(1 <= time_hour <= 12):
        print(f'Invalid input: {time_hour}')
        return
    
    if not(0 <= time_min <= 59):
        print(f'Invalid input: {time_min}')
        return
    
    if meridian not in ['AM', 'PM']:
        print(f'Invalid input: {meridian}')
        return
    
    # parse duration
    duration_colon_pos = duration.find(':')
    if duration_colon_pos == -1:
        print(f'Invalid input: {duration}')
        return
    
    dur_hour = int(duration[:duration_colon_pos])
    dur_min = int(duration[duration_colon_pos + 1: duration_colon_pos + 3])
    
    # validate duration
    if dur_hour < 0:
        print(f'Invalid input: {dur_hour}')
        return
    if not (0 <= dur_min <= 59):
        print(f'Invalid input: {dur_min}')
        return
    
    # validate day (if given)
    if day is not None:
        if day.lower() not in [d.lower() for d in days_of_the_week]:
            print(f'Invalid input: {day}')
            return

    # calculate
    days_passed = 0

add_time("12:20 AM", "3:40", "Thursday")