from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES
BOXES_HEIGHT = CANVAS_HEIGHT/BOX_SIZE

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    for i in range(N_BOXES):
        if(i==0):
            canvas.create_rectangle(
                0, 
                BOXES_HEIGHT, 
                BOX_SIZE, 
                CANVAS_HEIGHT, 
                "white",
                "black"
            )
        else:
            canvas.create_rectangle(
                BOX_SIZE*i, 
                BOXES_HEIGHT, 
                BOX_SIZE*(i+1), 
                CANVAS_HEIGHT,
                "white",
                "black"
            )


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
    