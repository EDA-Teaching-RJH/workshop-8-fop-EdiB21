import re

phone_input = input("Enter your UK phone number: ")

phone_formatted = r"^07\d{9}$"

if re.search(phone_formatted, phone_input):
    print("Valid Number")
else:
    print("Invalid Number")