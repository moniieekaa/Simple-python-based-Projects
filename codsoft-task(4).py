import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "user"
    else:
        return "computer"

# Function to handle the user's choice
def user_choice(choice):
    global user_score, computer_score
    
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    
    if result == "user":
        user_score += 1
        result_text = "You win!"
    elif result == "computer":
        computer_score += 1
        result_text = "Computer wins!"
    else:
        result_text = "It's a tie!"
    
    result_label.config(text=f"Your choice: {choice}\nComputer's choice: {computer_choice}\nResult: {result_text}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Initialize the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x300")
root.configure(bg='#f0f0f0')

# Initialize scores
user_score = 0
computer_score = 0

# Title Label
title_label = tk.Label(root, text="Rock-Paper-Scissors", font=("Helvetica", 16, "bold"), bg='#f0f0f0')
title_label.pack(pady=10)

# Choice Buttons
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: user_choice("Rock"), bg='#4caf50', fg='white', font=("Helvetica", 12, "bold"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: user_choice("Paper"), bg='#2196F3', fg='white', font=("Helvetica", 12, "bold"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: user_choice("Scissors"), bg='#f44336', fg='white', font=("Helvetica", 12, "bold"))
scissors_button.grid(row=0, column=2, padx=10)

# Result Label
result_label = tk.Label(root, text="", bg='#f0f0f0', font=("Helvetica", 12))
result_label.pack(pady=10)

# Score Label
score_label = tk.Label(root, text=f"Score - You: {user_score} | Computer: {computer_score}", bg='#f0f0f0', font=("Helvetica", 12, "bold"))
score_label.pack(pady=10)

# Reset Button
reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg='#ff9800', fg='white', font=("Helvetica", 12, "bold"))
reset_button.pack(pady=10)

# Run the application
root.mainloop()