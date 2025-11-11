password=input("Enter your password: ")
while not (len(password)>8 and password.isalnum() and any(ch.upper() for ch in password)):
    print("Your password is invalid.")
    password=input("Enter your password again : ")
print("wellcome!")
