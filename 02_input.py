# input = A function which prompt the user to enter data 
#         Written the entered data as string
name_1= input("what is your name?:")
age_1= int(input("how old are you ?:"))
age_1+=1
print(f"hello,{name_1}!")
print("HAPPY BIRTHDAY!")
print(f"you are {age_1} years old.")
#practice problem 1 :  calculating area of rectangle 
length=int(input(" enter length of the rectangle:"))
breadth=int(input("enter breadth of the rectangle:"))
area=length*breadth
print(f"Area of the rectangle : {area}cm²")
# practice problem 2: calculating the bill
item= input("what you want to buy ? :")
price= float(input("what is its price ? :"))
quantity= int( input ("how much do you want ?:"))
total=price*quantity
print(f""" your bill
          item : {item} 
       quantity: {quantity}
          price: {price}
          total: ${total}""")


# madlibs game: a game where you create a story with some missing words and  then
# commplete the story by receiving words from user
adjective1=input("Enter your adjective1 :")
adjective2=input("Enter your adjective2 :")
adjective3=input("Enter your adjective3 :")
print(f"""     my story     
      born as a {adjective1} human. Live as
      a {adjective2} human. Die as a {adjective3} human.""")

noun=input("Enter your name:")
adjective1=input("Enter your  age:")
adjective2=input("Enter your one quality:")
gender=input("Enter whether are you a girl or a boy :")
adjective3=input("Enter where you live :")

print(f""" my name is {noun}.
      i am {adjective1} years old.
      i am  a {adjective2} {gender}. 
      i live here in {adjective3}""")

#chat gpt practice problem 

# Practice Problem 1: Create a BMI Calculator
"""Ask the user for their name, age, weight (kg), and height (m).
Calculate BMI = weight / (height * height).
Print the result in a neat sentence."""
name=input("Enter your name :")
age=int(input("Enter your age:"))
weight=float(input("Enter your body weight:"))
height=float(input("Enter your height:"))
height_square=height*height
bmi=weight/height_square
print(f" hello {name}! i hope you are doing well! your bmi as per the data you have entered is {bmi}")


# Practice Problem 2: Create a Bill Splitter
"""Ask the user for the total bill, number of people, and tip percentage .
Calculate the per-person share.
Print how much each person should pay."""
bill_amount=float(input("Enter the bill ammount:"))
number_of_people=int(input("Enter number of people:") )
tip_percentage=int(input("Enter the tip percentage:"))
tip_amount=tip_percentage/100*bill_amount
total_bill=tip_amount+bill_amount
a=total_bill/number_of_people
print(f"Bill ammount paid by each person is ${a}.")


# Practice Problem 3: Create a Student Report Generator
"""Ask the user for name, age, roll number, and marks in 3 subjects.
Calculate the total and average marks.
Print a report in a neat format."""
name=input("Enter your name :")
age=int(input("Enter your age:"))
roll_number=int(input("Enter your roll number:"))
mark_in_maths=float(input("Enter your marks in mathematics:"))
mark_in_physics=float(input("Enter your marks in physics:"))
marks_in_chemistry=float(input("Enter your marks in chemistry:"))
total_marks=mark_in_maths+mark_in_physics+ marks_in_chemistry
average_marks=total_marks/3
print(f"""----- Student Report -----
Name: {name}
Age: {age}
Roll No: {roll_number}
Total Marks: {total_marks}
Average: {average_marks}
--------------------------
 """)