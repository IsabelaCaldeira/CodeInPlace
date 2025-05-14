import random

def main():
    print("Khansole Academy")
    
    compteur = 0;
    while(compteur < 3):
        numb1 = random.randint(10, 99)
        numb2 = random.randint(10, 99)
        
        print(f'What is {numb1}  + {numb2}?')
        user_answer = int(input('Your answer: '))
        sum =  numb1 + numb2
        if(user_answer == sum):
            print('Correct!')
            compteur += 1
            print(f"You've gotten {compteur} correct in a row")
        else:
            print(f"Incorrect.\nThe expected answer is {sum}")
            compteur = 0
    
    print("Congratulations! You mastered addition.")
    
if __name__ == '__main__':
    main()