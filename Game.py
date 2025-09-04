import random

options = ["rock", "paper", "scissors"]

user = input("choose rock, paper, or scissors: ")
computer = random.choice(options)

print("computer chose:", computer)

if user == computer:
	print("it's a tie!")
elif (user == "rock" and computer == "scissors") or \
	 (user == "paper" and computer == "rock") or \
	 (user == "scissors" and computer == "paper"):
	print("you win!")
else:
	print("computer wins!")import random

options = ["rock", "paper", "scissors"]

user = input("choose rock, paper, or scissors: ")
computer = random.choice(options)

print("computer chose:", computer)

if user == computer:
	print("it's a tie!")
elif (user == "rock" and computer == "scissors") or \
	 (user == "paper" and computer == "rock") or \
	 (user == "scissors" and computer == "paper"):
	print("you win!")
else:
	print("computer wins!")