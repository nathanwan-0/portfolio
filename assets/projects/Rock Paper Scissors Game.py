import random

def play_game():
    show_rules()
    player = get_player_choice()
    computer = get_computer_choice()
    declare_winner(player, computer)
    
def show_rules():
    print("*** Rock-Paper-Scissors ***")
    print()
    print("Rules:\tEach player chooses either rock, paper, or scissors.")
    print("      \tThe winner is determined by the following rules:")
    print("              \trock smashes scissors -> rock wins")
    print("              \tscissors cuts paper   -> scissors wins")
    print("              \tpaper covers rock     -> paper wins")
    print()

def get_player_choice():
    player = input("Player choice: ")
    return player.lower()

def get_computer_choice():
    computer = random.randint(1,3)
    if computer == 1:
        computer = "rock"
        print("Computer choice: " + computer)
        return computer.lower()
    elif computer == 2:
        computer = "paper"
        print("Computer choice: " + computer)
        return computer.lower()
    elif computer == 3:
        computer = "scissors"
        print("Computer choice: " + computer)
        return computer.lower()
    
def declare_winner(player, computer):
    print()
    if player == computer:
        print("Winner: Draw")
    elif player == "rock" and computer == "scissors":
        print("Winner: player")
    elif player == "paper" and computer == "rock":
        print("Winner: player")
    elif player == "scissors" and computer == "paper":
        print("Winner: player")
    else:
        print("Winner: computer")