from stanfordkarel import *

"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_3()
    pick_beeper()
    move()
    turn_left()
    move_3()
    put_beeper()
    turn_90()
    move_3()
    turn_right()
    move_to_wall()
    turn_90()

def turn_right():
    for i in range(3):
        turn_left()

def turn_90():
    turn_left()
    turn_left()

def move_3():
    for i in range(2):
        move()

def move_to_wall():
    while(front_is_clear()):
        move()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()