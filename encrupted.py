import string
import random
#
character = " " + string.punctuation + string.digits + string.ascii_letters
character = list(character)
key = character.copy()
random.shuffle(key)
print(f"characters:{character}")
print(f"key:{key}")
#
originaltext = input("Enter a message to encrupt:")
encruptedtext = ""
#
for letter in originaltext: 
    #index = character.index(letter)
    encruptedtext += key[character.index(letter)]
#
print(f'original message:{originaltext}')
print(f"encrupted message:{encruptedtext}")
 






