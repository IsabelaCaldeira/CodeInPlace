from stanfordkarel import *

# File: shelter.py
# -----------------------------
# The warmup program defines a "main"
# function which should make Karel 
# move to the beeper, pick it up, and
# return home.
def main():
    move_to_wall()
    turn_right()
    move()
    turn_left()
    move()
    pick_beeper()

    turn_corner()
    move()
    turn_right()
    move()
    turn_left()
    move_to_wall()
    turn_corner()
    
def move_to_wall():
    while(front_is_clear()):
        move()

def turn_corner():
    turn_left()
    turn_left()
def turn_right():
    for i in range(3):
        turn_left()
    
# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()