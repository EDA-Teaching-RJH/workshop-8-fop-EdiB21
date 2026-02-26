import re


email = input("What's your email? ").strip()
#username, domain = email.split("@")

#if username and domain.endswith(".ac.uk"):
 #print("Valid")
#else:
    #print("Invalid")


if re.search(r"^\w+@\w.+\.(ac\.uk|gov\.uk|nhs\.net)$", email):  #| acts as an or
    print("Valid")