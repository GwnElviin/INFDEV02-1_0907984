__author__ = 'Elvin Carvalho, 0907984 INFB1'

#Function checks if input given is right
def checkInput(q):
    inputCorrect = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    if not q in inputCorrect:
        print('No input/Wrong input given0\n\n')
        n = 'false'
    else:
        n = 'true'
    return n

#Functions with different outcomes
def rXp(n):
    print "PLAYER %s WINS! PAPER beats ROCK.\n" %(n)
def rXs(n):
    print "PLAYER %s WINS! ROCK beats SCISSORS.\n" %(n)
def rXsp(n):
    print "PLAYER %s WINS! SPOCK vapourises ROCK.\n" %(n)
def rXl(n):
    print "PLAYER %s WINS! ROCK crushes LIZARD.\n" %(n)
def pXsp(n):
    print "PLAYER %s WINS! PAPER disproves SPOCK.\n" %(n)
def pXl(n):
    print "PLAYER %s WINS! LIZARD eats PAPER.\n" %(n)
def sXsp(n):
    print "PLAYER %s WINS! SPOCK smashes SCISSORS.\n" %(n)
def sXl(n):
    print "PLAYER %s WINS! SCISSORS decapitates LIZARD.\n" %(n)
def spXl(n):
    print "PLAYER %s WINS! LIZARD poisons SPOCK.\n" %(n)
def sXp(n):
    print "PLAYER %s WINS! SCISSORS beats PAPER.\n" %(n)
def same():
    print "DRAW! no one wins\n"

#Player 1&2 input
p1 = raw_input("PLAYER 1: rock, paper, scissors, spock or lizard : \n")

while checkInput(p1) == 'false':
    p1 = raw_input("PLAYER 1: rock, paper, scissors, spock or lizard : \n")
else:
    p2 = raw_input("PLAYER 2: rock, paper, scissors, spock or lizard : \n")
    while checkInput(p2) == 'false':
        p2 = raw_input("PLAYER 2: rock, paper, scissors, spock or lizard : \n")
    else:
        print 'PLAYER 1 used %s and PLAYER 2 used %s' %(p1.upper(),p2.upper())

        if p1 == p2:
            p1 = 'same'
            p2 = ''

        combo = p1 + p2

#User input decides what function u will use
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
        elif combo == 'rockspock':
            rXsp(2)
        elif combo == 'spockrock':
            rXsp(1)
        elif combo == 'rocklizard':
            rXl(1)
        elif combo == 'lizardrock':
            rXl(2)
        elif combo == 'paperspock':
            pXsp(1)
        elif combo == 'spockpaper':
            pXsp(2)
        elif combo == 'scissorslizard':
            sXl(1)
        elif combo == 'lizardscissors':
            sXl(2)
        elif combo == 'scissorsspock':
            sXsp(2)
        elif combo == 'spockscissors':
            sXsp(1)
        elif combo == 'paperlizard':
            pXl(2)
        elif combo == 'lizardpaper':
            pXl(1)
        elif combo == 'spocklizard':
            spXl(2)
        elif combo == 'lizardspock':
            spXl(1)
        elif combo == 'same':
            same()
