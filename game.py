import tkinter as tk
from tkinter import ttk
import random

class HintedNumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hinted Number Guessing Game")
        
        self.secret_number = random.randint(1, 100)
        self.max_attempts = 5
        self.attempts = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        self.message_label = ttk.Label(self.root, text="Welcome to the Hinted Number Guessing Game!")
        self.message_label.pack(pady=10)
        
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=5)
        
        self.guess_label = ttk.Label(self.input_frame, text="Enter your guess:")
        self.guess_label.grid(row=0, column=0, padx=5)
        
        self.guess_entry = ttk.Entry(self.input_frame, width=10)
        self.guess_entry.grid(row=0, column=1, padx=5)
        
        self.guess_button = ttk.Button(self.input_frame, text="Guess", command=self.check_guess)
        self.guess_button.grid(row=0, column=2, padx=5)
        
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.pack(pady=10)
        
        self.new_game_button = ttk.Button(self.root, text="New Game", command=self.new_game)
        self.new_game_button.pack(pady=5)
        
    def check_guess(self):
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            
            if guess == self.secret_number:
                self.result_label.config(text=f"Congratulations! You've guessed the correct number {self.secret_number} in {self.attempts} attempts!")
                self.guess_button.config(state=tk.DISABLED)
            elif self.attempts == self.max_attempts:
                self.result_label.config(text=f"Sorry! You've used all {self.max_attempts} attempts. The correct number was {self.secret_number}.")
                self.guess_button.config(state=tk.DISABLED)
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try guessing higher.")
                if self.secret_number - guess <= 10:
                    self.result_label.config(text="Too low! But you are close. Try guessing higher.")
            else:
                self.result_label.config(text="Too high! Try guessing lower.")
                if guess - self.secret_number <= 10:
                    self.result_label.config(text="Too high! But you are close. Try guessing lower.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")
    
    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.message_label.config(text="Welcome to the Hinted Number Guessing Game!")
        self.result_label.config(text="")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)

# Create main window
root = tk.Tk()
game = HintedNumberGuessingGame(root)
root.mainloop()
