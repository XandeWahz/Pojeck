print("Guess my age")
import random
age = random.randint(1, 100)
tries = 10
while tries > 0:
    try:
        user_guess = int(input("Enter Your Guess: ").strip())
        if user_guess == age:
            print("You got it!")
            break
        elif user_guess != age:
            tries -= 1
            print(f" Guess again! You have this number of tries left: {tries}")
    except ValueError as e:
        print(f" Don't think that was a number, You have this number of tries left: {tries}")

if tries == 0:
    print(f"Sorry!, You have ran out of tries left :( ")
    print(f"Correct age {age}")
        
        
            
                  
