__author__ = 'Raziel'

import random

print ("Welcome Hero! \nWe have waited for so long for you to come and vanquish "
       "the \nincredibly annoying, irksome, and noisome menace known as TOM CRUISE!!!")
hero = input("What is your name fell hero?\n> ")
print ("Hello",hero,"it is a great pleasure to meet you!"
                      "\nIt is your mission, your doom, to defeat Tom.")
print ("In order to defeat him you must bring his Thetan level down to zero. \nHis Thetan level is currently 666 which "
       "means that he is almost at *Cleared Theta Clear*, \nan unstoppable godlike state! This is why you must KILL TOM NOW!")
xxx = input("Do you understand?\n> ")
print ("Good! Btw, your current Thetan level is 100, which doesn't mean much in the real world, "
       "\nbut if Tom gets your Thetan level down to zero your will lose all will to live \nand probably join the scientology cult."
       " OH NO, here he comes now!!!\n")
print ("Tom is looking up at you angrily. He may be short and have bad hair but he is fierce!")

hero_h = 100
tom_h = 666
turn = 1
tomdam = 0
herodam = 0
defend = 0


while (hero_h > 0 and tom_h > 0):
    while turn == 1:
        action = input("\nWhat will you do?"
                           "\nBOX: Box Tom's Face."
                           "\nPHOTO: Release an embarrasing photo of Tom that your friend took last week."
                           "\nKICK: Kick Tom right in the Gonads."
                           "\nBLOCK: Prepare to defend yourself from Tom's attack.\n> ")

        if action == "BOX":
                tomdam = random.randint(99,199)
                print ("You Box Tom's face and decrease his Thetans by ", tomdam,". AWESOME!")
        elif action == "PHOTO":
                tomdam = random.randint(30,300)
                print ("You embarass Tom and decrease his Thetans by ", tomdam,". AWESOME!")
        elif action == "KICK":
                tomdam = 0
                print ("You kick Tom dead in the balls but this has no effect!!!")
        elif action == "BLOCK":
                tomdam = 0
                defend = 1
                print ("You prepare to defend yourself.")

        else:
            action = input("Tom doesn't recognize this action. PRESS ENTER\n")
            break


        tom_h = tom_h - tomdam
        turn = 2

    else:
        if defend == 1:
            print ("Tom tries to hit you but you are too tricky for him!")
            defend = 0
            turn = 1
            continue

        else: attack = random.randint(1,3)

        if attack == 1:
            herodam = random.randint(1,10)
            print ("\nTom trips you!\n He decreases your Thetans by ", herodam,".")
        elif attack == 2:
            herodam = random.randint(1,20)
            print ("\nTom uses his superior vocal chords to unleash a sonic assault (aka a screaming fit)!"
                   "\n He decreases your Thetans by ", herodam,".")
        elif attack == 3:
            herodam = random.randint(10,39)
            print ("\nTom hovers a foot off of the ground and red lazers shoot at you from his eyes!"
                   "\n He decreases your Thetans by ", herodam,".")

        hero_h = hero_h - herodam
        turn = 1


if tom_h <= 0:
    print ("After his last attack Tom collapses! \nYou have defeated Tom Cruise! You are a great hero indeed! \nNow that Tom is gone we will sack all "
           "churches of scientology and recover all of the money they swindled from their members. \nWe will send you check "
           "in the mail.\n\n THE END!")
elif hero_h <= 0:
    print ("Tom has defeated you! You are totally demoralized and will join the church of scientology. "
           "\nYou will sign a billion year contract and give them all of your money. Also we are all DOOMED."
           "\n Thanks for nothing!")