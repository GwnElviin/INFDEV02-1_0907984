__author__ = 'Elvin Carvalho, 0907984 INFB1'

#Function to get Kelvin from Celsius input
def CtoK():
    q1 = input('Celsius to Kelvin: ')

    #check abolute zero point
    if q1 < -273.15:
        print("Cant go lower (minimum -273.15)")
        CtoK()
    else:
        formula = (q1 + 273.15)
        celsius = format(formula, '.2f')
        print('%s degrees Celsius is %s degrees Kelvin' % (q1, celsius))

#If no input, show it and try again
try:
    CtoK()
except SyntaxError:
    q1 = None
    print('No input given')
    CtoK()
