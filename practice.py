#COUNTDOWN TIMER PROGRAM
import time 
import os
my_time=int(input("Enter the time: "))
for x in range(my_time,0,-1):
    second=x%60
    minute=(x//60)%60
    hour=(x//3600)

    os.system("cls")
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

#SHOPPING CART PROGRAM
items=[]
prices=[]
total=0
while True:
    item=input("Enter the items (done to stop):")
    if item.lower()=="done":
        break
    else:
        price=float(input("Enter the price of the item:$"))
        items.append(item)
        prices.append(price)

print("\n----------- SHOPPING BILL -----------")
print("{:<20} {:>10}".format("Item", "Price ($)"))
print("-------------------------------------")

for i in range(len(items)):
    print("{:<20} {:>10.2f}".format(items[i], prices[i]))
    total += prices[i]

print("-------------------------------------")
print("{:<20} {:>10.2f}".format("TOTAL", total))
print("-------------------------------------")
