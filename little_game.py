import random

#stats
health = 30
sanity = 100
happiness = 100



#items
shield = False





def start_game():
    print("Welcome to a little adventure game.")
    print("you find yourself in a dark forest with paths going in directions: North, East, South, West.")
def start():
    choice = input("Which way do you go? (north, east, south, west: ").lower()
    if choice == "north":
        cave()
    elif choice == "east":
        town()
    elif choice == "west":
        monster()
    else:
        print("you stayed in the same spot for the rest on time.")
        game_over()



def cave():
    crossroad = input("you enter the cave to find a crossroad, which way do you go? (left/right/leave)").lower()
    if crossroad == "left":
        print("you find a chest with an unknown lock with 2 keys next to it, theres a note that says: 'ONE OF THESE KEYS WILL DESTROY THE CHEST AND YOU, AND ONE WILL OPEN IT, CHOOSE WISELY.")
        key = input("do you use the left or right key? (left/right)")
        if key == "left":
            decition = input("you open the chest and you find a shield, do you take it? (yes/no)").lower()
            if decition == "no":
                print("you leave the shield")
                cave()
            elif decition == "yes":
                "you take the shield."
                cave()
                shield = True
        else:
            print("you have destroyed the chest")
            cave()
            shield = False
    elif crossroad == "right":
        print("you enter a room with no other exit")
        cave()
    else:
        print("you leave the cave.")
        start()

def town():
    print("you have found a town, next to the road it has a sign that says Amsterdam.")
    crossroad = input("you can go one of three buildings, which do you choose? (house1/church/house2")
    if crossroad == "house1":
        print("you try to enter the house but iy seems to be lock.")
        town()
    elif crossroad == "church":
        print("you enter the church to find out that there is a funeral service going on, you feel bad and decide to leave.")
        town()




















def game_over():
    print("GAME OVER better thanks for playing")
    play_again = input("do you want to play again? (yes/no").lower()
    if play_again == "yes":
        start_game()
    else:
        print("Goodbye")

start_game()