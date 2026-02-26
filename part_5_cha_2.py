import re

student_id = input("Please enter your student ID: ")

id_formatting = r"^[a-zA-Z]{4}\d{4}$"

if re.search(id_formatting, student_id):
    print("Valid ID")
else:
    print("Invalid ID")