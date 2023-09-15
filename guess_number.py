biggest_num = 100
max_num_guesses = 5
num_guesses = 0
num_found = False
num_to_guess = 45

while input("Wanna play the number guessing game? (y or n) ==> ").upper() == "Y":
   
 while not num_found and num_guesses < max_num_guesses:
        my_guess = int(input(f"Enter a number between 1 and {biggest_num} ==> "))

        if not (0 < my_guess <= biggest_num):  
            print(f"{my_guess} is an invalid entry... try again")
            continue

        num_guesses += 1  

        if my_guess == num_to_guess:
            num_found = True
            print(f'You found the number {num_to_guess}! '
                  f'And it took you {num_guesses} guesses to find it')
        else:
            print(f"{my_guess} is too {('high' if my_guess > num_to_guess else 'low')}")
            num_left = "no" if max_num_guesses == num_guesses else (max_num_guesses - num_guesses)
            print(f'You have {num_left} guesses left.')
 
if not num_found:
        print("You have no more guesses left")

print("Thanks for playing!")
