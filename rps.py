# RPS game

import select
import random

per_score = 0
com_score = 0

playing = True
options = "rock" , "paper" , "scissors"
for option in options:
     option.capitalize()
print(f"From options: {options}")
while playing :
    select = None
    computer = random.choice(options)

    while select not in options :
      select = input("Enter a choice: ")

      print(f"selected: {select}")
      print(f"computer: {computer}")

      if select == "rock" and computer == "scissors":
            print("You won!")
            per_score += 1
      elif select == "paper" and computer == "rock":
            print("You won!")
            per_score += 1 
      elif select == "scissors" and computer == "rock":
            print("You lose!")
            com_score += 1
      elif select == "paper" and computer == "scissors":
            print("You lose!")
            com_score += 1
      elif select == "rock" and computer == "paper":
            print("You lose!")
            com_score += 1
      elif select == "scissors" and computer == "paper":
            print("You won!")
            per_score += 1
      else:
            print("it's a tie!")
            per_score = com_score
  
      if not input("playagain? (y/n):").lower() == "y":
        playing = False
        
        print(f"Your Score: {per_score}")
        print(f"Computer score: {com_score}")
        if not com_score > per_score:
          print(f"You won by {per_score} points.")
        elif per_score == com_score :
             print(f"It's a tie by {per_score} points.")
        else:
          print(f"computer won by {com_score} points.") 


         
      
      
          






