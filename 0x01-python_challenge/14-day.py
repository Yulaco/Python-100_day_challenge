# Rock, paper, scissors game

from getpass import getpass as input

print("Today you are going to play Rock, Paper, Scissors game.")
print()

player1 = input("Please player 1 enter your move: R, P or S: ")
player2 = input("Please player 2 enter your move: R, P or S: ")

if player1 == player2:
    print("Its a draw")
elif player1 == "R" and player2 == "S":
    print("Player 1 wins with rock.")
elif player2 == "R" and player1 == "S":
    print("Player 2 wins with rock.")
elif player1 == "P" and player2 == "R":
    print("Player 1 wins with paper.")
elif player2 == "P" and player1 == "R":
    print("Player 2 wins with paper.")
elif player1 == "S" and player2 == "P":
    print("Player 1 wins with scissors.")
elif player2 == "S" and player1 == "P":
    print("Player 2 wins with scissors.")
else:
    print("The option entered is not valid. Please try again!")
