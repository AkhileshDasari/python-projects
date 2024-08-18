principal = 0
rate = 0 
time = 0 
while principal <= 0 :
     principal = float(input("Enter the principal: "))
if principal <= 0 :
   print("principal must not be less then or equal to zero")

while rate <= 0 :
   rate = int(input("Enter the rate of interest: "))
if rate <= 0 :
   print("rate must not be less then or equal to zero")

while time <=0 :
    time = int(input("Enter the time in years: "))
if time<=0 :
   print("time must not be less then or equal to zero")
   #print(principal)
   #print(rate)
   #print(time)
final_amount = round(principal * pow((1 + rate/100), time), 2)
print(f"your final amount after {time} year's is {final_amount}")


