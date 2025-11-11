#logical operator: used in  conditional statement 
#And operator=check if two or more condition is true 
#Or operatore= check if atleast one condition is true 
# Not= false if condition is true and vise versa

tem=int(input("Enter temperature:"))
if tem > 0 and tem<30:
    print("Temperature is normal.")
else:
    print("Temperature is not normal.")

if tem<0 or tem>30 :
    print("Temperature is not normal.")
else:
    print("Temperature is normal")

for_sale=True
if for_sale:
    print(" This is for sale.")
else:
    print("This is not for sale.")

    
if not for_sale:
    print(" This is  for  sale.")
else:
    print("This is not   for sale.")

#Chat gpt practice problems 
#practice problem 1:Voting Eligibility Checker
age=int(input("Enter your age:"))
status=input("Are you a citizen of this country?(Yes , No):")
if age>=18 and status=="yes":
    print("You are eligible to  vote.")
else :
    print("You are not eligible to vote. ")

#practice problem 2:Dicount Eligibility Checker
"""A person gets a discount if they are either a student OR a member of the shop."""
is_student=input("Are you a student? (Yes/No):")
is_member= input("Are you a member?:(Yes/No):")
if is_student=="Yes" or is_member=="Yes":
    print("Congrates! You are eligible for discount. ")
else:
    print("Sorry! you are not eligible for discount.")

#practice problem 3: Login System with Lock
username=input("Enter your user name:")
password=int(input("Enter your password:"))
if username=="admin"and password==123456:
    print("Access granted!")
else :
    print("Access denied!")

# practice problem 4: exam eligibility checker 
attendance=int(input("Enter your attendance:"))
medical_certificate=input("Do you have a medical certificate ? (Yes/No):")
if attendance>=75 or medical_certificate=="Yes":
    print("You are eligible for the exam.")
else:
    print("You are not eligible for the exam.")

# leap year checker
year=int(input("Enter the year:"))
if year%4==0 and year%100 !=0:
    print(f"Year {year} is a leap year.")
else:
    print(f"Year{year} is not a leap year.")

# dicount checker problem :2
total_amount=int(input("Enter the total shoping amount:"))
is_member=input("Are you a member ? (yes/no):")
if total_amount>=5000 or is_member=="yes":
    print("Dicount applied!")
else:
    print("You are not eligible for the dicount.")

# Temperature checker:
temperature=int(input("Enter temperature in celcius: "))
if temperature<15:
    print("It's cold !")
elif temperature>=15 and temperature<=30:
    print("It's warm!")
else:
    print("It's hot !")
    