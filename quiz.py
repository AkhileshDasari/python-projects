#quiz code
print("-------------Quiz----------------")
questions = ("How many days are there in a leap year:",
             "Who was the first president of USA:",
             "How many organs are there in a human body:",
             "Eygpt lies under which continent:",
             "A class of 30 students shake their hands,no of handshakes:",
             "Cheapest material among:",
             "Which city is called the city of lakes:",
             "80 percent of 120 is:",
             "Which anime was declared best in 2023:",
             "Which color absorbs most of the heat:")

options = (("A. 367" , "B. 366" , "C. 365" , "D. 364" ),
           ("A. Colombus" , "B. George Washington" , "C. Donald Trumph" , "D. John Adams" ),
           ("A. 82" , "B. 64" , "C. 78" , "D. 91" ),
           ("A. Africa" , "B. Asia" , "C. South America" , "D. Antartica" ), 
           ("A. 455" , "B. 435" , "C. 30" , "D. 15" ),
           ("A. Plastic" , "B. Brass" , "C. Paper" , "D. Bronze" ),
           ("A. Ladak" , "B. Rajasthan" , "C. Hyderabad" , "D. Udaipur" ),
           ("A. 96" , "B. 92" , "C. 80" , "D. 90" ),
           ("A. Naruto" , "B. Haiyaku" , "C. Demonslayer" , "D. Spyxfamily" ),
           ("A. White" , "B. Black" , "C. Grey" , "D. Blue" )) 

answers = ("B" , "B" , "C" , "A" , "B" , "A" , "D" , "A" , "C" , "B")

guesses = []
score = 0
question_num = 0

for question in questions :
    print("--------------------------------------------------------")
    print(question)

    for option in options[question_num]:
        print(option)

    guess = input("Enter your answer (A/B/C/D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
           score += 1
           print("CORRECT!")

    else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct anwer.")
            
    question_num += 1

print("--------------------------------")
print("           RESULTS              ")   
print("--------------------------------")   
print("Answers:", end = "")    
for answer in answers:
    print(answer, end = " ")
print()

print("Guesses:", end = "")    
for guess in guesses:
    print(guess, end = " ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is {score}%")

    

    










