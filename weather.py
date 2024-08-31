import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")

    # date = datetime.fromisoformat(iso_string)
    # result = date.strftime("%A %d %B %Y")
    # # print('Result --> ', result)
    # return result

    # Create a date 'object' to put my stuff into and convert ISO string using Python datetime
    #date_object = date.fromisoformat(iso_string)
    # Format date object to date format (e.g. Tuesday 06 July 2021)
    #formatted_date = date.strftime("%A %d %B %Y")
    #return formatted_date


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    #celcius_temp = 
    #F = 9/5 ×°C + 32
    #Celsius(°C) = (Fahrenheit(°F) - 32) × 5/9

    #result = weather.convert_f_to_c(temp_in_f)
    #celcius = (temp_in_fahrenheit - 32) * 5/9

    temp_in_celsius = (float(temp_in_fahrenheit) - 32) * 5/9
    return round(temp_in_celsius, 1)



def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """

    total = sum([float(i) for i in weather_data])/len(weather_data)
    return float(total)
    



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """

    list = []
    with open (csv_file, "r") as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            if row != []:
                list.append([row[0], int(row[1]), int(row[2])])
            
    return list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # Find a spot to store your minimum number and the index of it. Assume at the start that the first thing you look at is 0.
    
    # handle empty list
    if weather_data == []:
        return ()
    # change weather data to float
    min_weather_data = [float(weather) for weather in weather_data]
    # step 1: check how many elements in the list
    total_elements = len(min_weather_data)
    # step 2: set first element as the staring point to compare with the other elements in the list, and find out the minium vale
    min_value = min_weather_data[0]
    # step 4: compare each element in the list
    # for i in range(total_elements):
    #     if min_value > updated_weather_data[i]:
    #         min_value = updated_weather_data[i]
    #         min_index = i
    # # print(min_value)
    # # step 5: find the last index of the minimum vale
    last_index = -1
    for index, value in enumerate(min_weather_data):  # https://stackoverflow.com/questions/24816669/find-the-minimum-value-in-a-python-list
        if min_value > value:
            min_value = value
        # print(index, value)
        if value == min_value:
            last_index = index
    # print(last_index)
    # print(f”The minimum value is {min_value} and the last position in the list is {last_index}“)
    return (min_value, last_index) #run_tests.py expects returning tuple
# print(find_min([49, 57, 56, 55, 53, 49]))


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    # Find a spot to store your minimum number and the index of it. Assume at the start that the first thing you look at is 0.
    
    # handle empty list
    if weather_data == []:
        return ()
    # change weather data to float
    max_weather_data = [float(weather) for weather in weather_data]
    # step 1: check how many elements in the list
    total_elements = len(max_weather_data)
    # step 2: set first element as the staring point to compare with the other elements in the list, and find out the minium vale
    max_value = max_weather_data[0]
    # step 4: compare each element in the list
    # for i in range(total_elements):
    #     if min_value > updated_weather_data[i]:
    #         min_value = updated_weather_data[i]
    #         min_index = i
    # # print(min_value)
    # # step 5: find the last index of the minimum vale
    last_index = -1
    for index, value in enumerate(max_weather_data):  # https://stackoverflow.com/questions/24816669/find-the-minimum-value-in-a-python-list
        if max_value < value:
            max_value = value
        # print(index, value)
        if value == max_value:
            last_index = index
    # print(last_index)
    # print(f”The minimum value is {min_value} and the last position in the list is {last_index}“)
    return (max_value, last_index) #run_tests.py expects returning tuple
# print(find_min([49, 57, 56, 55, 53, 49]))


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    num_of_data = len(weather_data)

    min_c_list = []
    max_c_list = []
    
    for summary_list in weather_data:
        min_c_list.append(summary_list[1])
        max_c_list.append(summary_list[2])
    min_temp, min_index = find_min(min_c_list)
    max_temp, max_index = find_max(max_c_list)
    average_min = calculate_mean(min_c_list)
    average_max = calculate_mean(max_c_list)
    day_min = convert_date(weather_data[min_index][0])
    day_max = convert_date(weather_data[max_index][0])
    return (
        f"{num_of_data} Day Overview\n"
        f"  The lowest temperature will be {format_temperature(convert_f_to_c(min_temp))}, and will occur on {day_min}.\n"
        f"  The highest temperature will be {format_temperature(convert_f_to_c(max_temp))}, and will occur on {day_max}.\n"
        f"  The average low this week is {format_temperature(convert_f_to_c(average_min))}.\n"
        f"  The average high this week is {format_temperature(convert_f_to_c(average_max))}.\n"
    )
    # Takes all the given weather data. Create an output object.
    # Iterate over a list
    # Assign variables to a new list
    # change weather data to a string
    # string_summary =
    # Ling: Go to test generate
    # Call isodate function

# def generate_summary(weather_data):
# data required: min temp, max temp, average low , average high, day and date, number of days in weather data
# find minium and maximum temperature
# convert minium and maximum temperature from fahrenheit to celsius
# format minium and maximum temperature to include °C
# find day and date data for minimum and maximum temperature
# check how many days in weather data
# find average low and high temperature
# convert average low and high temperature from fahrenheit to celsius
# format average low and high temperature to include °C
# return formate data


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    num_of_data = len(weather_data)
    day_list = []
    min_c_list = []
    max_c_list = []
    output = ""
    for i in range(num_of_data):
        day = convert_date(weather_data[i][0])
        day_list.append(day)
        min_c = convert_f_to_c(weather_data[i][1])
        format_min_c = format_temperature(min_c)
        min_c_list.append(format_min_c)
        max_c = convert_f_to_c(weather_data[i][2])
        format_max_c = format_temperature(max_c)
        max_c_list.append(format_max_c)
        output += f"---- {day_list[i]} ----\n  Minimum Temperature: {min_c_list[i].strip()}\n  Maximum Temperature: {max_c_list[i].strip()}\n\n"
    return output
