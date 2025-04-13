from stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    for i in range(4):
        check_corridor()
        out_corridor()
        next_corridor()
    check_corridor()
    out_corridor()
    turn_corner()

def check_corridor():
    while(front_is_clear()):
        move()
    if(no_beepers_present()):
        put_beeper()

def out_corridor():
    turn_corner()
    while(front_is_clear()):
        move()
    
def next_corridor():
    turn_right()
    move()
    turn_right()

def turn_corner():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

        
if __name__ == '__main__':
    main()
