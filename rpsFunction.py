
def RPS(number):
    import random
    option = ["R","P","S"] #each computers' option
    comp1_wins = [] #lists to append the results of each game depending on the results
    comp2_wins = []
    ties = []
    for i in range(number): #iterates 100 games
        comp1_index = random.randrange(0,len(option)) #random choice index position for computer 1
        comp1_choice = option[comp1_index] #actual value of the random choice index position for computer 1
        comp2_index = random.randrange(0,len(option))
        comp2_choice = option[comp2_index]
        if (comp1_choice == "R" and comp2_choice == "S") or \
           (comp1_choice == "S" and comp2_choice == "P") or \
           (comp1_choice == "P" and comp2_choice == "R"): #cases where computer 1 would win
            comp1_wins.append(1) #appends to computer 1 wins list
        elif (comp2_choice =="R" and comp1_choice == "S") or \
             (comp2_choice == "S" and comp1_choice == "P") or \
             (comp2_choice == "P" and comp1_choice == "R"): #cases where computer 2 wins
            comp2_wins.append(1)
        else:
            ties.append(1)
    print "Computer 1 won",sum(comp1_wins),"games, Computer 2 won",sum(comp2_wins),"games.\nThe draw game percentage out of 100 games is",sum(ties),"%."
    return sum(ties)

RPS(100)


import sys
print sys.path[0]