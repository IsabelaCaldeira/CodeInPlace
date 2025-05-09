from stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while(front_is_clear()):
        turn_left()
        build_colmun()
        for i in range(4):
            move()

    turn_left()
    build_colmun()
        
def build_colmun():
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()
    turn_around()
    move_to_wall()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while(front_is_clear()):
        move()

if __name__ == '__main__':
    main()