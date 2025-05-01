from stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    """
    Karel moves to the pile of beepers.
    She spreads the beepers.
    She goes back to the original position.
    """
    move()
    spread_beepers()
    move_back()

def spread_beepers():
    """
    Karel picks up one beeper at a time.
    Karel moves and puts down a beeper in 
    the next available spot.
    Moves back
    """
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move_to_next()
            put_beeper()
            move_back()
            move()
    put_beeper()

def move_to_next():
    while beepers_present():
        move()

def move_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()