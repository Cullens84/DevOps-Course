import random  # imports a module to use in the code
# states the options for theh game in a list
options = ["rock", "paper", "scissors"]
# stating the computer will make a random choice from the list
computer = random.choice(options)


def player_input():  # function to get player input
    player = input("choose one 'rock', 'paper', 'scissors':")  # players input
    # converting the players nput to lower so it will always match the list
    player = player.lower()
    return player  # returns the players input so other functions can call it


# this starts the if statement by defining the rules using if, elif and then else
player = player_input()
if computer == player:
    print("tie")
elif computer == "rock":
    if player == "paper":  # each state ment corresponds to the game, rock beats scissors, paper beats rock
        print("you win")
    else:
        # this allows the game to be broken down into ifs and elses
        print("you loose sucka!!!!!!")
elif computer == "paper":
    if player == "scissors":  # there are if statements nested in the elifs to allow all conetations
        print("you win")
    else:
        print("you loose sucka!!!!!!")
elif computer == "scissors":
    if player == "rock":
        print("you win")
    else:
        print("you loose sucka!!!!!!")
else:
    print("technical issues start again")
    player_input()
print("computer chose", computer)
