txt=input("Enter string: ")
Letters=0
Digits=0
for i in range(len(txt)):
    if txt[i].isalpha():
        Letters+=1
    elif txt[i].isnumeric():
        Digits+=1
print("Letters: ",Letters)
print("Digits: ",Digits)