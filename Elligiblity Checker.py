#### 10. Eligibility Checker:

#Create a program that checks a person’s eligibility for a job based on these conditions:

#- Age: Must be between 18 and 60.
#- Experience: Must have 2+ years of experience.
#- Qualification: Must have a degree (ask yes or no).




age = int(input("Enter your age"))
exp = int(input("Enter your experience"))
quali = (input("Do you have qualificaton? yes/no"))

if(age >=18 and age<60 and exp>2 and quali=="yes" ):
    print("you are elligible")

