"""
Write a function named add_time that takes in two required parameters and
one optional parameter:

- a start time in the 12-hour clock format (ending in AM or PM)
- a duration time that indicates the number of hours and minutes
- (optional) a starting day of the week, case insensitive
"""


def add_time(start: str, duration: str, starting_day: str = None) -> str:
    """The function adds the duration time to the start time and returns the result.

    If the result will be the next day, it will show (next day) after the time.
    If the result will be more than one day later, it shows (n days later) after
    the time, where "n" is the number of days later.

    If the function is given the optional starting day of the week parameter,
    then the output displays the day of the week of the result.
    The day of the week in the output appears after the time and before
    the number of days later.

        Args:
            start (str): Start time.
            duration (str): Duration in ##:## format.
            starting_day (str, optional): The day of the start time.
            Defaults to None.

        Returns:
            str: Calculated time.
    """
    LIST_OF_DAYS: list[str] = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # get time from arguments and split into hours, mins and pm / am
    time, pm_am = start.split()
    pm_am = pm_am.strip().upper()
    hours, mins = time.strip().split(":")
    # get starting day
    if starting_day:
        starting_day: str = starting_day.strip().capitalize()
    # get duration and split into hours and mins
    duration_hours, duration_mins = duration.strip().split(":")

    # cast times to int values
    duration_hours_int: int = int(duration_hours)
    duration_mins_int: int = int(duration_mins)
    hours_int: int = int(hours)
    mins_int: int = int(mins)

    # check if the minutes for the duration and time are acceptable
    if duration_mins_int > 59 or duration_mins_int < 0:
        return f"Error: Minutes of the duration are out of bounds: {duration_mins_int}"

    if mins_int > 59 or mins_int < 0:
        return f"Error: Minutes of for the time are out of bounds: {mins_int}"

    # check if the given value for day exists in a week
    if starting_day not in LIST_OF_DAYS and None:
        return f"Error: {starting_day} is no day in a week."

    # check if valid day period
    if pm_am not in ["AM", "PM"]:
        return f"Error: {pm_am} is not a vaild day period."

    # change into 24-hour format if its PM because it easier to calculate
    if pm_am == "PM":
        hours_int += 12

    # calculate time for the minutes of time and duration
    combined_time: int = duration_mins_int + mins_int
    # divmod splits the added minutes into a hour and minute value
    combined_hour, combined_mins = divmod(combined_time, 60)

    # calculate the total duration as hours and minutes
    total_hours: int = duration_hours_int + combined_hour + hours_int
    total_mins: int = combined_mins

    # how many days have passed
    days_passed: int = int(total_hours / 24)

    # calculate new time
    new_hours: int = total_hours % 24
    new_mins: int = total_mins

    # make sure that its a 12-hour time format
    period = "AM"
    if new_hours >= 12:
        new_hours -= 12
        if new_hours == 0:
            new_hours = 12
        period = "PM"

    # make sure that when new_hours == 0 is 12
    # if this check doesn't happen it displays 0:25 AM instead of 12:25 AM
    if new_hours == 0:
        new_hours = 12

    # display the new time in the requested string format depending on
    # a requested day or not.
    if starting_day is None:
        if days_passed > 1:
            new_time = f"{new_hours}:{new_mins:02d} {period} ({days_passed} days later)"
        elif days_passed == 1:
            new_time = f"{new_hours}:{new_mins:02d} {period} (next day)"
        else:
            new_time = f"{new_hours}:{new_mins:02d} {period}"
    else:
        new_day = LIST_OF_DAYS[
            (LIST_OF_DAYS.index(starting_day) + 1 + days_passed) % 7 - 1
        ]
        if days_passed > 1:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day} ({days_passed} days later)"
        elif days_passed == 1:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day} (next day)"
        else:
            new_time = f"{new_hours}:{new_mins:02d} {period}, {new_day}"

    return new_time
