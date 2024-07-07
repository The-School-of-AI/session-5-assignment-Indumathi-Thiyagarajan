"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""
    # Repetition should be positive number
    if repetitions < 0:
        return ValueError("Repetition should be positive number")
    diff_sum = 0
    for i in range(repetitions):
        start = time.perf_counter()
        fn(*args, **kwargs)
        end = time.perf_counter()
        diff = end - start
        diff_sum+= diff
    average = diff_sum / repetitions
    return average


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if start is None:
        start = 0
    if end is None:
        end = 5
    # Return the list of number to the power of numbers from start to end
    powered_list = [number ** i for i in range (start,end+1)]  
    print(powered_list)
    return powered_list

def polygon_area(length, *args, sides = 3, **kwargs):
    """Retruns area of a regular polygon with number of sides between
    3 to 6 bith inclusive"""
    import math
    # Validations
    print("sides", sides)
    print("length", length)
    if sides >=3 and sides <=6:
        # Return area
        area = (sides * length**2) / (4 * math.tan(math.pi / sides))
    else:
        return ValueError("Sides should be within 3 to 6")
    print(area)
    return area

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations

    # if isinstance(temp_converter, time_it):
    #     print("belongs to instance of timeit")
    # Return the converted temprature
    if temp_given_in =='f':
        temperature = ((temp - 32) * 5 ) / 9

    if temp_given_in == 'c':
        temperature = ((temp * (9/5))+32)
    print(temperature)
    return temperature

def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    

    # Conversion factors for distance
    distance_conversion = {
        'km': 1,
        'm': 1000,
        'ft': 3280.84,
        'yd': 1093.61
    }
    
    # Conversion factors for time
    time_conversion = {
        'ms': 3600000,
        's': 3600,
        'min': 60,
        'hr': 1,
        'day': 1/24
    }
    
    if dist not in distance_conversion:
        raise ValueError(f"Invalid distance unit. Choose from: {list(distance_conversion.keys())}")
    
    if time not in time_conversion:
        raise ValueError(f"Invalid time unit. Choose from: {list(time_conversion.keys())}")
    
    # Convert km/h to the specified units
    speed_in_specified_units = speed * (distance_conversion[dist] / time_conversion[time])
    print(speed_in_specified_units)
    return speed_in_specified_units
