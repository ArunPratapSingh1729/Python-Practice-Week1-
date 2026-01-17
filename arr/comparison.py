#Check if all elements are same
# check if len are same 

#list,tuple,set,dic can be euqal but not identify

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
arr1 = [1,2,3]
arr2 = [1,2,3]
length1 = len(arr1)
length2 = len(arr2)

a = 2
if arr1.count(a) == 1:
    print("yes the arr contains the number once")
else:
    print("no the arr doesnt contains the number")

if a in arr:
    print("yes it contains the number ",a)
else:
    print("it does not contains the number ", a)

if arr1 == arr2:
    print("yes both of the arrays content are same")
else:
    print('not both are not same')

if len(arr1) == len(arr2):
    print("yes the length of both the arrays are same")

