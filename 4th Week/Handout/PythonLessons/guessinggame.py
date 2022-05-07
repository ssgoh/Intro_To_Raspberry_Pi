import random

continue_to_play="Y"
while continue_to_play=="Y":
    mystery_no = random.randint(1,50)
    print(mystery_no)

    
    while True:
        guess=int(input('Guess a number between 1 to 50  '))
        if guess == mystery_no:
            print("You guessed correctly!! \n", "The Mystery No is ", mystery_no)
            break
            
        elif guess > mystery_no:
            print('Too High. Try Again ')
        elif guess < mystery_no:
            print('Too Low. Try Again ')


    continue_to_play=input('Contine to play Next Game? Y / N ')

