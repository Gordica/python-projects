from adventurebehindthescenes import *

name = input("What is your character's name? ")
print("Hi {}.".format(name))
age = input("what is your age?")
age = int(age)

if age <= 13:
    print("ummm... are you a little to young to be going on a dangerous and posibly horrable and epic adventure?")
elif age >= 60:
    print("I think this adventure is a little to harsh for someone of your age but ok.")
else:
    print("sounds like a reasonable age.")

while True:
    race = input("What is your race?: Human, Avian, Drakon, or Terren? ")

    if race == "Human":
        print("You picked Human, the race of Earth, not much more to say.")
        break
    elif race == "Avian":
        print("You picked Avian, The Avians are an advanced, old, galactic race."
              " Evolved from a bird like creature, the Avians get their energy from"
              " crystals harvested from their home planet, Avoc. Although not as"
              " smart as humans, Avians are a force to be recognized.")
        break
    elif race == "Drakon":
        print("You picked Drakon, the Drakons are a bold, dragon/human like race."
              " Many discriminate againsed them, but the Drakon don't care much,"
              " with thick scales and amazing physical abilities, the Drakons are"
              " an amazing, powerful force.")
        break
    elif race == "Terren":
        print("you picked Terren, Terren are humans but are smarter than the avrage"
              " human. Broken off from the human race, terren are verry advanced and"
              " have a mazing machings and weapons of great power.")
        break
    else:
        print("that is not a pickable race.")
        
while True:
    cockpit_room(Player)

    if answer == ("Engine room"):
        engine_room(Player)
        break
    
    elif answer == ("Shield room"):
        shield_room(Player)
        break
        
    elif answer == ("Oxygen room"):
        oxygen_room(Player)
        break

    else:
        print("you can't go to that room.")
        print("you can't go to that room.")
