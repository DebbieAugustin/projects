import random

choices = ["rock", "paper", "scissors"]

# Initiate player and computer scores
player_score = 0
computer_score = 0

# Ask the player for the number of rounds they want to play
while True:
        num_rounds = int(input("Enter the number of rounds you want to play: "))
        break
    
# Ask the player to choose a difficulty level
while True:
    difficulty = input("Choose a difficulty level (easy, medium, hard): ")
    if difficulty in ["easy", "medium", "hard"]:
        break

def computer_choice_easy():
    # Easy difficulty: Computer's choice is entirely random
    return random.choice(choices)

def computer_choice_medium():
    # Medium difficulty: Computer's choice is somewhat random, with a slight preference for winning moves
    if player_choice == "rock":
        return random.choice(["paper", "scissors", "scissors"])
    elif player_choice == "paper":
        return random.choice(["rock", "scissors", "rock"])
    else:
        return random.choice(["paper", "paper", "rock"])

def computer_choice_hard():
    # Hard difficulty: Computer's choice is based on trying to win or tie
    if player_choice == "rock":
        return random.choice(["paper", "paper", "scissors"])
    elif player_choice == "paper":
        return random.choice(["scissors", "scissors", "rock"])
    else:
        return random.choice(["rock", "rock", "paper"])

#Prints the number of rounds
for round_num in range(1, num_rounds + 1):
    print(f"Round {round_num} of {num_rounds}")

    #Ask for player's input
    while True:
        player_choice = input("Pick your choice (rock/paper/scissors): ")
        if player_choice in choices:
            break
            
    #Determines the computer's choice difficulty
    if difficulty == "easy":
        computer_choice = computer_choice_easy()
    elif difficulty == "medium":
        computer_choice = computer_choice_medium()
    else:
        computer_choice = computer_choice_hard()

    #Find the game results:
    if player_choice == computer_choice:
        result = "It's a tie"
    elif player_choice == "rock":
        if computer_choice == "paper":
            result = "Computer wins"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1
    elif player_choice == "paper":
        if computer_choice == "scissors":
            result = "Computer wins"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1
    elif player_choice == "scissors":
        if computer_choice == "rock":
            result = "Computer wins"
            computer_score += 1
        else:
            result = "You win"
            player_score += 1
    
    #Print the results
    print(f"You picked: {player_choice}.")
    print(f"Computer picked: {computer_choice}.")
    print(f"Result: {result}")
    print(f"Score => You: {player_score}, Computer: {computer_score}")

# Determine the overall winner
if player_score > computer_score:
    print("You win!")
elif computer_score > player_score:
    print("Computer win!")
else:
    print("It's a tie!")

print("Thanks for playing!")
