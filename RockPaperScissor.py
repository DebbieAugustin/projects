import random

choices = ["rock", "paper", "scissors"]

while True: #Keeps the game going
    player_choice = input("Pick your choice (rock/paper/scissors): ") #Get player's input
    computer_choice = random.choice(choices) #Get computer's input

    #Find the game results:
    if player_choice == computer_choice:
        result = "It's a tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            result = "Computer wins"
        else:
            result = "You win"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            result = "Computer wins"
        else:
            result = "You win"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            result = "Computer wins!"
        else:
            result = "You win!"

    #Print the results
    print(f"You picked: {player_choice}.")
    print(f"Computer picked: {computer_choice}.")
    print(f"Results: {result}")
    
    #Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "n":
        print("Thanks for playing")  
        break # Ends the game if the player doesn't want to play again

