import random

def play():
    user=input("What's Your Choice?? 'r' for rock, 'p' for paper, 's' for scissor/n")
    computer=random.choice(['r','p','s'])

    if user == computer:
        return 'Tie'
    if win(user,computer):
        return 'You Won!!'

    return 'You Lose'

def win(player,opponent):
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') or \
        (player=='s' and opponent=='p'):
        return True
    
def game_loop():
    while True:
        result=play()
        print(result)
        play_again=input("Do you want to play again? y/n").lower()
        if play_again != "y":
            break
        print("Thanks for playing!")

game_loop()