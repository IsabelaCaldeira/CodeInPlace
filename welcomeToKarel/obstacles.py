"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from stanfordkarel import move, turn_left, put_beeper

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    move()
    turn_left()
    move()
    turn_right()
    move()
    gettin_into_hole()
    out_the_hole()
    gettin_into_hole()
    out_the_hole()
    gettin_into_hole()
    turn_left()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_90degree():
    turn_left()
    turn_left()

def gettin_into_hole():
    turn_right()
    move()
    put_beeper()

def out_the_hole():
    turn_90degree()
    move()
    turn_right()
    move()
# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()