import re

# long form text for me to extract data from.
clientData = """
Client 1:
John Doe - Mobile: 07982 345 944
Email: john.doe+sales@gmail.com

Client 2:
Jane Smith - Tel: 0208-456-7890 (Office)            
Email: j.smith@londonoffice.co.uk

Client 3:
Emergency Contact - 07982345944 or +44 2084567890
Backup Email: emergency_contact@help-now.io

Client 4:
Old contact: 0781234567 (disconnected)  
Email: bad_email@domain (invalid, ignore this one)
"""
# lists to store extracted information.
phone = []
email = []

# write a function to format all numbers into +44XXXXXXXXXX
def phoneNo(number):
    for num in number:
        num = re.sub(r"^0", "+44", num)
        num = re.sub(r"[ -]", "", num)
        phone.append(num)

# regular expressions to extract necessary phone numbers and append them to the list
numFormat = re.compile(r"\d{5}\s\d{3}\s\d{3}|\d{11}|\+44\s\d{10}|\d{4}-\d{3}-\d{4}")
numFind = numFormat.findall(clientData)
phoneNo(numFind)
print (phone)

# regular expressions to extract necessary email addresses and append them to the list
emFormat = re.compile(r"[a-zA-z0-9.+_]*@[a-zA-z0-9.-]+\.[a-zA-z0-9.-]+")
emFind = emFormat.findall(clientData)
email = emFind
print(email)
