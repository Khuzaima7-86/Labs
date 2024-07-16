list1=[]
while(True):
   binary_num= input("Enter 4 digits Binary number: (Enter -1 to break)")
   if(binary_num=="-1"):
       break
   decimal_num=int(binary_num,2)
   if decimal_num%5==0:
       list1.append(binary_num)
print(list1)
