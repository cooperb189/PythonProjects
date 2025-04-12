import pyinputplus as pi

# Celsius to Kelvin
def celKel(temp):
    global tempCK
    tempCK = temp + 273.15
    return tempCK  

# Celsius to Fahrenheit
def celFah(temp):
    global tempCF
    tempCF = (temp * 1.8) + 32
    return tempCF

# Fahrenheit to Celsius
def fahCel(temp):
    global tempFC
    tempFC = (temp - 32) * 5 / 9
    return tempFC

# Fahrenheit to Kelvin
def fahKel(temp):
    global tempFK
    tempA = ((temp - 32) * 5) / 9
    tempFK = tempA + 273.15
    return tempFK

# Kelvin to Fahrenheit
def kelFah(temp):
    global tempKF
    temp0 = (temp - 273.15) * 9 / 5
    tempKF = temp0 + 32
    return tempKF

# Kelvin to Celsius
def kelCel(temp):
    global tempKC
    tempKC = temp - 273.15
    return tempKC

# MAIN PROGRAM LOOP
while True:
    print ("""
        Temperature Conversion Tool:

       Press 1 for Celsius to Kelvin
       Press 2 for Celsius to Fahrenheit
       Press 3 for Fahrenheit to Celsius
       Press 4 for Fahrenheit to Kelvin
       Press 5 for Kelvin to Celsius 
       Press 6 for Kelvin to Fahrenheit
""")

    option = input("Please choose which temperature conversion you would like to make: ").strip()

# TEMP CONVERSION OPTIONS
# OPTION 1
    if option == '1':
        num = pi.inputNum("Please enter the temperature you want to convert - from Celsius to Kelvin: ")
        celKel(num)
        print (tempCK)

# OPTION 2
    elif option == '2':
        num = pi.inputNum("Please enter the temperature you want to convert - from Celsius to Fahrenheit: ")
        celFah(num)
        print (tempCF)

# OPTION 3    
    elif option == '3':
        num = pi.inputNum("Please enter the temperature you want to convert - from Fahrenheit to Celsius: ")
        fahCel(num)
        print (tempFC)

# OPTION 4
    elif option == '4':
        num = pi.inputNum("Please enter the temperature you want to convert - from Fahrenheit to Kelvin: ")
        fahKel(num)
        print (tempFK)

# OPTION 5
    elif option == '5':
        num = pi.inputNum("Please enter the temperature you want to convert - from Kelvin to Celsius: ")
        kelCel(num)
        print (tempKC)

# OPTION 6
    elif option == '6':
        num = pi.inputNum("Please enter the temperature you want to convert - from Kelvin to Fahrenheit: ")
        kelFah(num)
        print (tempKF)

# ERROR HANDLING
    else:
        print ("Invalid input, please enter a valid option.")
        continue