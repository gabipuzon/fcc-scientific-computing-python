def add_time(start, duration, day=None):
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
    if day:
        day = day.strip().capitalize()
        if day not in days_of_the_week:
            print(f'Invalid input: {day}')
    # calculate
    if meridian == 'AM':
        if time_hour == 12:
            time_hour = 0
    elif meridian == 'PM':
        if time_hour != 12:
            time_hour += 12

    converted_start = time_hour * 60 + time_min
    converted_dur = dur_hour * 60 + dur_min

    total_min = converted_start + converted_dur

    days_passed = total_min // 1440
    final_min = total_min % 1440

    new_hour = final_min // 60
    display_min = final_min % 60

    if new_hour == 0:
        display_hour, meridian = 12, 'AM'
    elif 1 <= new_hour < 12:
        display_hour, meridian = new_hour, 'AM'
    elif new_hour == 12:
        display_hour, meridian = 12, 'PM'
    else:
        display_hour, meridian = new_hour - 12, 'PM'
 
    # output format
    display_hour = int(display_hour)
    display_min = int(display_min)

    if day:
        start_index = days_of_the_week.index(day.capitalize())
        display_day = days_of_the_week[(start_index + days_passed) % len(days_of_the_week)]

    time_str = f'{display_hour}:{display_min:02d} {meridian}'
    if day:
        time_str += f', {display_day}'
    if days_passed == 1:
        time_str += f' (next day)'
    elif days_passed > 1:
        time_str += f' ({days_passed} days later)'
    return time_str

print(add_time('11:59 PM', '24:05'))