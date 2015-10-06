__author__ = 'Elvin Carvalho, 0907984 INFB1'

#function that checks if a letter(item)is lower/uppercase
def shiftIt(x,y):
    if x.islower():
        #if amount goes out of range(+z or -a) reset it to a or z
        if y >= 122:
            y = 97 + ((y%122)-1)
        elif y <= 97:
            y = 122 - ((97%y)-1)
        #Change the ascii to character
        result = chr(y)
        #print 'new %s = %s' %(y,result)
        #Add the result to the list
        resultL.append(result)

    elif x.isupper():
         if y >= 90:
            y = 65 + ((y%90)-1)
         elif y <= 65:
            y = 90 - ((65%y)-1)
         result = chr(y)
         #print 'new %s = %s' %(new_ascii,result)
         resultL.append(result)
    else:
            resultL.append(item)

while True:

    q1 = raw_input("Enter a string : \n")

    n = input("Amount: \n")
    lq1 = list(q1)

    #Get all the letters of your input
    print 'shift %s space(s)' %(n)
    resultL = []
    for item in lq1:

        ascii = ord(item)
        #print '%s = %s' %(item,ascii)
        new_ascii = ascii + n
        shiftIt(item,new_ascii)

    print q1,' = ',''.join(resultL)