#TIME MODULE:
import time 
"function() that we can use while using time module."
#1. time.sleep(1):pauses the program for the given number of seconds (accepts decimals too).
"Mostly used in countdown timer"
time_=int(input("Enter the number of seconds:"))
for x in range(1,time_):
    
    print(x)
    time.sleep(1)
print("Done!")

#countdown program
import os
my_time=int(input("Enter the time: "))
for x in range(my_time,0,-1):
    second=x%60
    minute=(x//60)%60
    hour=(x//3600)

    os.system("cls")
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)


#2. time.time():Returns the number of seconds elapsed since January 1, 1970 (a fixed reference point programmers call "the epoch") —
#  not human-readable on its own, but extremely useful for measuring elapsed time. (Elapsed Time = End Time - Start Time)
"Mostly used to calculate how much time  a code takes to get excecuted."
start_time=time.time()
total=0
for i in range(10000):
    total+=i
end_time=time.time()
print(f"Sum:{total}")
print(f"Time Taken to calculate:{end_time-start_time:.4f}seconds")

start_time=time.time()
answer="amazon"
question=input("What's most largest forest in world?:").lower()
while question!=answer:
    print("Wrong answer,please try again!")
    question=input("What's most largest forest in world?:").lower()
end_time=time.time()
print(f"Time you took to give the correct  answer is {end_time-start_time:.4f} seconds.")

#3. time.ctime() — human-readable current date/time  (If you want something people can actually read not epoch time )
"usefull when u want to display current time time well formated"
print(time.ctime())

#OS MODULE:

import os 
#os.system(command) — run a system/terminal command (note: whenever a os execute some cammand successfully it print zero otherwise other no)
print(os.system("echo Hello from terminal!")) #print whatever comes after echo..............
print(os.system("date /t")) #print date
print(os.system("cd")) #list the name of current folder
#os.system("clear") or os.system("cls") clear the window (same  command that you used in  terminal of window)
print(os.system("dir")) #list the files in the current folder
#os.name: print the  name of desktop operating system  # 'nt' on Windows, 'posix' on Linux/Mac
print(os.name) 

#os.getcwd() — get current working directory
print(os.getcwd())

#os.listdir(path):list files/folders in a directory

#5. os.path.exists(path) — check if a file/folder exists Prints True if exists otherwise False
print(os.path.exists(r"/home/claude")) #false

#RANDOM MODULE:
import random
#1. random.random() — a random decimal between 0 and 1(not used frequently but other function are  build on this idea)
print(random.random()) # always between 0.0 and 1.0 (never exactly 1.0)

#2. random.randint(a, b) — a random whole number, both ends included
print(random.randint(1,10)) # any whole number from 1 to 10, INCLUDING both 1 and 10 unlike range(1,10)

#3. random.choice(sequence) — pick one random item from a list/tuple/string DOESN'T WORK NOT SET AND DICTIONARY
print(random.choice("hello")) # pick any random letter
print(random.choice(["apple","orange","gauva","pears"]))
print(random.choice(("riya","sia","Gia")))
l=["rock","paper","scissors"]
computer_move=random.choice(l)
print(computer_move)

# 4. random.shuffle(list) — rearrange a list randomly, in place
cards=[2,3,4,5,6,7,8,9,10,"k","q","a","j"]
random.shuffle(cards)
print(cards)

#5. random.sample(sequence, k) — pick multiple UNIQUE random items, without repeats
sequence=[1,2,3,20,4,5,5,6,8,7,8,9]
print(random.sample(sequence,2))
print(random.sample(sequence,4))
print(random.sample(sequence,7))

"""Note:random.choice() called multiple times: if you called random.choice(numbers) three separate times, you could get
 the same number twice (like your 'grape' repeat above). random.sample() guarantees no duplicates within a single call."""

# 6. random.uniform(a, b) — a random decimal between two numbers Like randint, but for decimals instead of whole numbers.
print(random.uniform(1,60))
print(random.uniform(1,2))
print(random.uniform(1,10))

#progams:
# Quiz game - shuffle question order
questions = ['Q1', 'Q2', 'Q3', 'Q4']
random.shuffle(questions)
print('Shuffled question order:', questions)

# Pick 3 random 'winners' from a list of names, no duplicates
names = ['Ravi', 'Sam', 'Tia', 'Zoe', 'Om']
winners = random.sample(names, 3)
print('Winners:', winners)

import random
import time
#Number guessing program 
start=time.time()
secret_number=random.randint(1,100)
count=0
while True:
    number=int(input("Enter a secret number:"))
    count+=1
    if number>secret_number:
        print("Too high!")
    elif number<secret_number:
        print("Too low!")
    else:
        print(f"You have guessed right! The Correct Number is {secret_number}")
        break
    
end=time.time()
print(f"The no  of guesses and time you took is {count} and {end-start:.1f} seconds respectively.")

# ROCK PAPER SECISSOR GAME 
import random 
options=("rock","paper","secissor")
score=0
print("----------------GAME STARTS---------------- ")
playing=True
while playing:
    player_choice=None
    computer_choice=random.choice(options)

    while player_choice not in options:
        player_choice=input("Enter  your choice (rock ,paper,secissor):")
        print(f"Your choice :{player_choice} ")
        print(f"Computer choice:{computer_choice}")

    if computer_choice==player_choice:
        print("It's a tie!")
    elif player_choice=="paper" and computer_choice=="rock":
        print("You win!")
        score+=1
    elif player_choice=="secissor" and computer_choice=="paper":
        print("You win!")
        score+=1
    elif player_choice=="rock" and computer_choice=="secissor":
        print("You win!")
        score+=1
    else:
        print("You lose!")

    play_again=input("Do you wanna play (yes/no):").lower()
    while not(play_again=="yes" or play_again=="no"):
        play_again=input("Please enter yes/no:")
    if play_again=="yes":
        pass 
    else:
        playing=False

    
print("Thanks for playing !")
print(f"Your score is {score}")
print("----------------GAME OVER---------------- ")

