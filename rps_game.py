import random
from dataclasses import dataclass

@dataclass
class GameEngine:
    valid_moves: list = ("rock", "paper", "scissors")

    def get_computer_move(self) -> str:
        return random.choice(self.valid_moves)

    def decide_winner(self, player_move: str, computer_move: str) -> str:
        if player_move == computer_move:
            return "tie"
        elif (player_move == "rock" and computer_move == "scissors") or \
             (player_move == "scissors" and computer_move == "paper") or \
             (player_move == "paper" and computer_move == "rock"):
            return "win"
        else:
            return "lose"

def main():
    game = GameEngine() 
    player_move = input("Enter your move (rock, paper, or scissors): ").lower()

    if player_move not in game.valid_moves:
        print("Invalid move! Please enter rock, paper, or scissors.")
        return

    computer_move = game.get_computer_move()
    result = game.decide_winner(player_move, computer_move)

    print(f"Your move: {player_move}")
    print(f"Computer's move: {computer_move}")
    print(f"Result: You {result}!")

if __name__ == "__main__":
    main()
