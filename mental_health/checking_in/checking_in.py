
from asyncore import read
from datetime import datetime

situation = input("What's going on:  ") 
emotion = input("What emotions came up:  ")
negative_automatic_thought = input("What thoughts came up:  ") 
evidence = input("What makes you think that:  ")
evidence_against = input("What evidence could prove otherwise:  ") 
alt_thought = input("Is there another way to think about this:  ") 
final_emotion = input("Now how do you feel:  ")
today = datetime.now()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
final_report = f"---------------------\n {dt_string} \n \n 1.) Situation: {situation} \n \n 2.) Emotion: {emotion} \n \n 3.) Negative Automatic Thought: {negative_automatic_thought} \n \n 4.) Evidence: {evidence} \n \n 5.) Evidence against: {evidence_against} \n \n 6.) Alternate thought: {alt_thought} \n \n 7.) Now emotion: {final_emotion} \n---------------------\n"
journal_file = open("./checking_in.txt", "a+")

journal_file.writelines(final_report)

read_file = open("./checking_in.txt", "r")

print("Thought record saved. Take a look......... \n", final_report)

print("++++++++++++++++++++++++")

print(read_file.read())
