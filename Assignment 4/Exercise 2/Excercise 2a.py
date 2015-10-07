__author__ = 'Elvin Carvalho, 0907984 INFB1 RPS'

#Function check if input given is right
def checkInput(q):
    #list with correct input
    inputCorrect = ['rock', 'paper', 'scissors']

    #if input doesnt match with any item in list
    if not q in inputCorrect:
        print('No input/Wrong input given0\n\n')
        n = 'false'
    else:
        n = 'true'
    return n

#Functions with different outcomes(player that wins, winning item, correct way to say how it beats something, losing item)
def outcome(n,i1,m,i2):
    print "PLAYER %s WINS! %s %s %s.\n" %(n, i1.upper(),m.upper(), i2.upper())
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

        #if input of p1,p2 is same
        if p1 == p2:
            p1 = 'same'
            p2 = ''

        combo = p1 + p2

        #for every different outcom send different parameters to function outcome
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
        elif combo == 'same':
            same()
