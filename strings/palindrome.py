
text = "racecar"
if text[:] == text[::-1]:
    print("A palindrome")

left = 0
right = len(text)-1
is_pal = False
while left < right:
    if text[left] != text[right]:
        print("This is not a palindrome")
        is_pal = True
        break
    left+=1
    right-=1
else :
    print("It is a plaindrom")
    
if not is_pal:
    print("It is a palindrome...")
