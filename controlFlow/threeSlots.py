"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    for i in range(2):
        in_and_out_wall()
        turn_right()
        move()
    in_and_out_wall()
    turn_right()


# There is no need to edit code beyond this point

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_90degree():
    turn_left()
    turn_left()

def in_and_out_wall():
    turn_right()
    move()
    put_beeper()
    turn_90degree()
    move()

if __name__ == '__main__':
    main()