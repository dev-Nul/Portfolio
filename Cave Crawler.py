import random
import msvcrt
import time
import sys
import traceback

#Create Dictionary of Attatched Rooms
roomIndex = {
    'Kitchen': {
        'north': 'Hall',
        },
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room'
        },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden'
        },
    'Garden': {
        'north': 'Dining Room'
        },
    }

#Create iterable index of all available directions for rooms.
directionIndex = {
    'Kitchen': {
        0: 'north',
        },
    'Hall': {
        0: 'south',
        1: 'east'
        },
    'Dining Room': {
        0: 'west',
        1: 'south'
        },
    'Garden': {
        0: 'north'
        }
    }

#Create list of items that can be picked up.
keyItems = ['sword', 'key']

#Lists where items are located.
itemSpawn = {
    'Kitchen' : ['fork', 'stove', 'key', 'plate'],
    'Hall' : ['dust', 'chair', 'table', 'goo', 'sword'],
    'Dining Room' : ['cup', 'food', 'skeleton', 'painting'],
    }

#Creates inventory.
inventory = []

#Describes all items if they are looked at.
lookDescription = {
    'fork' : "It's a rusty old fork. Not sure if I need this.",
    'stove' : "This thing has long since broken. It's stained, too!",
    'plate' : "Cracked and dirty. Looks like the last meal on it was spaghetti. Nice.",
    'dust' : "Wow awesome. That's dust.",
    'chair': "I would never trust sitting on that thing.",
    'table': "Mhmm. That's a table alright. Wow.",
    'goo' : "Disgusting and rancid. Classic monster indicator, though.",
    'cup' : "Long since emptied. I'm thirsty.",
    'food' : "Hey, I'm on a diet! I'm trying to cut my mold consumption.",
    'skeleton' : "Spooky AND scary... but it's dead.",
    'painting' : "Something about this painting is off. But then again, this whole place is.",
    'key' : "I nice way to open doors without busting them down. Maybe I should take this.",
    'sword' : "That might be good to have in such a forlorn place. I should pick it up.",
    }

#Create starting position (Kitchen)
currentRoom = 'Kitchen'

#First time in hall and Dining Room.
firstInHall = True
firstInDiningRoom = True

#Describes the current room and its attatched doorways.
def describeLocation (roomName):
    options = []
    print(f'You are currently in the {roomName}\n')
    time.sleep(2)
    if roomName == "Hall" and firstInHall == True:
        print("A chill goes down your spine. You think you see something move in the dining room.")
        print("Perhaps you should arm yourself.\n")
        time.sleep(4)
        firstInHall == False
    for i in range(0, len(directionIndex[roomName])):
        options.append(directionIndex[roomName][i])
    direction = ', '.join(options)
    print(f"You can go {direction}.\n")
    time.sleep(2)

#Lists all items in the itemSpawn for the current room.
def listItems (roomName):
    itemsCurrent = []
    for i in range(0, len(itemSpawn[roomName])):
        itemsCurrent.append(itemSpawn[roomName][i])
    itemsString = ', '.join(itemsCurrent)
    print(f"There are the following items in the room: {itemsString}.\n")
    time.sleep(3)

#Prints description of item.
def examineItem (itemName):
    print(f'You look at the {itemName}.')
    print(f'You: "{lookDescription[itemName]}"\n')
    time.sleep(4)

#Finds the room name that is the result of moving in some direction.
def goDirection(request):
    if request in roomIndex[currentRoom]:
        return roomIndex[currentRoom][request]
    else:
        print(f"ERROR. REQUEST \"{request}\" NOT FOUND IN \"roomIndex\" WHILE IN \"{currentRoom}\"")

#Converts all inventory items into a string which is returned.
def listInventory(listX):
    inventoryList = []
    for i in range(0, len(listX)):
        inventoryList.append(listX)
    string = ', '.join(inventoryList)
    return string

#Create Line
def line ():
    print('==========================\n')

#DEFUNCT.
'''
def interpretCommand():
    while True:
        print("Command: ")
        userInput = input("> ")
        try:
            formatted = (userInput.split()).lower()
            if formatted[0] == "go":
                return "go"
            elif formatted[0] == "get":
                return ""
            elif formatted[0] == "look":
                x = 0
            elif formatted[0] == "see":
                x = 0
            else:
                print("\nDidn't recognize your command. You can use \"go, get, look and see\".")
        except:
            print("Please format your command properly.\n")
'''

#Welcome Sequence
print("Welcome to Hall Crawler...")
print('==========================')
print('Commands:')
print('\t1. go [north, south, east, west] - Moves to room in x direction.')
print('\t2. get [Item] - Attempts to pick up item.')
print('\t3. examine [Item] - Describes an object.')
print('\t4. See - Lists everything in Room.')
print('\t5. Inventory - Lists what you\'re holding.')
print('==========================\n')

#OLD TESTING AREA
'''
for i in range(0, 4):
    describeLocation(currentRoom)
    listItems(currentRoom)
    examineItem("skeleton")
    line()
    if currentRoom == "Kitchen":
        currentRoom = goDirection("north")
    elif currentRoom == "Hall":
        currentRoom = goDirection("east")
    elif currentRoom == "Dining Room":
        currentRoom = goDirection("west")
'''

#Main game loop.
while True:
    line()
    #If they've won the game, break the loop.
    if currentRoom == 'Garden':
        break
    elif currentRoom == 'Dining Room':
        firstInHall = False
    #Describe room and list the items inside it.
    describeLocation(currentRoom)
    listItems(currentRoom)

    #User command loop.
    while True:
        print("Command: ")\
        #Gather user input.
        userInput = input("> ")
        print("")
        try:
            #Turns string into list with entries.
            formatted = (userInput.lower()).split()
            #If command is go and there is another word following go,
            if formatted[0] == "go" and len(formatted) != 1:
                if formatted[1] in directionIndex[currentRoom].values():
                #If the second word (direction) is in the currentRoom's available directions.)
                    if goDirection(formatted[1]) == 'Dining Room' and firstInDiningRoom == True:
                        firstInDiningRoom = False
                        currentRoom = goDirection(formatted[1])
                        print("You see a writhing mass of flesh emerge from the darkness.\n")
                        time.sleep(2)
                        #If the plaer has a sword...
                        if 'sword' in inventory:
                            #The player kills the monster.
                            print("You lift your sword in terror, then swiftly cut down the monster before you.")
                            time.sleep(3.5)
                            print("The monster falls to the floor, burning alive until only a skeleton remains.\n")
                            time.sleep(3.5)
                        #If the player does not have a sword...
                        elif 'sword' not in inventory:
                            #The player is killed by the monster.
                            print("You can hardly let out a scream before the monster descends on you.")
                            time.sleep(2.5)
                            print("With no way of protecting yourself, you accept your fate.\n")
                            time.sleep(2.5)
                            line()
                            print("GAME OVER...")
                            time.sleep(1)

                            #Identical to ending of program.
                            print("Press any key to exit...")
                            stop = msvcrt.getch()
                            sys.exit()
                        else:
                            print("A game-breaking error has occured.")
                        break
                    #If the user is attempting to go to the garden...
                    elif goDirection(formatted[1]) == 'Garden':
                        print("You approach the locked door...\n")
                        time.sleep(2)
                        #If the user has a key...
                        if 'key' in inventory:
                            #The user exits the house into the garden.
                            print("The key from the kitchen slots perfectly into the door.")
                            time.sleep(2)
                            print("Within seconds the door is wide open.")
                            time.sleep(2)
                        elif 'key' not in inventory:
                            #The user is rejected from going further.
                            print("You go for the handle but notice quickly that the door is locked.")
                            time.sleep(3)
                            print("Maybe if you had a key from an earlier room you could open the door?\n")
                            time.sleep(3)
                            continue
                        else:
                            print("A game breaking error has occured.")
                    #Change current room to other specified room.
                    currentRoom = goDirection(formatted[1])
                    print("You shuffle through the doorway.\n")
                    break
                else:
                    print("")
                    print("You try to go that way, but walk straight into the wall.\n")
                    time.sleep(2.5)
            #If command is get and there is another word following get,            
            elif formatted[0] == "get" and len(formatted) != 1:
                #If the word following get is an item found in the current room, and can be picked up,
                if formatted[1] in itemSpawn[currentRoom] and formatted[1] in keyItems:
                    #Add item to inventory
                    inventory.append(formatted[1])
                    #Remove item off floor.
                    itemSpawn[currentRoom].remove(formatted[1])
                    print(f"You have picked up the {formatted[1]}!\n")
                    time.sleep(2)
                #If the item is in the room (but not in key items).
                elif formatted[1] in itemSpawn[currentRoom]:
                    #Create a random integer from 0 - 4, then use one of the responses.
                    integer = random.randint(0, 4)
                    if integer == 0:
                        print(f"You don't think that {formatted[1]} will come in handy.")
                    elif integer == 1:
                        print(f"You: \"I don't think I need that...\"")
                    elif integer == 2:
                        print("Just before you grab it, you realize that you dont need it.")
                    elif integer == 3:
                        print("You: \"Useless junk. Not sure if I need it.\"")
                    elif integer == 4:
                        print("You pause, wondering why on earth you would ever need that.")
                    time.sleep(2)
                    print("")
                #If user inputs an item that doesn't exist.
                else:
                    print("You look around the room and have no idea what you're looking for.\n")
            #If command is look and there is a word following look,
            elif formatted[0] == "examine" and len(formatted) != 1:
                #If item is in current room,
                if formatted[1] in itemSpawn[currentRoom]:
                    #Look and describe item.
                    print("You decide to take a closer look...\n")
                    examineItem(formatted[1])
                #If user tries to examine something that doesn't exsist.
                else:
                    print(f"You look around for the room for the {formatted[1]} but don't see it.")
            #If the only command is "see"
            elif formatted[0] == "see" and len(formatted) == 1:
                #Describe the room again.
                print("You look around the room again...\n")
                describeLocation(currentRoom)
                listItems(currentRoom)
            #If command doesn't exist, tell user.
            elif formatted[0] == "inventory" and len(formatted) == 1:
                #If the user has nothing in their inventory,
                if len(inventory) == 0:
                    print("You currently have nothing in your inventory!")
                #If the user only has one item in their inventory,
                elif len(inventory) == 1:
                    print(f"You have a {inventory[0]} in your inventory.")
                #If the user has more than one thing in their inventory.
                else:
                    print(f"Here are the following things in your inventory:\n{listInventory(inventory)}")
                time.sleep(3)
                print("")
            elif formatted[0] == "bypass" and len(formatted) == 1:
                print("Look at you, cheating the game...")
                time.sleep(3)
            #If an unknown command is entered or a user mistypes.
            else:
                print("\nYou're an expert at confusing yourself.")
                print("Did you type the right command?")
                continue
        #If error, tell user to type in their command again.
        except Exception as ex:
            print("\nYou feel confused.")
            print("Did you enter the right command or input the right direction/item?\n")

#Ending Text
print("You step out of the house, leaving the horrors inside behind you.")
time.sleep(3)
print("You're free!")
time.sleep(2)

print("")
line()

print("You've completed the game!")
#Once game is complete, ask user to press any key to exit then exits.
#getch() only works in terminal.
print("Press any key to exit...")
stop = msvcrt.getch()
sys.exit()
