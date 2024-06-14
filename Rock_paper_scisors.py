import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
user_score = 0
computer_score = 0
tie=0

def play_round(user_choice):
    global user_score, computer_score,tie
    
    # Generate computer choice
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
        tie +=1
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You win!"
        user_score += 1
    else:
        result = "You lose!"
        computer_score += 1
    
    # Update the result and scores
    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}")
    score_label.config(text=f"User Score: {user_score}  Computer Score: {computer_score} Tie: {tie}")
    
    # Ask to play again
    if messagebox.askyesno("Play Again?", "Do you want to play another round?"):
        pass  # Continue playing
    else:
        root.destroy()  # Exit the game

# Set up the main application window
root = tk.Tk()
root.title("Rock Paper Scissors game")
root.geometry("400x300")
root.configure(bg='lightblue')

# Create widgets
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors to play:")
instructions_label.pack()

result_label = tk.Label(root, text="")
result_label.pack()

score_label = tk.Label(root, text=f"User Score: {user_score}  Computer Score: {computer_score} Tie: {tie}")
score_label.pack()

# Create buttons for user choices
rock_button = tk.Button(root, text="Rock",bg="brown",fg="white", command=lambda: play_round("Rock"))
rock_button.pack(side=tk.LEFT, padx=10, pady=10)

paper_button = tk.Button(root, text="Paper",bg="green",fg="white", command=lambda: play_round("Paper"))
paper_button.pack(side=tk.LEFT, padx=10, pady=10)

scissors_button = tk.Button(root, text="Scissors",bg="gold",fg="white", command=lambda: play_round("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

# Run the application
root.mainloop()
