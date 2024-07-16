list1=[]

while(True):
    txt=input("Enter nothing to terminate\nEnter String:")
    if txt=="":
            break
    else:
        list1.append(txt.lower())
print(list1)
