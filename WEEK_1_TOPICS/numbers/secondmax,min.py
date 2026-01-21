#check for the second largest and minimum
arr = [10,2,3,4,9,20]
maximum = arr[0]
minimum = arr[0]
smaximum = 0
sminimum = 0

for i in arr:
    if i > maximum:
        if i > smaximum:
                smaximum = i
        smaximum = maximum
        maximum = i
    
    else:
        if i < minimum:
         sminimum = minimum
         minimum = i
        else:
            if i < sminimum :
                sminimum = i

print("second maximum is : ", smaximum)
print("second minimum is : ", sminimum)

