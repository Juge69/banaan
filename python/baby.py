import time

opt1 = input("hai my love, do you want to play a game with me? (yes) or (no): ")
if opt1 == "yes":
    print("Yay! Let's play!")
else:
    print("Okay, maybe next time!")
    exit()

time.sleep(2)
print("you are lost in a town called woudenberg, you need to find your way to my house to give you a big hug :D")
time.sleep(2)
print("you can go north, south, east or west")
time.sleep(2)

directionChoise = input("which direction do you want to go?: ")
if directionChoise == "north":
    print("you find a river and decide to follow it")
    time.sleep(2)
    print("after a while you find a bridge and cross it")
    time.sleep(2)
    print("Suprise! you find a village on the other side")
    time.sleep(2)
    print("you can stock up on supplies and rest here")
    time.sleep(2)
elif directionChoise == "south":
    print("you find a cave and decide to explore it")
    time.sleep(2)
    print("inside the cave you find a treasure chest")
    time.sleep(2)
    print("you open the chest and find gold coins and jewels")
    time.sleep(2)
    print("you can take some treasure and leave the cave")
    time.sleep(2)
elif directionChoise == "east":
    print("you find a path leading to a mountain")
    time.sleep(2)
    print("you climb the mountain and reach the top")
    time.sleep(2)
    print("from the top you can see the whole forest")
    time.sleep(2)
    print("you can take a moment to enjoy the view")
    time.sleep(2)
elif directionChoise == "west":
    print("you find a path leading to a waterfall")
    time.sleep(2)
    print("you follow the path and reach the waterfall")
    time.sleep(2)
    print("you can take a swim in the pool below the waterfall")
    time.sleep(2)
    print("after swimming you feel refreshed and ready to continue your journey")
    time.sleep(2)

finalchoise = input("You feel like you are almost there, dont give up now baby! do you want to go left or right? ")

if finalchoise == "left":
    print("You walk for a while and find a small hut")
    time.sleep(2)
    print("You knock on the door and an old lady opens it")
    time.sleep(2)
    print("She invites you in and offers you some food and drink")
    time.sleep(2)
    print("After resting for a while, you thank her and continue your journey")
    time.sleep(2)
    print("After walking for a while, you see a road in the distance and decide to follow it")
    time.sleep(2)
    print("you follow the road and after a while you see a house in the distance")

elif finalchoise == "right":
    print("You decide to go right and walk for a while")
    time.sleep(2)
    print("You see a road in the distance and decide to follow it")
    time.sleep(2)
    print("you follow the road and after a while you see a house in the distance")

housechoise = input("You see the house, do you want to go to the door or look for another way in? (door) or (another way): ")
if housechoise == "door":
    print("You walk to the door and knock")
    time.sleep(2)
    print("The door opens and you see me standing there with open arms")
    time.sleep(2)
    print("I give you a big hug and we live happily ever after :D")

elif housechoise == "another way":
    print("You decide to look for another way in")
    time.sleep(2)
    print("You walk around the house and find a window that is slightly open")
    time.sleep(2)
    print("You carefully climb through the window and find yourself in the living room")
    time.sleep(2)
    print("I am sitting on the couch and look up as you enter")
    time.sleep(2)
    print("I give you a big hug and we live happily ever after :D")
    time.sleep(2)

time.sleep(2)
print("Thank you for playing my game, I hope you had fun! :)")
time.sleep(2)
print("Goodbye my love, see you soon! <3")
time.sleep(2)
print("Mwahh :D")
exit()