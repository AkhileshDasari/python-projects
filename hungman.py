from wordslist import  *
import random

print("----------------------------------")
print("ANIMAL DICATIONARY TO SAVE HUNGMAN")
print("----------------------------------")
    
def displayman(wrongguesses):
    print("-----")
    for line in hungmanart[wrongguesses]:
        print(line)
    print("-----")    

def displayhint(hints):
    print(" ".join(hints))


def displayanswers(answers):
    print(" ".join(answers))        

def main():
    answers = random.choice(animals)
    hints = ["_"] * len(answers)
    wrongguesses = 0
    guessedletters = set()
    isrunning = True
    
    while isrunning:

        displayman(wrongguesses)
        displayhint(hints)

        guess = input("Guess a letter:").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid guess. Try again")
            continue

        if guess in guessedletters:
            print(f"You already guessed {guess} letter")
            continue

        guessedletters.add(guess)

        if guess in answers:
            print("Good guess")
            for index in range(len(answers)):
                if answers[index] == guess:
                    hints[index] = guess
        else:
            wrongguesses += 1

        if "_" not in hints:
            displayman(wrongguesses)
            displayanswers(answers)
            print("You won")
            isrunning = False
            continue
        
        if wrongguesses >= len(hungmanart) -1:
            displayman(wrongguesses)
            displayanswers(answers)
            print("You lost")
            isrunning = False
            continue

if __name__ == "__main__":
   main()
