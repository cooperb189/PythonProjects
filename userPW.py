import pyinputplus as pi
import re, os
from pathlib import Path

os.chdir(r'C:\Users\work\python\txtFiles\userPW')   # Setting file CWD for simplicity and a list to store all users data.
allUsers = []

### PART 1: CREATING THE USER'S LOGIN CREDENTIALS AND STORING THE DATA

## FUNCTIONS - functions for error handling in case of any typos.
def nameCheck(n):
    if re.search(r'[a-zA-Z]\s[a-zA-z]', n):
        return True
    else:
        return False

def emailCheck(e):
    if re.search(r"^[a-zA-Z0-9._+-]+@[a-zA-Z0-9-]+\.([a-z]|[a-z]\.[a-z])+$", e):
        return True
    else:
        return False

def userCheck(un):
    if 5 <= len(un) < 20:
        if re.search(r'^[a-z][a-z0-9-_.]*$', un):
            return True
        else:
            return False
    else:
        return False

def passCheck(pw):
    if len(pw) > 8:
        if re.search(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9])', pw):
            return True
        else:
            return False
    else:
        return False

## MAIN PROGRAM LOOP
while True:
    users = {}

    while True:
        name = input("Enter your full name: ").title().strip()
        cleanName = name.replace(" ", "_").lower().strip()      # Loop that allows the user to enter their full name and
        if nameCheck(name) == True:                             # then stores that data into the 'users' dictionary.
            users['Full Name'] = name
            break
        else:
            print("Please enter your full name (eg. 'John Doe').")
            continue 

    while True:
        email = input("Enter your email address: ")
        if emailCheck(email) == True:
            users['Email Address'] = email              # Loop that allows the user to enter their email address
            break                                       # and then stores that data into the 'users' dictionary.
        else:
            print("Invalid email, please try again.")
            continue

    while True:
        username = input("Enter a username: ")
        if userCheck(username) == True:
            users['Username'] = username        # Allows the user to enter their username and yet 
            break                               # again stores that info into the dictionary.
        else:
            print("Invalid username")
            continue 

    while True:
        password = pi.inputPassword("Enter a password: ")
        pass2 = pi.inputPassword("Re-enter your password: ")
        if password != pass2:                                   # Repeating the loop process with setting their password
            print("Password doesn't match, try again.")         # and then storing it into the dictionary.
            continue
        else:
            if passCheck(password) == True:
                users['Password'] = password                # Double password check to ensure accuracy.
                break
            else:
                print("Password Requirements".center(30, '-'))
                print("1) Password must be a minimum of 8 characters.")                     # Instructions for a solid password
                print("2) Password must contain both uppercase and lowercase characters.")  # in case a weak one is entered
                print("3) Password must contain one or more digits.")
                print("4) Password must contain one or more special characters.")
                continue

    with open(rf'{cleanName}.txt', 'w') as file:
        for k, v in users.items():                    # All the users inputted data is stored into their own file for retention.
            file.write(f"{k}: {v}\n")

    allUsers.append(users)                  # Adding the dictionary of data into the list to store the data.

# EXIT OPTION
    exitOption = pi.inputYesNo("Would you like to create another user? : ").lower().strip()
    if exitOption == 'yes':
        continue                        # Including an extra option to exit the program in
    else:                               # case they don't want to make another account.
        break
