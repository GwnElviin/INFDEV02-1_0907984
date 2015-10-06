from Start import *

#For this assigment you are asked to use the drawing facilities of python provided by the turtle library.
#For simplicity we provide you an interfae that hides the complexitie of the turtule library.
#It is important for the correct execution of this program that you do not remove the header and the footer of
# this file.
#Add your code within the def Program(): ... (mind the spaces)
#
#If you try to run this sample a white screen will appear and a black triangle (from now on pen) will be drawn 
# in the middle.
#To move the pen we provide you two instructions: 
#   (i)    forward (amount)           'forward' moves the pen by 'amount' steps
#                                     amount is a value of type Integer
#
#   (ii)   turn (amount)              'turn' rotates the pen by 'amount' degrees
#                                     amount is a value of type Integer
#
#   (iii)  change_color_to (color)    'change_color_to' changes the color of the pen into 'color'
#                                      the possible colors are: Black, Green, Blue, and Red
#
#By combining forward and turn (inside loops) you are able to draw lots of nice shapes :) good luck and have fun!


def Program():
    #SUPPORTING INSTRUCTION
    #use 'get()' to read the input and store it into a variable. The input is provided in the shape of an ASCII integer number.
    #Check https://en.wikipedia.org/wiki/ASCII for the complete ASCII table 
    #Example:
    # The following code reads the input and stores it into a variable called 'x'. 'x' is then printed out into the console
    # x =get()
    # print (x)w=119 a=97 d=100 s=115
    


    #---------------------------------------------------------------------
    #                  PUT YOUR CODE BELOW
    #---------------------------------------------------------------------
    #get ascii of key
    x =get()
    print (x)
    #if ascii = w move forward 5 steps
    if x == 119:
      forward(5)
    #if ascii = a rotate -90 degrees  
    elif x == 97:
      turn(-90)
      change_color_to ('blue') 
    #if ascii = d rotate 90 degrees  
    elif x == 100:
      turn(90) 
      change_color_to ('purple')

    elif x == 115:
      turn(360)

    #if ascii = z make a star
    elif x == 122:
        change_color_to ('yellow')
      #everytime that num is in the range of 0 -97 
        for num in range(0,97):
            forward(1)
            y = 8
            # if num / y equals 0 turn 150 degrees
            if num % y == 0:
                turn(150)
          
        


run(Program)
from End import *
