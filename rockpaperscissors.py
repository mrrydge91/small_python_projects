
import random

choices = ["p", "r", "s"]

computer_choice = random.choice(choices)

user_choice = input("[R]ock, [P]aper, [S]cissors: ")
processed_choice = str.lower(user_choice)
result = ""

if computer_choice == processed_choice:
    result = "tie"
    
if computer_choice == "p":
    if processed_choice == "s":
        result = "you win"
    if processed_choice == "r":
        result = "you lose"

if computer_choice == "s":
    if processed_choice == "p":
        result = "you lose"
    if processed_choice == "r":
        result = "you win"
        
if computer_choice == "r":
    if processed_choice == "p":
        result = "you win"
    if processed_choice == "s":
        result = "you lose"
        
print(f"{result}! ----- computer: {computer_choice}, you: {processed_choice}")