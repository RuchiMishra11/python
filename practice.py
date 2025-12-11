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

# Concession stand program
menu={"pizza":3,
      "popcorn":8,
      "soda":4,
      "coke":4,
      "burger":5,
      "lemonade":3,
      "nachos":5,
      "potato Chips":6}
total=0
cart=[]
print("----------MENU----------")
for k,v in menu.items():
    print(f"{k:13}:${v:.2f}")
print("-------------------------")
while True:
    food=input("Enter the food items(q to stop): ").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("-------YOUR ORDER ---------")

for food in cart:
    total+=menu.get(food)
    print(food,end=" ")
print()

print(f"Your total bill: ${total:.2f}")
print("-------------------------")
