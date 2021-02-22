temperature=input('what is the temperature in fahrenheit?')

if temperature.isnumeric()==False:
    print('Input is not a numebr')
    exit()
temperature=int(temperature)
celsius=int((temperature-32)*5/9)
print('Temperature is celsius is '+str(celsius))

    