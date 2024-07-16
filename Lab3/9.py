list1=[0,1]
i=1
while(True):
    print(i)
    num= list1[i]+list1[i-1]
    if(num>50):
        break
    list1.append(num)
    i+=1
print(list1)