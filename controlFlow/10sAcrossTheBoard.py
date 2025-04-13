from stanfordkarel import *

def main():
    """
    Place 10 beepers in each position of the bottom row of a world.
    """
    while(front_is_clear()):
        put_10_beepers()
        move()
    put_10_beepers()

def put_10_beepers():
    for i in range(10):
        put_beeper()

if __name__ == '__main__':
    main()