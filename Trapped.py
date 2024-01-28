print ("Type a direction from the exit options to move in that direction.\nType take to grab an item from the room.\nType fight, to fight an entity.\n" )



rooms = {
    'living room': {
        'description': "It's a grand living room with a huge TV, a fireplace beneath it, and an ostrich leather sofa with a rug made of the finest wool. If you have the key go west.",
        'exits': {"north": "kitchen", "east": "library", "west": "bedroom"}
    },

    'kitchen': {
        'description': "The kitchen is filled with crockery. You notice Ming crockery on one of the shelves. You also spot gold cutlery on the marble cooking surface.",
        'exits': {"south": "living room"}
    },

    'library': {
        'description': "The library is empty except for a book on the librarian's desk. You spot a CD jutting out from the middle of the book.",
        'exits': {"north": "office", "west": "living room"},
        'items': {"cd": 'Text that is written on the CD reads DO NOT OPEN.'}
    },

    'office': {
        'description': "The office is messy. There are loose papers everywhere. In the middle of the mess, you spot a computer and a CD player port in it. You pop in the CD, and a video plays. A mysterious figure appears and says one sentence. Behind the mirror. The video abruptly ends.",
        'exits': {"south": "library", "west": "master bedroom"}
    },

    'master bedroom': {
        'description': "The master bedroom is majestic. A king-sized bed with a down feather duvet.",
        'exits': {"south": "bathroom", "east": "office"}
    },

    'bathroom': {
        'description': "The bathroom's flooring and walls are made of white marble. The washbasin and the mirror's frame are made of gold. The mirror! You prise open the mirror and find a secret tunnel pathway.",
        'exits': {"north": "master bedroom", "west": "passage"}
    },

    'passage': {
        'description': "The passage turns north. You have no choice but to keep going.",
        'exits': {"east": "bathroom", "north": "ammunitions room"}
    },

    'ammunitions room': {
        'description': "The walls of the room are lined with guns, grenades, and knives.",
        'exits': {"south": "passage", "east": "bunker"},
        'items': {"pistol": "A Glock pistol lies on the table"}
    },

    'bunker': {
        'description': "The bunker is built well. The room is safe from even nuclear radiation. A table with enough supplies to last for days lies in front of you.",
        'exits': {"west": "ammunitions room"},
        'items': {"key": "A rusty key lies on the table."}
    },
    
    'bedroom': {
        'description': "The whole room is a mess. The bed, curtains, and paintings are torn up. You hear breathing and look up to see a mythical Chimera. Your only choice is to fight.",
        'requires': {"key": True},
        'exits': {"west": "balcony", "east": "living room"}
    },

    'balcony': {
        'description': "You get a beautiful view of a forest and a lake, and in front of it, you find a mild view of the city.You will have to jump off the balcony to escape the haunted mansion ",
        'exits': {"east": "bedroom"},
        
    },
}

inventory = []
current_room = "living room"

# ...

def fight():
    if "pistol" in inventory:
        print("You take on the Chimera and shoot it with your gun!")
        rooms["bedroom"]["requires"]["key"] = False
        print("You've defeated the Chimera! You find yourself magically teleported to the balcony.")
        return "balcony"  # Return the room you want to teleport the player to
    else:
        print("You try to fight the Chimera, but it's too strong for you. It pounces on you and ends the game")
        exit(0)

# ...

while True:
    print(rooms[current_room]['description'])

    if 'exits' in rooms[current_room]:
        print('Exits:')
        for direction, next_room in rooms[current_room]['exits'].items():
            # Check if the direction is west, the key is required for the next room, and the key is not in the inventory
            if direction == "west" and rooms[next_room].get("requires", {}).get("key", False) and "key" not in inventory:
                print("You need the key to enter the bedroom.")
                continue  # Skip entering the bedroom without the key
            print(f"- {direction}")

    if "items" in rooms[current_room]:
        print("Items:")
        for item in rooms[current_room]['items'].values():
            print(f"- {item}")

    action = input("\nWhat do you do? ").lower()

    if action in rooms[current_room]['exits']:
        current_room = rooms[current_room]['exits'][action]
    elif action == "take" and "items" in rooms[current_room]:
        item_name = input("Which item do you want to take? ").lower()
        if item_name in rooms[current_room]["items"]:
            inventory.append(item_name)
            del rooms[current_room]["items"][item_name]
            print(f"You took the {item_name}.")
        else:
            print("There is no such item here.")
    elif action == "drop" and "items" in rooms[current_room]:
        item_name = input("Which item do you want to drop? ").lower()
        if item_name in inventory:
            inventory.remove(item_name)
            rooms[current_room]["items"][item_name] = f"{item_name} lies here."
            print(f"You dropped the {item_name}.")
        else:
            print("You don't have that item in your inventory.")
    elif action == "fight" and current_room == "bedroom":
        current_room = fight()  # Update the current room based on the fight result
    elif action == "jump" and current_room == "balcony":
        print("You bravely jump off the balcony, escaping the mansion! Congratulations, you've won the game.")
        exit(0)
    else:
        print("Invalid action. Try again.")


