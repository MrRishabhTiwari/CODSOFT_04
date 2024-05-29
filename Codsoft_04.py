import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.master.geometry("400x350")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_label = tk.Label(master, text="Choose rock, paper, or scissors:")
        self.user_choice_label.pack()

        self.choice_var = tk.StringVar(master)
        self.choice_var.set("rock")

        self.choice_menu = tk.OptionMenu(master, self.choice_var, "rock", "paper", "scissors")
        self.choice_menu.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.computer_choice_label = tk.Label(master, text="")
        self.computer_choice_label.pack()

        self.play_button = tk.Button(master, text="Play", command=self.play_game)
        self.play_button.pack()

        self.score_label = tk.Label(master, text="Score: You 0 - 0 Computer")
        self.score_label.pack()

    def play_game(self):
        user_choice = self.choice_var.get()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=result)
        self.computer_choice_label.config(text=f"Computer chose {computer_choice}")

        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1

        self.update_score_label()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "You win!"
        else:
            return "Computer wins!"

    def update_score_label(self):
        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")


def main():
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
