## 1. time_it
### Description:
Measures the average execution time of a given function over a specified number of repetitions.

* Parameters:

fn: Function to time.
repetitions (optional): Number of times to execute fn.
*args, **kwargs: Additional arguments to pass to fn.
Returns:
Average time taken for fn to execute over repetitions.

## 2. squared_power_list
### Description:
Generates a list of powers of a number from start to end.

#### Parameters:

number: Base number for calculations.
start (optional): Starting power (default: 0).
end (optional): Ending power (default: 5).
Returns:
List of number raised to powers from start to end.

3. polygon_area
### Description:
Calculates the area of a regular polygon based on its number of sides and side length.

Parameters:

length: Length of each side of the polygon.
sides: Number of sides of the polygon (must be between 3 and 6 inclusive).
Returns:
Area of the regular polygon.

4. temp_converter
### Description:
Converts temperature between Celsius and Fahrenheit.

Parameters:

temp: Temperature value to convert.
temp_given_in: Unit of the input temperature ('c' for Celsius, 'f' for Fahrenheit).
Returns:
Converted temperature value.

5. speed_converter
### Description:
Converts speed from kilometers per hour (kmph) to various other units.

Parameters:

speed: Speed value in kmph to convert.
dist: Distance unit for the output speed ('km', 'm', 'ft', 'yd').
time: Time unit for the output speed ('ms', 's', 'min', 'hr', 'day').
Returns:
Speed converted to the specified units.
