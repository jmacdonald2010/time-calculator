def add_time(start_time, duration, starting_day=None):
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    # parse the start_time input
    start_time_values = start_time.split()
    input_time = start_time_values[0].split(":")
    # sth is start time hours
    sth = int(input_time[0])
    # stm is start time minutes
    stm = int(input_time[1])
    # convert to 24 hr time
    if start_time_values[1] == "PM":
        sth = sth + 12

    # parse duration input
    duration_values = duration.split(":")
    # dh is duration hours
    dh = int(duration_values[0])
    # dm is duration minutes
    dm = int(duration_values[1])

    # time math
    output_hours = sth + dh
    output_min = stm + dm
    
    # overflow w/ min
    if output_min >= 60:
        output_min = output_min - 60
        output_hours = output_hours + 1
    
    output_day = None

    # calc if next day or not, and calc # of next days
    days_later = ""
    if output_hours >= 24:
        days_later = int(output_hours / 24)
        output_hours = output_hours - (24 * days_later)
        # determine day of week
        if starting_day != None:
            starting_day = starting_day.lower()
            starting_day = starting_day.capitalize()
            pos_in_tuple = days_of_week.index(starting_day)
            calc_days = 0
            if days_later > 6:
                calc_days = days_later % 7
                output_day = days_of_week[(pos_in_tuple + calc_days) % 7]
            else:
                output_day = pos_in_tuple + days_later
                if output_day > 6:
                    output_day = days_of_week[(pos_in_tuple + days_later - 7)]
                else:
                    output_day = days_of_week[(pos_in_tuple + days_later)]
        if days_later == 1:
            days_later = "(next day)"
        else:
            days_later = f"({days_later} days later)"
        
    
    # deal w/ overflow in values:
    # for minutes < 10
    if output_min < 10:
        output_min = "0" + str(output_min)
    # determine am/pm
    am_pm = "AM"
    if output_hours >= 12:
        if output_hours == 24:
            output_hours = output_hours - 12
        elif output_hours != 12:
            output_hours = output_hours - 12
            am_pm = "PM"
        elif output_hours == 12:
            am_pm = "PM"
    if output_hours == 0:
        output_hours = 12    

    if output_day is None:
        if starting_day is not None:
            output_day = starting_day.lower()
            output_day = starting_day.capitalize()

    # build string
    output_time = str(output_hours) + ":" + str(output_min) + " " + am_pm
    if output_day is not None:
        if days_later == "":
            output = output_time + "," + " " + output_day
        else:
            output = output_time + "," + " " + output_day + " " + days_later
    else:
        if days_later == "":
            output = output_time
        else:
            output = output_time + " " + days_later
    # this is changing my return variable to their desired one
    # i didn't want to retype mine above
    new_time = output
    return new_time
