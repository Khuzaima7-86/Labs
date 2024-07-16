list1=[6,19,17,23,38,45,77,84,90]
num=int(input("Enter a number to find: "))
loc=False
list1.sort()
print(list1)
low = 0
high = len(list1) - 1
while low <= high:
    mid = (low + high) // 2
    if list1[mid] == num:
        loc=True
        break
    elif list1[mid] < num:
        low=mid+1
    elif list1[mid]> num:
        high=mid-1
if loc==True:
    print(f"{num} is found at index {mid}")   
else:
    print(f"{num} is not found in list")


