from random import randint

def supplies():
    supplies = raw_input("Do you bring the magic potion or poison?")
    
    if supplies == "potion" or supplies == "poison":
        print "Princess " + name + " will bring the " + supplies
        return str(supplies)
    elif supplies != "poison" or supplies != "potion":
        print "Sorry! You have to type potion or poison in lowercase."

def direction_fork():
    if direction == "right" and supplies == "potion":
        print "You have arrived at the Fairy Forest - what a magical, mysterious place! The fairies will give you advice in excange for the magic potion.  They tell you to continue through their dark and mysterious forest until you arrive at the Unicorn Clearing."
    elif direction == "right" and supplies == "poison":
        print "You have arrived at the Fairy Forest, but the fairies do not want your poison...In fact, they want you to leave! The fairies send you out of the magic forest with a wave of their wands...Unfortunately, their magic was too strong, and you died. "
    elif direction == "left" and supplies == "potion":
        print "You have entered the Ogre Swamp.  Oh no! You have chosen the wrong supply! You can't defend yourself against the Ogre without poison. The Ogre will kill princess " + str(name) + " now. "
    elif direction == "left" and supplies == "poison":
        print "You have entered the Ogre Swamp. You poured the poison on the Ogre and have defeted him. He falls to the ground, writhing in pain as the posion stings and burns his slimey, green skin. Congratulations, Princess " + str(name) + "!"
#if direction == "left" and supplies == "posion":
#alligator_fight(direction, supplies)
def alligator_fight(direction, supplies):
    if direction == "left" and supplies == "poison":
        print "You have the supplies you need!"
        print "Now, an alligator attacks!"
        
        alligator_num = randint(0,11)
        guess_num = int(raw_input("Pick a number between 1 and 10 to see if you defeat the alligator!  "))
        while guess_num != alligator_num:
            guess_num = int(raw_input("Uh, oh!  He looks angry!  Guess again, quickly!!  "))
            print "Your new guess is:  " + str(guess_num)
        else:
            print "You have chosen wisely.  You are not alligator food today."
    elif direction == "right" and supplies == "potion":
        print "You leave the fairies safely and move on."
    else:
        print "You have the wrong supplies for your journey, and you meet your doom!"
    return direction, supplies
#if direction == "right" and supplies == "potion":
#unicorn_ride(guess)
#if direction == "right" and supplies == "potion":
#unicorn()
def unicorn():
    print "As you stumble through the forest, you arrive at a clearing.  HAZAR! A dozen bright, shiny unicorns lay in the grass, munching flowers. Following the Fairies' advice, you begin to attempt to get on the unicorn.  You have 3 chances to get on the unicorn in the correct fashion... but be careful! The unicorn might stab you with its horn if you try to get on it the wrong way."
    guess = raw_input("Choose a number between 1 and 10. Your number will determine whether you can successfully ride the unicorn out of the forest. Your number:")
#unicorn()
def unicorn_ride(guess):
    for i in range(3):
        if guess == 5 or guess == 9:
            print "Good job - you have ascended the unicorn from the left!"
            break
        elif guess == 3 or guess == 7:
            print "You have been impaled by the unicorn - ouchie. Game over."
            break
        elif guess == 2 or guess == 6:
            print "You have barely managed to get on the unicorn from the right side.  Alright, time to fly!"
            break
        else:
            if i < 2:
                guess = int(raw_input("You missed - try again! "))
                print "Your new guess is:  " + str(guess)
            else:
                print "You are out of guesses.  You wander around the forest, eventually getting lost. You die of starvation. Or exposure. Or both."
    return guess
#unicorn_ride(guess)
def stuck_in_cave():
    if direction == "left" and supplies == "poison":
        return "As you leave the swamp, the mushy land gives way to a grassy forest.  The ground is uneven; you stumble up and down. Oh no! You have twisted your ankle and fallen into a hole!  You struggle to stand, but realize you are only falling deeper into the ditch. Princess " + str(name) + " is stuck in a cave."
    elif direction == "right" and supplies == "potion":
        return "As the unicorn flaps its wings, you admire the rolling hills and forested areas that unfold underneath you.  Clouds and mist swish past you, creating a hazy smog. Soon, the unicorn begins to descend, and you find yourself landing in amongst tall, imposing oak trees.  You hop off the unicorn and give it a pat on its neck as it leaves. Once again, Princess " + str(name) + " is alone - but have no fear! You walk throught the forest, weaving through trees and over knotted roots... Oh no! You have twisted your ankle on a root, and you have fallen into a deep hole! Princess " + str(name) + " struggles to stand up and climb out, but she soon realized that she is stuck in a cave."
# Call function
def cave():
    if escape_cave == "right":
        if action == "sword":
            print "Uh oh! You swing the sword, but the bats are quicker and they sink their teeth into you, leaving you laying in a bloody mess. Princess " + str(name) + " dies."
        elif action == "sneak":
            print "You quietly crouch on all fours and crawl under the bats, safely making it out of the cave. Congrats! Once outside of the cave, you follow a dirt path to a giant, magnificent castle."
        elif action != "sword" or action != "sneak":
            print "Sorry! You must type 'sword' or 'sneak'"
    elif escape_cave == "left":
        print "You wander to the left of the cave, stepping over rocks and mud.  It's pitch black!"

# call function
def cave_cont(escape_cave, direction_cave):
    if escape_cave == "right":
        print ' '
    elif direction_cave == "left":
        print "Oh no! You wander around in the cave aimlessly, slowly panicking as you seem to get more and more lost. Princess " + str(name) + " dies of claustrophobia. Yikes!"
    elif direction_cave == "right":
        print "HAZAR! You wander through the cave for a while, and soon you see a light. You follow the light out of the cave, and find yourself in a beatiful field full of flowers.  After wandering through the field, you spot a magnificent castle...THE CASTLE OF PRINCE ERIC!!"
    elif direction_cave != "right" or direction_cave != "left":
        print "Uh-oh...Looks like you didn't type 'right' or 'left'"

#if direction_cave == "right" or action == "sneak":
#dragon()
def dragon():
    bucket = raw_input("Which bucket will you choose?")
    if bucket == '1':
        print "WOOT-WOOT! You have chosen the magic, dragon-fighting sword! GO FIGHT THAT DRAGON!"
    elif bucket == '2':
        print "Nice! You picked the magic shield.  Although you will have a tough battle without a dragon-proof sword, your special shield should hold up. GOOD LUCK FIGHTING THAT DRAGON!"
    elif bucket == '3':
        print "Uh-oh...looks like you picked a stick... I don't know how you are going to beat the dragon with a stick!"
    else:
        print 'um'

#if bucket == "1" or bucket == "2":
    #rock_paper_scissors(player, computer)
def rock_paper_scissors():
    print "You must play the dragon in rock, paper, scissors in order to get a good swipe at its head. A tied round does not count as a play, however whichever player wins best out of 3 plays will ultimately become the winner."
    t = ["rock", "paper", "scissors"]
    computer = t[randint(0,2)]
    player = raw_input("Do you choose rock, paper, or scissors?")
    plays = 0
    wins = 0
    while plays <= 2 or wins <= 1:
        print "Dragon guess: " + computer
        print "Your guess:" + str(player)
            #print "Number of plays:" + str(plays)
            #print "Princess " + str(name) + "'s wins:" + str(wins)
        if player.lower() != "rock" and player.lower() != "paper" and player.lower() != "scissors":
            print "Uh-oh! Looks like something went awry. Check to make sure you typed rock, paper, or scissors."
            player = raw_input("Try again! ")
        elif player.lower() == computer:
            computer = t[randint(0,2)]
            print "You tied the dragon!"  
            player = raw_input("Play again! Rock, paper, or scissors?")
    
        else:
            if player.lower() == "rock" and computer == "paper":
                computer = t[randint(0,2)]
                plays += 1
                print "Uh-oh! The dragon won!."
                print "Number of plays: " + str(plays)
                print "Number of Princess " + str(name) + "'s wins: " + str(wins)
                player = raw_input("Play again! Rock, paper, or scissors?")
            elif player.lower() == "paper" and computer == "scissors":
                computer = t[randint(0,2)]
                plays += 1
                print "Uh-oh! The dragon won!."
                player = raw_input("Play again! Rock, paper, or scissors?")
                print "Number of plays: " + str(plays)
                print "Number of Princess " + str(name) + "'s wins: " + str(wins)
            elif player.lower() == "scissors" and computer == "rock":
                computer = t[randint(0,2)]
                plays += 1
                print "Uh-oh! The dragon won!"
                player = raw_input("Play again! Rock, paper, or scissors?")
                print "Number of plays: " + str(plays)
                print "Number of Princess " + str(name) + "'s wins: " + str(wins)
            else: # iterate plays and wins each time
                if player.lower() == "scissors" and computer == "paper":
                    computer = t[randint(0,2)]
                    plays += 1
                    wins += 1
                    print "Yay! You won."
                    print "Number of plays: " + str(plays)
                    print "Princess " + str(name) + " has " + str(wins) + " win(s)."
                    print "Number of Princess " + str(name) + "'s wins: " + str(wins)
                    if wins <= 0 and plays <= 1:
                         player = raw_input("Play again! Rock, paper, or scissors?")
                elif player.lower() == "paper" and computer == "rock":
                    computer = t[randint(0,2)]
                    plays += 1
                    wins += 1
                    print "Yay! You won."
                    print "Number of plays: " + str(plays)
                    print "Princess " + str(name) + " has " + str(wins) + " win(s)."
                    if wins <= 0 and plays <= 1:
                         player = raw_input("Play again! Rock, paper, or scissors?")
                elif player.lower() == "rock" and computer == "scissors":
                    computer = t[randint(0,2)]
                    plays += 1
                    wins += 1
                    print "Yay! You won."
                    print "Number of plays: " + str(plays)
                    print "Princess " + str(name) + " has " + str(wins) + " win(s)."
                    if wins <= 0 and plays <= 1:
                         player = raw_input("Play again! Rock, paper, or scissors?")
            if plays == 2 and wins < 1:
                print "Uh-oh...Looks like the dragon has won best out of 3!"
                break
            elif wins == 2:
                print "Yay! You beat the dragon, best out of 3!" 
                break
#if bucket == "3":
#bucket_depend()
def bucket_depend():
    if bucket == "3":
        print "Well, since you chose the bucket with a stick...RUN!!!"
    else:
        print ' '




def run_away(bucket, unicorn):
    if bucket == "3":
        print "As you run, you make your way towards the Fairy Forest to the left. The dragon roars, and leaps into the air to begin following you.  It breathes fire, missing your hair by inches - lucky! As you stumble into the forest, you find yourself back in the unicorn clearing."
    guess = raw_input("Choose a number between 1 and 10. Your number will determine whether you can successfully ride the unicorn out of the forest. Your number:")
def unicorn_ride2(guess):
    for i in range(3):
        if guess == 5 or guess == 9:
            print "Good job - you have ascended the unicorn from the left! The unicorn begins to flap its wings, and you are flying out of the forest with an angry dragon in hot pursuit.  The unicorn is barely faster than the angry dragon, and you direct it towards the castle in the distance.  As you approach, the dragon roars fire, but your unicorn dodges. Squinting your eyes, you see the prince jumping up and down, waving his arms from the tallest tower.  You zoom down to the tower, your stomach dropping with the sharp descent, and grab Prince Eric's hand. HURRRAYYY!!! You have the prince!! The unicorn flies faster and faster away from the dragon, which is beginning to slow as it recognizes defeat. CONGRATULATIONS, YOU HAVE COMPLETED YOUR QUEST!"
            break
        elif guess == 3 or guess == 7:
            print "Good job - you have ascended the unicorn from the left! The unicorn begins to flap its wings, and you are flying out of the forest with an angry dragon in hot pursuit.  The unicorn is barely faster than the angry dragon, and you direct it towards the castle in the distance.  As you approach, the dragon roars fire, but your unicorn dodges. Squinting your eyes, you see the prince jumping up and down, waving his arms from the tallest tower.  You zoom down to the tower, your stomach dropping with the sharp descent, and grab Prince Eric's hand. HURRRAYYY!!! You have the prince!! The unicorn flies faster and faster away from the dragon, which is beginning to slow as it recognizes defeat. CONGRATULATIONS, YOU HAVE COMPLETED YOUR QUEST!"
            break
        elif guess == 2 or guess == 6:
            print
            break
        else:
            if i < 2:
                guess = int(raw_input("You missed - try again! "))
                print "Your new guess is:  " + str(guess)
            else:
                print "You are out of guesses. The dragon zooms down from the clouds, and gobbles you up. Ouchie."
    return guess
#calling all the functions
name = raw_input("What is your princess name?")
print "You are princess " + str(name) + ", and you are given the task to save Prince Eric from the EVIL DRAGON. Along the way you will encounter DANGEROUS challenges. GOOD LUCK!"
print "As you prepare for your journey, you have to decide what to bring.  In your closet, there is a sword, which you grab right away.  You have one pocket, and you can choose to fill it with potion or poison."
supplies()
print "Great! Now you are ready to begin.  Once you walk outside, you are met with a fork in the road."
direction = raw_input("Do you go right or left at the fork in the road?")
print "Princess " + str(name) + " will go " + str(direction) + "."
direction_fork()
if direction == "right" and supplies == "potion":
    print "As you leave the Ogre's dead body, you make your way through the swamp, stepping through mushy mud and oozing piles of gunk. The smell was awful, but Princess " + str(name) + " kept moving. Soon, you arrive at a deep part of the swamp... An alligator jumps out! It smiles at you, flashing its gnarly teeth. 'If you want to pass my swamp, you must guess my number correctly.  Otherwise...Let's just say I haven't eaten in a while!'"
if direction == "left" and supplies == "posion":
    alligator_fight(direction, supplies)
if direction == "right" and supplies == "potion":
    unicorn()
if direction == "right" and supplies == "potion":
    unicorn_ride(guess)
stuck_in_cave()
escape_cave = raw_input("Will you choose to go right or left in the dark cave?")
if escape_cave == "right":
    print "You turn right and agitate a swarm of bats! As they swoop around in a frenzy, you must choose to either swing your sword at them or stealthily creep out."
    action = raw_input("Do you choose sword or sneak?")
cave()
if escape_cave == "left":
    direction_cave =raw_input("After you wander for a while, you find yourself at wall. It is dark and you can hardly see anything...Right or left?")
cave_cont(escape_cave, direction_cave)
if direction_cave == "right" or action == "sneak":
    print "Once you arrive at the castle, you come face to face with a massive, red dragon. Its              scales reflect sunlight and shine in yours as it flies down to meet you. It has massive, black claws that pierce the earth as it sits in front of you, barring your path. It roars, and you duck you head avoid its hot, putrid breath. 'Princess " + str(name) + ", I see you have arrived. In order to retrieve Prince Eric, you must pass me. Because I am so big and strong, I could kill you in an instant.  In order to make this little game more interesting, I will let you choose between 3 buckets. One bucket has a sword strong enough to pierce my scales, one bucket has a shield that can block my fire, and the other has a measly stick from the forest. You must choose one bucket, and you will not know what is inside the bucket you choose.  The buckets are numbered 1, 2 and 3.' With that, the dragon gave a sly smile, flashing rows and rows of pearly daggers. It presented 3 wooden buckets, and set them in front of Princess " + str(name) + " and crossed its arms, flapping its      wings while it waited."
dragon()
if bucket == "1" or bucket == "2":
    print "Now that you have picked your weapon, you must fight the dragon! Beat the dragon in rock paper scissors in order to STAB IT IN THE FACE!"
if bucket == "1" or bucket == "2":
    rock_paper_scissors()
if bucket == "3":
    bucket_depend()
if bucket == "3":
    run_away(bucket, unicorn)
    unicorn_ride2(guess)



