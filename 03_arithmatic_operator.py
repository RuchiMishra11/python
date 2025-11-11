# Assignment operator 
friends=10
# friends = friends + 1
# friends += 1
# friends = friends 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends 2
# friends **= 2
remainder = friends % 2 #we can use this to check whether a number is even or odd
print(remainder)        #  when the number is even we get 0 when we find number %2 when odd we get 1  
#another example 
money=2
# money=money+1
money+=1 
print(money)  #3
money-=1 
print(money)  #2
money*=3 
print(money)  #6
money/=2 
print(money)  #3
money%=3 
print(money)  #0
money**=3 
print(money)  #0
# some built in maths related functions 
x=6
y=3.5
z=-5
round_fun=round(y) #round function 
print(round_fun) #4
absolute_fun= abs(y) #absolute function  : distance between number and the 0 on the number line
print(absolute_fun)  #3.5 
print(abs(z))        #5
print(abs(x))        #6
power_fun= pow(3 ,4 ) # power function 
print(power_fun) #81
print(pow(5,3))  #125
max_fun=max(x ,y ,z) # maximum function calculate maximum value amongs the values
print(max_fun)     #6
print(max(5,6,6.1)) #6.1
print(max(-2,-1,-14)) #-1
min_fun=min(x ,y,z)  # minimum function find the  minimum value amongs the  values
print(min_fun) #-5
print(min(-3,-9,0) ) #-9
print(min(6,2,5))    # 2
import math
print(math.pi)
print(math.e)
print(math.sqrt(169)) # use  to find out the square root of a number  
print(math.ceil(9.4))  #round of to higher digit
print(math.ceil(99.8))
print(math.floor(6.9)) #round off  to lower digit 
print(math.floor(9.0))
#excercise
# practice problem 1: calculate the circumference of the circle 
radius=float(input("Enter the radius of the circle:"))
circumfrence=2*math.pi*radius
print(f"Circumfrence of the circle with radius {radius}cm is {round(circumfrence,1)}cm.")

# practice problem 2: calculate the area of circle 
radius=float(input("Enter the radius of the circle:"))
area= math.pi * pow(radius,2)
print(f"Area of the circle with radius {radius}cm is {round(area,2)}cm²")
  
#practice problem 3:find the hypoteneous of a right angle triangle 
height=int(input("Enter the height of  right angled triangle:"))
base=int(input("Enter the base of the right angled triangle:"))
a=pow(height,2)+pow(base,2)
hypoteneous=math.sqrt(a)
print(f" The hypoteneous of the given triangle with height {height}cm and base {base}cm is {hypoteneous}cm.")

#chat gpt practice problem 
# practice problem 1: Create square,cude and squareroot calculator 
number=int(input("Enter your number:"))
square_of_number= number**2
cube_of_number=number**3
squareroot= math.sqrt(number)
print(f"""........all about number........
square of the number:   {square_of_number}
cube of the number  :    {cube_of_number}
squareroot of the number: {squareroot}
.......................................""")

# Practice Problem 6: Create a Simple Marks Grader

"""Ask the user for marks out of 100.
Use assignment operators to add 5 bonus marks.
Print whether the final score is:
≥90 → “Excellent”
70-89 → “Good”
50-69 → “Pass”
<50 → “Fail” """
marks=int(input("Enter your marks :"))
marks+=5
if marks>=90:
    print("Excellent")
elif marks>=70:
    print("Good")
elif marks>=50:
    print("pass")
else:
    print("Fail") 

#python calculator
operator=input("Enter a arithmatic operator(+,-,/,*):")
num_1=float(input("Enter your first number:"))
num_2=float(input("Enter your second number:"))
if operator=="+":
    print(round(num_1+num_2))
elif operator=="*":
    print(round(num_1*num_2))
elif operator=="-":
    print(round(num_1 - num_2))
elif operator=="/":
    print(round(num_1/num_2))
else:
    print(f"Operator {operator} you have entered is not valid!")