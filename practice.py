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


# PROJECT: STUDENT RESULT SYSTEM
"""Features:
Take multiple students
Store marks in 2D list
Display formatted result
Calculate total & average"""
student_info=[]
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter student name: ")
    English=int(input("Enter the marks scored in English: "))
    Mathematics=int(input("Enter the marks scored in Mathematics: "))
    science=int(input("Enter the marks scored in Science: "))
    student_info.append([name,English,Mathematics,science])
print("/n----------Student information----------")
print("{:<5} {:<8} {:<8} {:<12} {:<7}".format("Name","English","Mathematics","Science","Total"))
print("-----------------------------------------")

    
for s in student_info:
    total=s[1]+s[2]+s[3]
    print("{:<5} {:<8} {:<8} {:<12} {:<7}".format(s[0],s[1],s[2],s[3],total))


