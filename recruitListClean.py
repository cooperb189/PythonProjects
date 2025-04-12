# RECRUITMENT LIST CLEANER
"""
You've been given a messy recruitment email with info from multiple applicants. Your job is to:
- Extract valid phone numbers and normalize them to +44XXXXXXXXXX
- Extract valid email addresses
- Ignore bad/incomplete data
- Return unique results (no duplicates)
"""
############################################################################################################

import re 

# messy data to clean up
data = """
Applicant 1: Name: Sarah Johnson  
Contact: 07982 345 944, Email: sarah.j@email.com

Applicant 2: Jack R. - Tel: 0208-456-7890  
Email: jackR123@company.org

Applicant 3: +44 2084567890, Email: emergency_contact@help-now.io  
Old Email: not-an-email@domain  

Applicant 4: 0781234567
Email: cheems.doge+back@gmail.com

Duplicate Entry: 07982 345 944 | jackR123@company.org

Invalid Contacts: 1234, 0208 345 789 (too short)  
Email: doge@email (incomplete)
"""

phones = []
emails = []

# function to sort phone numbers
def numFormat(phoneNo):
    for num in phoneNo:
        num = re.sub(r"^0", "+44", num)
        num = re.sub(r"[ -]", "", num)
        phones.append(num)
    return phones

# extracting the phone numbers
phoneNum = re.compile(r"\d{5}\s\d{3}\s\d{3}|\d{4}-\d{3}-\d{4}|\+44\s\d{10}")
phoneFormat = list(set(phoneNum.findall(data)))
numFormat(phoneFormat)

# extracting the email addresses
emailAdd = re.compile(r"[a-zA-z0-9._+]+@[a-zA-z0-9.-]+\.[a-zA-z0-9]+")
emailFormat = list(set(emailAdd.findall(data)))
emails = emailFormat

# printing the extracted information
no = 1
no1 = 1
print()
print ("PHONE NUMBERS".center(30, '*'))
for phone in phones:
    print (f"Phone number {str(no)} ".ljust(15, '-') + (f" {phone}".rjust(15, '-')))
    no += 1
print()
print ("EMAIL ADDRESSES".center(30, '*'))
for email in emails:
    print (f"Email address {str(no1)} ".ljust(15, '-') + (f" {email}".rjust(15, '-')))
    no1 += 1
print()