print("test")

def living_room(self):
    move = input("You're in the living room.\n" +
    "Where would you like to move next? " 
    if move == "q":
        break 
    elif move == "north":
        dining_room()
    elif move == "east":  
        theater() 
    elif move == "south":
        front_porch()
    elif move == "west":  
        garage()
    else:  
        print("Invalid input!")
        living_room()
