#cherry game simulation
#Young

import random


spinnerChoice = [-1,-2,-3,-4,2,2,10]

#cherryOnTree = spinResult + cherryOnTree # cherryOnTree += spinResult


turnToWin = []
for i in range(100):
    turns = 0
    cherryOnTree = 10
    while cherryOnTree > 0:
        spinIndex = random.randrange(0,len(spinnerChoice))
        spinResult = spinnerChoice[spinIndex]
        #print "you spun", spinResult
        cherryOnTree = spinResult + cherryOnTree # cherryOnTree += spinResult
        
        if cherryOnTree > 10:
            cherryOnTree = 10
        elif cherryOnTree < 0:
            cherryOnTree = 0
    #    print "you now have %d on  your tree" %(cherryOnTree)
        #print "you now have ", cherryOnTree, "cherries on your tree."
        turns += 1
        #print "you spun ", turns, "times."
    turnToWin.append(turns)
print turnToWin
print "It took average", sum(turnToWin)/len(turnToWin), "times to win the game out of 100 games."

    