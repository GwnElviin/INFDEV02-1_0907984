__author__ = 'Elvin Carvalho, 0907984 INFB1, ABS()'

#function to calculate absolute
def absoluteN():
    q1 = input('Input number: ')
    formula = abs(q1)
    print('The absolute of %s = %s' %(q1,formula))

#check if no input is given
try:
    absoluteN()
except SyntaxError:
    q1 = None
    print('No input/Wrong input given')
    absoluteN()


