from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    This is a programming problem where Karel fills the whole world with beepers.
    Karel starts in the bottom left corner of the world, facing east and ends in the bottom right corner of the world, facing east after putting beepers in all cases.
    """
    while left_is_clear():
        fill_line()  
        next_line()
    fill_line()

def fill_line():
    while front_is_clear():
        put_beeper()  
        move()

    put_beeper()

def next_line():
    turn_corner()
    while front_is_clear():
        move()  
    turn_right()
    move()
    turn_right()


def turn_corner():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()