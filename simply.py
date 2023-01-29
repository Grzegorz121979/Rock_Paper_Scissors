import random

def play():
    user = input("What is your choice 'r' for rock, 'p' for paper, 's' scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return 'It\'s a tie'
    if win(user, computer):
        return 'You won'
    return 'You lost'

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
        
game = input("Do you want to play rock, paper, scissors: (Y/N): ").upper()
next_game = True
while next_game:
    if game == 'Y':
        print(play())
        game = input("Do you want to play rock, paper, scissors: (Y/N): ").upper()
    else:
        next_game = False
        print("Thanks for the game.")