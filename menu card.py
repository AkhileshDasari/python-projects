menu = {"popcorn":150,
        "pizza":299,
        "fren-ies":170,
        "burger":180,
        "hotdog":200,
        "coke":60,
        "chi-gs":399,
        "garli-ad":229,
        "whi-sta":239,
        "mas-sta":199}

cart =[]
total = 0

print("-------------MENU--------------")
for key,value in menu.items() :
    print(f"{key:10}:rs.{value}")
print("-------------------------------")

while True:
    food = input("select from your menu (q for quit):").lower()

    if food == "q":
       break

    elif menu.get(food) is not None :
        cart.append(food) 

print("-----------Your Cart-------------")     
for food in cart :
    total += (menu.get(food))
    print(food) 

print(f"Your total is {total}rs.")            















        