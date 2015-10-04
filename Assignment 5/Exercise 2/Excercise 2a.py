__author__ = 'Elvin Carvalho, 0907984 INFB1'

# print len([c for c in p1 if c.isupper()])     #checks upper case characters
# print len([c for c in p1 if c.islower()])     #checks lower case characters
# print len([c for c in p1 if c.isdigit()])     #checks digits characters

#Function that calculates how many different characters u use and returns a the amount(upper,lower,digit,special)
def differentChar(x):
    chars = 0
    lenghtstring = (len(x))
    lenght3 = len([c for c in x if c.isdigit()]) + len([c for c in x if c.islower()]) + len([c for c in p1 if c.isupper()])
    if len([c for c in x if c.isdigit()]) > 0:
        chars = chars + 1
    if len([c for c in x if c.islower()]) > 0:
        chars = chars + 1
    if len([c for c in p1 if c.isupper()]) > 0:
        chars = chars + 1
    if lenghtstring - lenght3 > 0:
        chars = chars + 1
    return chars


while True:
    p1 = raw_input("Enter your password : \n")

#If string lenght is smaller or equal to 7 you entered a easy password
    if len(p1) <= 7:
        print('Password is EASY')
#If string lenght is smaller or equal to 7 and the amount of different characters is bigger or equal to 4 you entered a medium password
    elif len(p1) <= 7 and differentChar(p1) >= 4:
        print('Password is Medium')

    elif len(p1) <13 and differentChar(p1) >= 3:
        print('Password is MEDIUM')

    elif len(p1) <13 and differentChar(p1) <= 2:
        print('Password is MEDIUM')

    elif len(p1) >13 and differentChar(p1) >= 2:
        print('Password is HARD')

    else:
        print('Password is HARD')

