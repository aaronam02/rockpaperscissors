#Rock Paper scissors Shoot
import random

options= ["Rock", "Paper", "Scissors"]

computerMove =""
userPlay = ""
wins = 0
ties = 0
lose = 0
#the complay play chooses a random #, # respective to play>
i =(random.randint(0, 2))


def uPlay():
    global userPlay
    userPlay = input("Rock, Paper, Scissors set SSHOOOOOOOOOT: ")
    
def pcPlay():
    global computerMove
    computerMove = options[i]
    print("The computer plays " + computerMove)

def runGame():
    global userPlay
    global wins
    global ties
    global lose
    if computerMove == userPlay:
        ties += 1
        return ("Tie!")

    elif computerMove == "Rock":
        if userPlay == "Paper":
            wins +=1
            return ("Paper beats Rock, you WIN!")
        elif userPlay == "Scissors":
            lose += 1
            return ("Rock beats Scissors, you LOOSE!")
    elif computerMove == "Paper":
        if userPlay == "Rock":
            lose += 1
            return ("Paper beats Rock, you LOOSE!")
        elif userPlay == "Scissors":
            wins += 1
            return ("Scissors beats Paper, you WWIN!")
            
    elif computerMove == "Scissors":
        if userPlay == "Rock":
            wins += 1
            return ("Rock beats Scissors, you WINN!")
            
        elif userPlay == "Paper":
            lose += 1
            return ("Scissors beats Paper, you LOOSEEEEE!")

play = 'yes'

while play == 'yes':
    print("")
    uPlay()
    pcPlay()
    print(runGame())
    print("So far, you've won " + str(wins) + " games.")
    play = input("Play again? yes or no: ")
print("")
print("Game over! Wins:Ties:Losses " + str(wins) + ":" + str(ties) + ":" + str(lose))