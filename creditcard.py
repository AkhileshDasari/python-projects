sum_of_odd = 0
sum_of_even = 0
total = 0
card_number = input("Enter a credit card #: ")
card_number = card_number.replace("-" , "")
for x in card_number[::2]:
    #sum_of_odd += int(x)
    sum_of_odd = sum_of_odd + int(x)
for x in card_number[1::2]:
    x = int(x) * 2 
if x >=10:
    sum_of_even = sum_of_even + (1 + (x % 10))
    #sum_of_even += 1 + (x % 10)
else:
    #sum_of_even += x
    sum_of_even = sum_of_even + x
total = sum_of_even + sum_of_odd

if total % 10 == 0:
    print("valid card")
else:
    print("invaild")
#print(card_number)
