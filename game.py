# GAME CONTEXT
# FIRST SCENARIO.
bad_ending: False


scenario_1 = print("\nYou are on the way to your vacations. Suddenly, your airplane starts to fall and you got faint. \
You woke \nup at the shore of an island, apparently you are the only survivor.")
print("\nYou start thinking about how to survive. You can wait for someone to come and help you or \
you can start \nlooking for a refuge, food, water and fire to survive.")

decision_1 = input("\nWhat should you do? WAIT or EXPLORE. ")

if decision_1.upper() == "EXPLORE":
    print("\nYou entered to the island and a wild animal attacked you and unfortunately you died.")
    bad_ending = True

if decision_1.upper() == "WAIT":
    print("\nYou decide to wait for help.You see some baggages at the shore of the \
island and you start checking inside for something useful while you are waiting \
for help.You just find one water bottle and two granola bars.")

# SECOND SCENARIO
    scenario_2 = print("\nWith all the stuff you got from the baggages you will only have one more day of life. \
You noticed you will \nhave to explore the island looking for some food if you want to survive, \
but you meditate about the risks \nof exploring the island without a weapon.")

    decision_2 = input("\nWill you STAY or LOOK into the island? ") 

    if decision_2.upper() == "STAY":
        print("\nYou never received help. You died because lack of food.")
        bad_ending = True

    if decision_2.upper() == "LOOK":
        print("\nYou made a knife with a branch and a rest of the plane and entered to the island.")

# THIRD SCENARIO
        scenario_3 = print("\nAfter 30 minutes walking. You see a boat near to the island but \
while you continue walking you \nnotice a guy that is not too far from the boat. You can RUN AWAY in the boat; TALK with the guy or SPY \non him to see if he is a good person. ")

        decision_3 = input("\nWhat are you gonna do? ")

        if decision_3.upper() == "RUN AWAY":
            print("\nYou decide to run and steal the boat. After reaching the open sea, you\
 calm yourself and notice that there is no food inside the boat. You are not able to\
 return because you don't now where you are exactly. After \nhours you got faint due the high dehydration.")
            bad_ending = True

        if decision_3.upper() == "TALK":
            print("\nYou take the determination to talk with the guy. \
He unexpectedly responds kindly to you and he takes you to his refuge and \
introduces you to his friends. Everyone successfully escape.")
            bad_ending = False

        if decision_3.upper() == "SPY":
            print("\nWhile you are spying on the guy, you got faint due to hunger \
and thirst. When you wake up a few hours later you try to find the shelter but you can't.")
            bad_ending = True



# END OF THE GAME
if bad_ending:
    print("\nGAME OVER\n")

if not bad_ending:
    print("\nCONGRATULATIONS, YOU ESCAPE FROM THE ISLAND SAFELY!!\n")
