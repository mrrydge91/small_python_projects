
from asyncore import read
from datetime import datetime

situation = input("What is the reason for your concern:  ") 
emotion = input("What emotions came up:  ")
negative_automatic_thought = input("What thoughts came up:  ") 
evidence = input("What makes you think that:  ")
evidence_against = input("What evidence could prove otherwise:  ") 
alt_thought = input("Is there another way to think about this:  ") 
final_emotion = input("Now how do you feel:  ")
today = datetime.now()
dt_string = today.strftime("%d/%m/%Y %H:%M:%S")
final_report = f"---------------------\n {dt_string} \n Situation: {situation} \n Emotion: {emotion} \n Negative Automatic Thought: {negative_automatic_thought} \n evidence: {evidence} \n Evidence against: {evidence_against} \n Alternate thought: {alt_thought} \n Now emotion: {final_emotion} \n---------------------\n"
journal_file = open("./checking_in.txt", "a+")

journal_file.writelines(final_report)

read_file = open("./checking_in.txt", "r")

print("Thought record saved. Take a look......... \n", final_report)

print(read_file.read())
