import random
from graphics import Canvas
# Name of the file to read in!
FILE_NAME = 'cswords.txt'

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
FONT = 'Arial'
FONT_SIZE = 50
COLOR = 'blue'


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    lines = []
    with open(FILE_NAME) as f:
        for line in f:
            # removes whitespace characters (\n) from the start and end of the line
            line = line.strip() 
            # if the line was only whitespace characters, skip it 
            if line != "":
                lines.append(line)
                
    return lines


def main():
    # your code here :) 
    # create a canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    # get the words from the file
    words = get_words_from_file()
    # randomly pick a number from 0 to the length -1
    random_number = random.randint(0, (len(words) - 1))
    random_word = words[random_number]
    # create text 
    canvas.create_text(
        CANVAS_WIDTH / 2 - (FONT_SIZE * 2.5), 
        CANVAS_HEIGHT / 2 - (FONT_SIZE ), 
        text = random_word,
        font = FONT,
        font_size = FONT_SIZE,
        color = COLOR
    )
    another_word = input('Hit Enter for the next one... ')
    main()