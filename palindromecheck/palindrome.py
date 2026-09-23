

strring = input("Enter a string: ")
lengthstring = len(strring)
left = 0
right = lengthstring - 1
#reversed_string = ""
#indexx = lengthstring - 1
"""
BUILD THE REVERSE STRING

for i in range(indexx,-1,-1):
    reversed_string += strring[i]
if reversed_string == strring:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

"""

#TWO-POINTER STRATEGY

while left < right:
    if strring[left] == strring[right]:
        left += 1
        right -= 1
    else:
        print("It is not a palindrome")
        break
else:
    print("It is a palindrome")
