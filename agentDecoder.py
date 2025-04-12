import re
phones = []
emails = []

data = """
Agent Zero: Email - zero99.spy@mail.com, Phone: +44 7700 900321
Ignore this line -- totally irrelevant.
AGENT: John. Contact - (020) 7946 0958. Hidden ID: j.doe_007@cia.int
Do NOT share: Agent *X*, phone: 07900 112233, email: agentx@secrets.co.uk
Random Text 12345 - agent009_email@agency.org / Phone: 07899 443322
secret code: 'ALPHA'
"""

# extracting phone numbers
phoneNo = re.compile(r"\+44\s\d{4}\s\d{6}|\(\d{3}\)\s\d{4}\s\d{4}|\d{5}\s\d{6}")
pFormat = phoneNo.findall(data)
phones.extend(pFormat)


# extracting email addresses
emailAdd = re.compile(r"[a-zA-z0-9._]+@[a-zA-z0-9.]+")
eFormat = emailAdd.findall(data)
emails.extend(eFormat)


# redacting agent names and secret code
agent = re.sub(r"Zero|John|\*X\*|'ALPHA'", "[REDACTED]", data)


# printing emails, phone numbers and redacted lines
print()
print("EMAILS".center(26, '-'))
for email in emails:
    print(email)

print()
print("PHONE NUMBERS".center(26, '-'))
for phone in phones:
    print(phone)

print()
print("REDACTED LINES".center(26, '-'))
print(agent)