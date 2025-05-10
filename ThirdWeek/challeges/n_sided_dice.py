import random

def main():
    dice = int(input("How many sides does your dice have? "))
    random_number = random.randint(1, dice)

    print("Your roll is " +str(random_number))

if __name__ == '__main__':
    main()