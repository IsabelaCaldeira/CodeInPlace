from stanfordkarel import *

"""
Each row starts in front of a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers infinite
her bag. How can you solve this puzzle?
"""

def main():
    move()
    spread_beepers()
    step_back()

def step_back():
    turn_around()
    move()
    turn_around()

def spread_beepers():
    while(beepers_present()):
        pick_beeper()
        if beepers_present():
            move_to_no_beepers()
            put_beeper()
            back_to_beginning()
    put_beeper()

def move_to_no_beepers():
    while(beepers_present()):
        move()

def back_to_beginning():
    turn_around()
    move_to_wall()
    turn_around()
    move()

def move_to_wall():
    while(front_is_clear()):
        move()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()