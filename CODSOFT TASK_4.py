import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        user_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "You lose!"

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Score - You: 0, Computer: 0")

# Setting up the GUI
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Creating buttons for user choices
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("rock"))
rock_button.pack()

paper_button = tk.Button(root, text="Paper", command=lambda: play_game("paper"))
paper_button.pack()

scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"))
scissors_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

# Label to display the score
score_label = tk.Label(root, text="Score - You: 0, Computer: 0")
score_label.pack()

# Button to reset the game
reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack()

# Running the GUI
root.mainloop()
