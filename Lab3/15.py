password=input("Enter password: ")
i=0
alphacount=0
numericcount=0
charcount=0
if len(password) >= 6 and len(password) <= 16:
    while i < len(password):
        if alphacount == 0 and password[i].isalpha():
            alphacount += 1
        if numericcount == 0 and password[i].isdigit():
            numericcount += 1
        if charcount == 0 and (password[i] == '$' or password[i] == '#' or password[i] == '@'):
            charcount += 1
        i += 1
    else:
        if alphacount > 0 and numericcount > 0 and charcount > 0:
            print("Password is valid")
        else:
            print("Password must contain at least one alphabet, one numeric digit, and one special character ($, #, @)")
else:
    print("Password length should be between 6 and 15 characters")
