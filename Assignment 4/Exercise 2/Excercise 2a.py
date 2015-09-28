__author__ = 'Elvin Carvalho, 0907984 INFB1'

#Function check if input given is right
def checkInput(q):
    inputCorrect = ['rock', 'paper', 'scissors']

    if not q in inputCorrect:
        print('No input/Wrong input given0\n\n')
        n = 'false'
    else:
        n = 'true'
    return n

#Functions different outcomes
def rXp(n):
        print "PLAYER %s WINS! PAPER beats ROCK.\n" %(n)

def rXs(n):
        print "PLAYER %s WINS! ROCK beats SCISSORS.\n" %(n)

def sXp(n):
        print "PLAYER %s WINS! SCISSORS beats PAPER.\n" %(n)

def same():
    print "DRAW! no one wins\n"

#Player 1&2 input
p1 = raw_input("PLAYER 1: rock, paper or scissors : \n")

while checkInput(p1) == 'false':
    p1 = raw_input("PLAYER 1: rock, paper or scissors : \n")
else:
    p2 = raw_input("PLAYER 2: rock, paper or scissors : \n")
    while checkInput(p2) == 'false':
        p2 = raw_input("PLAYER 2: rock, paper or scissors : \n")
    else:
        print 'PLAYER 1 used %s and PLAYER 2 used %s' %(p1.upper(),p2.upper())

        if p1 == p2:
            p1 = 'same'
            p2 = ''

        combo = p1 + p2

        if combo == 'rockpaper':
            rXp(2)
        elif combo == 'rockscissors':
            rXs(1)
        elif combo == 'paperrock':
            rXp(1)
        elif combo == 'paperscissors':
            sXp(2)
        elif combo == 'scissorsrock':
            rXs(2)
        elif combo == 'scissorspaper':
            sXp(1)
        elif combo == 'same':
            same()
