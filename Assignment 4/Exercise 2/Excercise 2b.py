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
def outcome(n,i1,m,i2):
    print "PLAYER %s WINS! %s %s %s.\n" %(n, i1.upper(),m.upper(), i2.upper())
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

#User input decides what function u will use and what parameters you send
        if combo == 'rockpaper':
            outcome(2,'paper','covers','rock')
        elif combo == 'rockscissors':
            outcome(1,'rock','crushes','scissors')
        elif combo == 'paperrock':
            outcome(1,'paper','covers','rock')
        elif combo == 'paperscissors':
            outcome(2,'scissors','cuts','paper')
        elif combo == 'scissorsrock':
            outcome(2,'rock','crushes','scissors')
        elif combo == 'scissorspaper':
            outcome(1,'scissors','cuts','paper')
        elif combo == 'rockspock':
            outcome(2,'spock','vapourises','rock')
        elif combo == 'spockrock':
            outcome(1,'spock','vapourises','rock')
        elif combo == 'rocklizard':
            outcome(1,'rock','crushes','lizard')
        elif combo == 'lizardrock':
            outcome(2,'rock','crushes','lizard')
        elif combo == 'paperspock':
            outcome(1,'paper','disproves','spock')
        elif combo == 'spockpaper':
            outcome(2,'paper','disproves','spock')
        elif combo == 'scissorslizard':
            outcome(1,'scissors','decapitates','lizard')
        elif combo == 'lizardscissors':
            outcome(2,'scissors','decapitates','lizard')
        elif combo == 'scissorsspock':
            outcome(2,'spock','smashes','scissors')
        elif combo == 'spockscissors':
            outcome(1,'spock','smashes','scissors')
        elif combo == 'paperlizard':
            outcome(2,'lizard','eats','paper')
        elif combo == 'lizardpaper':
            outcome(1,'lizard','eats','paper')
        elif combo == 'spocklizard':
            outcome(2,'lizard','poisons','spock')
        elif combo == 'lizardspock':
            outcome(1,'lizard','poisons','spock')
        elif combo == 'same':
            same()
