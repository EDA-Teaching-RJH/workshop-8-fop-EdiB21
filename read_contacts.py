import csv

with open("contacts.csv", "r", newline = "") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(f"Name: {row['name']} , Email: {row['email']}")