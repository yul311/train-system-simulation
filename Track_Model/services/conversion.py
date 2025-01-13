# convert from SI to imperial and vice versa

# inputs meters; output feet
def meters_feet(number):
    return round(number * 3.28084,3)

# input feet; output meters
def feet_meters(number):
    return round(number * 0.3048,3)

# input Kilometers; output miles
def kilometers_miles(number):
    return round(number * 0.62137119, 2)

# input miles; output kilometers
def miles_kilometers(number):
    return round(number/0.62137119,2)

# input celcius; output fahrenheit
def celcius_fahrenheit(number):
    return round((number* 1.8)+32 ,2)

# input fahrenheit; output celcius
def fahrenheit_celcius(number):
    return round(number - 32) * 5/9

# Input Meters Per Second; Output Miles Per Hour
def mph_kph(number):
    return round(number * 1.60934, 2)

# input kilometers per hour; output miles per hour
def kph_mph(number):
    return round(number * 0.6213711922,2)

# Input Meters Per Second^2; Output Feet Per Second^2
def mpssquared_fpssquared(number):
    return round(number * 3.28084,2)