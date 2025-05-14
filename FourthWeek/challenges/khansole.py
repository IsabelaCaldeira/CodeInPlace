import random

def main():
    print("Khansole Academy")
    numb1 = random.randint(10, 99)
    numb2 = random.randint(10, 99)
    
    print(f'What is {numb1} + {numb2}?')
    user_answer = int(input('Your answer: '))
    sum =  numb1 + numb2
    if(user_answer == sum):
        print('Correct!')
    else:
        print(f"Incorrect.\nThe expected answer is {sum}")
    
if __name__ == '__main__':
    main()