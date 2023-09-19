ampersand = -1;
while ampersand == -1:
    email = input("Enter your e-mail:").strip()
    ampersand = email.find("@")
    if ampersand == -1:
        print("Invalid input.")
    
username =email[0:ampersand]
domain = email[ampersand+1:]
print("Your username is:", username)
print("Your domain is:", domain)
