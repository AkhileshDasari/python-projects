#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘
import random
diceart ={
    1:("┌─────────┐",
       "│         │",
       "│    ●    │",
       "│         │",
       "└─────────┘"), 
           
    2:("┌─────────┐",
       "│  ●      │",
       "│         │",
       "│       ● │",
       "└─────────┘"),

    3: ("┌─────────┐",
        "│ ●       │",
        "│    ●    │",
        "│       ● │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
no_of_dice = int(input("No of dice:"))
for die in range(no_of_dice):
   dice.append(random.randint(1,6))

#for die in range(no_of_dice):
 #    for line in diceart.get(dice[die]):
  #       print(line)

for line in range(5):
    print(diceart.get(die)[line], end=" ")
print()

for die in dice :
      total += die 
print(dice)
print(f"Total:{total}")   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   


