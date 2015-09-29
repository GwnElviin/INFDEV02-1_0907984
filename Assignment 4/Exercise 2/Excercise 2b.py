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
def outcome(n,i1,i2):
    print "PLAYER %s WINS! %s beats %s.\n" %(n, p1.upper(), p2.upper())
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
            outcome(2,'paper','rock')
        elif combo == 'rockscissors':
            outcome(1,'rock','scissors')
        elif combo == 'paperrock':
            outcome(1,'paper','rock')
        elif combo == 'paperscissors':
            outcome(2,'scissors','paper')
        elif combo == 'scissorsrock':
            outcome(2,'rock','scissors')
        elif combo == 'scissorspaper':
            outcome(1,'scissors','paper')
        elif combo == 'rockspock':
            outcome(2,'spock','rock')
        elif combo == 'spockrock':
            outcome(1,'spock','rock')
        elif combo == 'rocklizard':
            outcome(1,'rock','lizard')
        elif combo == 'lizardrock':
            outcome(2,'rock','lizard')
        elif combo == 'paperspock':
            outcome(1,'paper','spock')
        elif combo == 'spockpaper':
            outcome(2,'paper','spock')
        elif combo == 'scissorslizard':
            outcome(1,'scissors','lizard')
        elif combo == 'lizardscissors':
            outcome(2,'scissors','lizard')
        elif combo == 'scissorsspock':
            outcome(2,'spock','scissors')
        elif combo == 'spockscissors':
            outcome(1,'spock','scissors')
        elif combo == 'paperlizard':
            outcome(2,'lizard','paper')
        elif combo == 'lizardpaper':
            outcome(1,'lizard','paper')
        elif combo == 'spocklizard':
            outcome(2,'lizard','spock')
        elif combo == 'lizardspock':
            outcome(1,'lizard','spock')
        elif combo == 'same':
            same()
