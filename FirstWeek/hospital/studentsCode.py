from stanfordkarel import *

# Here is a place to program your Section problem

def main():
    """Karel needs to move until it finds a beeper//while front is clear
    Karel needs to change directions 
    Karel needs to detect if there is a beeper
    """
    while(front_is_clear()):
        if(beepers_present()):
            build_hospital()
        if(front_is_clear()):
            move()

def build_hospital():
    """Karel does 2 columns 3 rows of beepers"""
    turn_left()
    build_column()
    change_column()
    build_column()
    turn_left()

def change_column():
    turn_right()
    move()
    put_beeper()
    turn_right()

def build_column():
     for i in range(2):
        move()
        put_beeper()

def turn_right():
    for i in range(3):
        turn_left()   

if __name__ == '__main__':
    main()