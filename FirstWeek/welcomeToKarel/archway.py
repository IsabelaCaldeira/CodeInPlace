"""
This is a worked example. This code is starter code; you should edit and run it to
solve the problem. You can click the blue show solution button on the left to see
the answer if you get too stuck or want to check your work!
"""

from stanfordkarel import move, turn_left

def main():
    """
    Karel starts facing East in the bottom left corner of the world and ends facing East in the bottom right corner of the world.
    """
    turn_left()
    move_3blocks()
    turn_right()
    move_3blocks()
    turn_right()
    move_3blocks()
    turn_left()

def move_3blocks():
    move()
    move()
    move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()