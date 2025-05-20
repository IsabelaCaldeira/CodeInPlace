import random

NUM_ROUNDS = 5

def main():
    # Have a number generated from 10-100 and allow a guess to be made higher or lower. 
    # If correct guess is made a point is given, if wrong no point is given
    
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score = 0
    for i in range(NUM_ROUNDS):

        print("Round", i+1)
        user_number = random.randint(1, 100)
        print("Your number is", user_number)
        guess = input("Do you think your number is higher or lower than the computer's?: ")
        computer_number = random.randint(1, 100)

        # We're telling the user whether their guess is greater than the computer_number or not
        if user_number > computer_number:
            answer = "higher"
        else:
            answer = "lower"

        if answer == guess:
            print("You were right! The computer's number was", computer_number)
            score += 1
        else:
            print("Aww, that's incorrect. The computer's number was", computer_number)
            
        print("Your score is now", score)
        print("")

    print("Thanks for playing!")



if __name__ == "__main__":
    main()