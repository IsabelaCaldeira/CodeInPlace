from stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while(front_is_clear()):
        if(beepers_present()):
            build_hospital()
        if(front_is_clear()):
            move()

def build_hospital():
    up_column()
    down_column()

def up_column():
    turn_left()
    put_2_beepers()
    turn_right()
    move()

def down_column():
    turn_right()
    put_beeper()
    put_2_beepers()
    turn_left()

def put_2_beepers():
    for i in range(2):
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()