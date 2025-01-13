# convert from SI to imperial

# inputs meters; ouputs feet
def m_to_ft(number):
    return round(number * 3.28084, 2)

# inputs feets; outputs meters
def ft_to_m(number):
    return round(number * 0.3048, 2)

# input meters; output miles
def m_to_mi(distance_meters):
    # 1 mile is approximately 1609.34 meters
    return round(distance_meters / 1609.34, 2)

# inputs meters per second; output miles per hours
def mps_to_mph(number):
    return round(number * 2.23694, 2)

# input miles per hour (mph); output meters per second (mps)
def mph_to_mps(speed_mph):
    # 1 mile is approximately 1609.34 meters, and 1 hour is 3600 seconds
    return round(speed_mph * 1609.34 / 3600, 2)

# input miles per hour (mph); output kilometers per hour (kph)
def mph_to_kph(speed_mph):
    return round(speed_mph * 1.60934, 2)

# input kilometers per hour (kph); output miles per hour (mph)
def kph_to_mph(speed_kph):
    return round(speed_kph / 1.60934, 2)

# input Kilometers; output miles
def km_to_mi(number):
    return round(number * 0.62137119, 2)

# input miles; output kilometers
def mi_to_km(number):
    return round(number/0.62137119, 2)

# input celcius; output fahrenheit
def c_to_f(number):
    return round((number* 1.8)+32 ,2)

# input fahrenheit; output celcius
def f_to_c(number):
    return round((number - 32) * 5/9, 2)



