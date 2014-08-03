def print_hello_(name):
    print("hello {}".format(name))

#print_hello_("rob")

#print_hello_("Gordon")

#print_hello_("all")

#from random import randrange

#def roll():
    #return randrange(0,20)

#speach = roll()

#print("speach:  {:>0}".format(speach))

class player:
    health = 10
    defense = 10
    strangth = 10
    

    def __init__(self):
        self.health = 10
        self.defense = 10
        self.strangth = 10

    def take_damage(self,damage=10):
        if self.defense < 3:           
            damage *= 2
        elif self.defence > 10:
            damage /= 2
        self.health -= damage
        

class controller:
    def print_player_stats(self,player):
        print("health:    {:>2}".format(self.health))
        print("defense:   {:>2}".format(self.defense))
        print("strangth:  {:>2}".format(self.defense))

        if self.health <= 1:
            print("you are dead, you have had the life beaten out of you."
                  "GAME OVER")
       
        

player1 = player()
plater2 = player()

player1.defense = 2

print(player1.health)
player1.take_damage()
print(player1.health)
player1.take_damage(5)
print(player1.health)





