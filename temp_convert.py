#Temperature converter
#https://en.wikipedia.org/wiki/Conversion_of_units_of_temperature

temp = float(input("Enter the temperature. "))
from_temp_scale = input("Enter the abbreviation of the starting temperature scale. ")
to_temp_scale = input("Enter the abbreviation of the destination temperature scale. ")

def temp_convert(temp, from_temp_scale, to_temp_scale):
    """Converts temperature from one temperature scale to another.

    Available temperature scales are:
    Celsius (C), Kelvin (K), Fahrenheit (F), Rankine (R), Delisle (De), Newton (N), Reaumur (Re), Romer (Ro).

    User to specify starting and ending temperature scales by indicating the abbreviations given in the brackets."""

    if from_temp_scale == 'C': #conversion from Celsius
        if to_temp_scale == 'K':
            return '{}C is approximately {}K.'.format(temp, round(temp+273.15, 2))
        elif to_temp_scale == 'F':
            return '{}C is approximately {}F.'.format(temp, round(temp*9/5+32, 2)) 
        elif to_temp_scale == 'R':
            return '{}C is approximately {}R.'.format(temp, round((temp+273.15)*9/5, 2))  
        elif to_temp_scale == 'De':
            return '{}C is approximately {}De.'.format(temp, round((100-temp)*3/2, 2)) 
        elif to_temp_scale == 'N':
            return '{}C is approximately {}De.'.format(temp, round(temp*33/100, 2))
        elif to_temp_scale == 'Re':
            return '{}C is approximately {}Re.'.format(temp, round(temp*4/5, 2))
        elif to_temp_scale == 'Ro':
            return '{}C is approximately {}Re.'.format(temp, round(temp*21/40+7.5, 2))
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    elif from_temp_scale == 'K': #conversion from Kelvin
        if to_temp_scale == 'C':
            return '{}K is approximately {}C.'.format(temp, round(temp-273.15, 2))
        elif to_temp_scale == 'F':
            return '{}K is approximately {}F.'.format(temp, round(temp*9/5-459.67, 2))
        elif to_temp_scale == 'R':
            return '{}K is approximately {}R.'.format(temp, round(temp*9/5, 2))
        elif to_temp_scale == 'De':
            return '{}K is approximately {}De.'.format(temp, round((373.15-temp)*3/2, 2))
        elif to_temp_scale == 'N':
            return '{}K is approximately {}N.'.format(temp, round((temp-273.15)*33/100, 2))
        elif to_temp_scale == 'Re':
            return '{}K is approximately {}Re.'.format(temp, round((temp-273.15)*4/5, 2))
        elif to_temp_scale == 'Ro':
            return '{}K is approximately {}Ro.'.format(temp, round((temp-273.15)*21/40+7.5, 2))
        else:
            return 'Invalid abbreviation for destination temperature scale.'
    
    elif from_temp_scale == 'F': #conversion from Fahrenheit
        if to_temp_scale == 'C':
            return '{}F is approximately {}C.'.format(temp, round(5/9*(temp-32), 2))
        elif to_temp_scale == 'K':
            return '{}F is approximately {}K.'.format(temp, round((temp+459.67)*5/9, 2))
        elif to_temp_scale == 'R':
            return '{}F is approximately {}R.'.format(temp, round(temp+459.67, 2))
        elif to_temp_scale == 'De':
            return '{}F is approximately {}De.'.format(temp, round((212-temp)*5/6, 2))
        elif to_temp_scale == 'N':
            return '{}F is approximately {}N.'.format(temp, round((temp-32)*11/60, 2))
        elif to_temp_scale == 'Re':
            return '{}F is approximately {}Re.'.format(temp, round((temp-32)*4/9, 2))
        elif to_temp_scale == 'Ro':
            return '{}F is approximately {}Ro.'.format(temp, round((temp-32)*7/24+7.5, 2))
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    elif from_temp_scale == 'R': # conversion from Rankine
        if to_temp_scale == 'C':
            return '{}R is approximately {}C.'.format(temp, round((temp-491.67)*5/9, 2))
        elif to_temp_scale == 'F':
            return '{}R is approximately {}F.'.format(temp, round(temp-459.67, 2))
        elif to_temp_scale == 'K':
            return '{}R is approximately {}K.'.format(temp, round(temp*5/9, 2))
        elif to_temp_scale == 'De':
            return '{}R is approximately {}De.'.format(temp, round((671.67-temp)*5/6, 2))
        elif to_temp_scale == 'N':
            return '{}R is approximately {}N.'.format(temp, round((temp-491.67)*11/60, 2))
        elif to_temp_scale == 'Re':
            return '{}R is approximately {}Re.'.format(temp, round((temp-491.67)*4/9, 2))
        elif to_temp_scale == 'Ro':
            return '{}R is approximately {}Ro.'.format(temp, round((temp-491.67)*7/24+7.5, 2))
        else:
            return 'Invalid abbreviation for destination temperature scale.'
    
    elif from_temp_scale == 'De': # conversion from Delisle
        if to_temp_scale == 'C':
            return '{}De is approximately {}C.'.format(temp, round(100-temp*2/3, 2))
        elif to_temp_scale == 'F':
            return '{}De is approximately {}F.'.format(temp, round(212-temp*6/5, 2))
        elif to_temp_scale == 'K':
            return '{}De is approximately {}K.'.format(temp, round(373.15-temp*2/3, 2))
        elif to_temp_scale == 'R':
            return '{}De is approximately {}R.'.format(temp, round(671.67-temp*6/5, 2))
        elif to_temp_scale == 'N':
            return '{}De is approximately {}N.'.format(temp, round(33-temp*11/50, 2))
        elif to_temp_scale == 'Re':
            return '{}De is approximately {}Re.'.format(temp, round(80-temp*8/15, 2))
        elif to_temp_scale == 'Ro':
            return '{}De is approximately {}Ro.'.format(temp, round(60-temp*7/20, 2))
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    elif from_temp_scale == 'N': # conversion from Newton
        if to_temp_scale == 'C':
            pass
        elif to_temp_scale == 'F':
            pass
        elif to_temp_scale == 'K':
            pass
        elif to_temp_scale == 'R':
            pass
        elif to_temp_scale == 'De':
            pass
        elif to_temp_scale == 'Re':
            pass
        elif to_temp_scale == 'Ro':
            pass
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    elif from_temp_scale == 'Re': # conversion from Reaumur
        if to_temp_scale == 'C':
            pass
        elif to_temp_scale == 'F':
            pass
        elif to_temp_scale == 'K':
            pass
        elif to_temp_scale == 'Ra':
            pass
        elif to_temp_scale == 'De':
            pass
        elif to_temp_scale == 'N':
            pass
        elif to_temp_scale == 'Ro':
            pass
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    elif from_temp_scale == 'Ro': # conversion from Romer
        if to_temp_scale == 'C':
            pass
        elif to_temp_scale == 'F':
            pass
        elif to_temp_scale == 'K':
            pass
        elif to_temp_scale == 'Ra':
            pass
        elif to_temp_scale == 'De':
            pass
        elif to_temp_scale == 'N':
            pass
        elif to_temp_scale == 'Re':
            pass
        else:
            return 'Invalid abbreviation for destination temperature scale.'

    else:
        return 'Invalid abbreviation for starting temperature scale.'

print(temp_convert(temp, from_temp_scale, to_temp_scale))

# To implement: calibration table similar to that of on Wikipedia

