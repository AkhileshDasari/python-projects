# Banking program

def show_balance(balance):
    print(f"Your Balance:${balance:.2f}")

def deposit():
    amount = float(input("Enter the Deposit Amount:"))
    if amount < 0 :
       print("--------------")
       print("Invalid Amount")
       print("--------------")
       return 0
    else:
       return amount
    
def withdraw(balance):
    amount = float(input("Enter the Withdraw Amount:"))
    if amount > balance:
       print("---------------------------")
       print("Your Balance is Insufficent")
       print("---------------------------")
       return 0 
    elif amount < 0:
       print("--------------------")   
       print("Amount must be Valid")
       print("--------------------")
       return 0
    else:
       return amount

def main():
   balance = 0 
   running = True
   while running:
     print("--------------------------")
     print("---WELCOME TO AXIS BANK---")
     print("--------------------------")
     print("1.SHOW BALANCE")
     print("2.DEPOSIT AMOUNT")
     print("3.WITHDRAW AMOUNT")
     print("4.QUIT")
     print("--------------------------")
    
     choice = input("Enter a choice(1-4):")
    
     if choice =='1':
       show_balance(balance)
   
     elif choice =='2':
        balance +=deposit()

     elif choice =='3':
        balance -= withdraw(balance)

     elif choice =='4':
        running = False

     else:
        print("----------------------------------")
        print("Please Select your Input b/w (1,4)")
        print("----------------------------------")

main()
print("---------------------------")
print("---THANK YOU VISIT AGAIN---")
print("---------------------------")