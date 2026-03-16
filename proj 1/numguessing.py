import random

def game():
    number=random.randint(0,100)
    print("start guessing the number between 0 to 100")
    attempts=0
    while True:
        guess= int(input("enter your guess:"))
        attempts+=1

        if guess==number:
            print("yayy! you guessed right! ")
            break
        elif guess>number:
            print("guess a lower number")
        
        else:
            print("guess a higher number")
            

def main():
    answer='y'
    while answer =='y':
         game()
         answer = input("do you want to play again? y/n ").lower()

    print("thanks for playing!")    

   

if __name__ == "__main__":
    main() 