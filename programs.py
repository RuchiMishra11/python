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


#QUIZE GAME:
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers=("C","D","A","A","B")
guesses=[]
score=0
questions_num=0

for question in questions:
    print("--------------------------")
    print(question)
    for option in options[questions_num]:
        print(option)
    
    guess=input("Enter your option:[A,B,C,D]: ").upper()
    guesses.append(guess)
    if guess==answers[questions_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questions_num]} is the correct answer!")
    questions_num+=1
   
print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%") 

questions=("1.Largest planet in our galaxy?",
          "2.Largest country in the world?",
          "3.Longest river in the world?",
          "4.Longet moutain in the world?")
options=(("A.Earth", "B.Mars", "C.Jupiter", "D.Saturn"),
         ("A.China", "B.USA", "C.Russia", "D.India"),
         ("A.Amazon", "B.Nile", "C.Ganga", "D.Yangtze"),
         ("A.Everest", "B.K2", "C.Andes", "D.Alps"))
answers=("C","C","A","C")
guesses=[]
score=0
question_num=0
for question in questions:
    print("------------------------")
    print(question)

    for option in options[question_num]:
        print(option)
    
    guess=input("Enter your answer(A,B,C,D):").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
    else:
        print(f"{answers[question_num]} is the correct answer.")
    question_num+=1

print("-----------------------")
print("        RESULT         ")
print("-----------------------")
print("Answers: ")
for answer in answers:
    print(answer,end=" ")
print()

print("Your guesses: ")
for guess in guesses:
    print(guess,end=" ")
print()

your_score=int(score/len(questions)*100)
print(f"You have scored {your_score}%")

# Food stall program
manu={"pizza":299,
      "burger":250,
      "coke":150,
      "ice-Cream":120,
      "soda":90,
      "fries":150,
      "cup-cake":160,
      "cold-coffee":99}
total=0
cart=[]
#printing cart
print("Wellcome to our food stall!")
print("This is our Manu!")
print("------- MANU -------")
for items ,price in manu.items():
    print(f"{items.capitalize():12}:Rs.{price}")
print("-------------------")
# taking order
while True:
    item=input("Enter the food you would like to order from the manu (q to stop):").lower()
    if item=="q":
        print("Exiting..")
        break
    elif manu.get(item)!=None:
        cart.append(item)
print("----- Your orders -----")
for item in cart:
    total+=manu.get(item)
    print(f"{item.capitalize():12}:Rs.{manu.get(item)}")
print(f"{"Total":12}:Rs.{total}")
print("Thanks for the orders!")
    


#library membership program
library_member={"Rahul", "Priya", "Aman", "Neha"}
print("""====== Library Membership ======

1. Show all members
2. Add a new member
3. Remove a member
4. Check if a member exists
5. Exit""")
permission=input("Enter do you wanna contine?(yes/no): ")

while permission=="yes":
    print("continuing...")
    task=input("Enter which task you wanna do from above list: ")
    if task=="1":
        print(library_member)
    elif task=="2":
        name=input("Enter the name of new member: ")
        if name not in library_member:
            library_member.add(name)
            print("Added!")
        else:
            print("Already exist as member.")
    elif task=="3":
        name=input("Enter name you wanna remove: ")
        if name in library_member:
            library_member.discard(name)
            print("Removed successfully!")
        else:
            print("Member is not found!")
    elif task=="4":
        name =input("Enter name you wanna search:")
        if name in library_member:
            print("Member exists!")
        else:
            print("Member does not exist.")
    elif task=="5":
        print("Exit!")
        break
    else:
        print("This task is not found in our system!")
    permission=input("Enter do you wanna contine?(yes/no): ")
else:
    print("Existing...")