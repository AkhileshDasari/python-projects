foods = []
quantity =[]
prices = []
total = 0

while True:
      food = input("Enter a food to buy (q to quit) : ")
      if food.lower() == "q":
        break
      else:
        foods.append(food)
        price = int(input(f"Enter the price of {food}: rs"))    
        quantity =int(input(f"Enter the quantity of {food}: "))
        prices.append(price)

print("------YOUR CART------")
for food in foods :
    print(food)
   
for price in prices :
    gst = 18 % 100
    #total = total + price
    total += price * quantity + gst

print()
print("Added gst: 0.18%")
print(f"Your Total is {total}rs")