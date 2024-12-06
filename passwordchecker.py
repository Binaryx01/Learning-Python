''' 6. Password Strength Checker:

Ask the user to input a password and check its strength:

- Less than 6 characters: Weak
- 6-12 characters: Medium
- More than 12 characters: Strong
'''


password = input('Enter your password')
x =len(password)
if(x<6):
    print("weak password")
elif(x>6 and x<12):
    print("medium password")
else:
    print("strong password")
    
