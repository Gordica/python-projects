class Player:
    room = "cockpit"
    shields = "damaged"


def prompt_room(player,race):
    whichroom = input("> ")
    if whichroom == "cockpit":
        if player.shields == "fixed":
            cockpit_room(player,race)
        else:
            print("There's nothing to do here.")
            prompt_room(player,race)
                

def cockpit_room(player,race):
    if player.shields == "fixed":
        print('''you enter the shields room and see thats the shields are damaged,
you need to get them fixed before you can navigate threw the
astroid field safly to get to Darvan 2. You take a look at it and find that a
panle is bolted shut. what do you do?
''')

    else:
        player.room == "cockpit"
    answer = input("you are on a {} mining ship on your way to Darvon 2. You are"
                   " looking for a verry rare and valuable mineral named Rune."
                   " Named after the runes that had the first traces of 'magic',"
                   " but you don't believe in that stuff. Everything seems operational"
                   " in your ship. You are at a control pannel in the cockpit."
                   " Suddenly, BOOM. You feel and hear a loud crash in the ship,"
                   " there are four ship rooms, you are in one, the cockpit. There is"
                   " the engine room, the oxygen room, and the shield room. which"
                   " room do you check out? ".format(race))
    
def engine_room(player,race):
    player.room = "engines"
    if engine == "no":
        print("One of the three engines is damaged very badly. there is a"
        " box in the room that has a the words, 'engine repair tools'"
        " on it. you open it up and find three tools, a hammer, a"
        " screwdriver, and a saw. You don't have time to use test them"
        " all. Which tool do you pick? ")
        while True:
            enginechoice = input("> ")
            if engine(choice == "hammer"):
                if hammer == "yes":
                    print("You've already tried that!")
                    
                if hammer == "no":
                    print('''You take the hammer, not knowing how this will help you with the engines.
                             But when you get to the engine, you see that the reason why it wasn't working
                              was becouse some of the dabris from the exploshion is traped in the engine reactor.
                              so you use the hammer to smack some off, temperaraly fixing the engine. but it's
                              not enough, you have time to pick anouther tool to do the rest. which do you pick. Saw, or screw driver?''')
                elif enginechoice == "saw":
                    player.shields = "repairable"
                    print('''
you take the saw, who knows, maby it will work. To your surprize, you find that
the reason the engine wasn't working was becouse some dabris from the exploshion istraped in the engine reactor. so you take the saw and saw off all of the dabris you can.
                          To your surprize, this relieves strain on the engine and fixes it. It is now fully operational.
                          the otto piolet turns on and you can now navagate threw the astroid feild safly. Finaly, you
                          take the three tools, hammer, saw, and screw driver. You add them to your invintory. So now
                          that the engines are stable, what room do you go to now? oxygen room, shields room, or cockpit?
''')
                    

                    prompt_room(player,race)
                    break

                elif enginechoice == "screwdriver":
                     print('''you are almost positive that the screw driver will work. But when you get to the engines, you
                         find that there is dubris stuck in the engine reactor. there is no way to use the screw driver to repair the engines!
                         You rush back to the box to get anouther tool, but before you can do anything, one final astroid tears you ship apart!''')
                     game_over()
                     break

                else:
                    print("That isn't an option!")

def shield_room(player,race):
    player.room = "shields"
    if player.shields == "damaged":
        print("the shields are damaged, but as soon as you get in the room,"
                  " CRASH! the ship is blown apart by an astroid, and you are thrown"
                  " out into the vacume of space.")
        game_over()
    elif player.shields == "repairable":
        print("You fix the shields")
        player.shields =="fixed"
def oxygen_room(player,race):
    plater.room = "oxygen"
    if oxygen == "no":
        oxygenchoice = input("the oxygen room seams fine, no damage has been done to it."
              " Suddenly, BOOM. an astroid hits your ship and the oxygen"
              " room has a leak in the tanks! You need to get out NOW! You"
              " look around for a tool or something to get you out before you"
              " suficate. You find a pipe to  break open the locked sucurity doors,"
              " an air vent to crawl out of, and a radio to call for help,"
              " what do you do, use radio, use vent, or use pipe?")

    while True:
        if oxygenchoice == "vent":
            print('''you climb threw the air vent and find an intersection. You can eather
    go left, or right. Which way do you go?
    ''')
        
        if oxygenchoice == "pipe":
            print('''You take the pipe that you found off of the venting systems and try
    with all of your might to bust open the door. But you have no luck. You sufficate in the room.''')
                  
    game_over()
                                    

def game_over(player):
    print("GAME OVER")
    print("Continue? Y/N")
    finalanswer = input("> ")
    while True:
        if finalanswer == "y":
            if player.room == "engines":
                cockpit_room(player,race)
                break
            elif player.room == "shield":
                cockpit_room(player,race)
                break
            elif player.room == "oxygen":
                cockpit_room(player,race)

        elif finalanswer == "n":
            print("Thanks for playing!")
            break

        else:
            print()
            
            print("INVALID")
