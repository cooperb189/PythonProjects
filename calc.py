# Simple Calculator 
import pyinputplus as pi

# function to perform the calculation
def calc(number, operator, number2):
    if operator == '+':
        return number + number2
    if operator == '-':
        return number - number2
    if operator == '/':
        return number / number2
    if operator == 'x':
        return number * number2

# function for further calculation
def calc2(operator, number2):
    if operator == '+':
        return answer + number2
    if operator == '-':
        return answer - number2
    if operator == '/':
        return answer / number2
    if operator == 'x':
        return answer * number2

# prompting the user to enter the details to perform the calculation
while True:
    try:
        num = pi.inputNum(prompt="Enter a number: ", limit=3, blank=False)
        op = pi.inputMenu(['+', '-', '/', 'x'], limit=3, blank=False)   
        num1 = pi.inputNum(prompt="Enter a number: ", limit=3, blank=False)
        answer = (calc(num, op, num1))
        print(answer)

# additional calculation as well as exit option
        while True:
            try:
                op2 = pi.inputMenu(['+', '-', '/', 'x'], limit=2, blank=False)   
                num3 = pi.inputNum(prompt="Enter a number: ", limit=2, blank=False)
                answer = calc2(op2, num3)
                print(answer)
            except:
                yo = pi.inputNum(prompt="Press 1 to restart calculator | Press 2 to close the program: ", min=1, max=2)
                if yo == 1:
                    break
                else:
                    quit()

# Error handling in case the limit is met
    except pi.RetryLimitException:
        response = pi.inputYesNo("Would you like to continue? : ").lower()
        if response == 'yes':
            continue
        else:
            quit()

