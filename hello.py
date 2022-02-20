import math


def split_check(total, number_of_people):
        return math.ceil(total / number_of_people)
    
try:
    total_due = float(input("What is total "))
    number_of_people = int(input("people? "))
except ValueError:
    print("NOasdf ")
else:
    amount_due = split_check(total_due,number_of_people)
    print(amount_due)