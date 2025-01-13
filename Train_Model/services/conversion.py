# convert from SI to imperial

# inputs meters; ouputs feet
def meters_feet(number):
    return round(number * 3.28084,2)

# inputs feets; outputs meters
def feets_meters(number):
    return round(number * 0.3048, 2)

# inputs meters per second; output miles per hours
def meter_sec_miles_hour(number):
    return round(number * 2.23694, 2)

# input Kilometers; output miles
def kilometers_miles(number):
    return round(number * 0.62137119, 2)

# input miles; output kilometers
def miles_kilometers(number):
    return round(number/0.62137119, 2)

# input celcius; output fahrenheit
def celcius_fahrenheit(number):
    return round((number* 1.8)+32 ,2)

# input fahrenheit; output celcius
def fahrenheit_celcius(number):
    return round((number - 32) * 5/9, 2)

# Input Meters Per Second; Output Miles Per Hour
def mps_mph(number):
    return round(number * 2.23695, 2)

# Input Miles Per Hour; Output Meters Per Second
def mph_mps(number):
    return round(number * 0.44704, 2)

# Input Meters Per Second^2; Output Feet Per Second^2
def mpssquared_fpssquared(number):
    return round(number * 3.28084,2)

# Input Kilograms; Output Pounds
def kilograms_pounds(number):
    return round(number * 2.20462, 2) 

# Input watts; Output horsepower
def watts_horsepower(number):
    return round(number * 0.00134, 2)

# Input 
def newton_poundforce(number):
    return round(number * 0.22481, 2)