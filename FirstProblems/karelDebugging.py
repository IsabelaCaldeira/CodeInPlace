"""
Assumes that Karel starts in the bottom of a world filled with beepers
Picks up all the beepers in the first two rows
"""
def pick_up_all_beepers():
    pick_row()
    change_rows()
    pick_row()

def change_rows():
    turn_left()
    move()

def pick_row():
    while front_is_clear():
        pick_beeper()
        move()
        
#Second Karel Debugging 
def main():
    dictionary = {}
    dictionary["learning"] = "awesome"
    dictionary["coding"] = "fun"
    # ... Fill with more data
    remove_keys_containing_string(dictionary, "learn")

"""
This Python function takes in a dict and a string and  
removes all keys containing that string from the dict
"""
def remove_keys_containing_string(dictionary, remove):
    new_dictionary = {}
    for key in dictionary:
        if remove not in key:
            new_dictionary[key] = dictionary[key]