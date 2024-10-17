name= str ("name")
section= input("section")

grade_1= int(input("Enter your prelims: "))
grade_2= int(input("Enter your midterm: "))
grade_3= int(input("Enter your finals: "))
total = (grade_1 + grade_2 + grade_3)

if 40 >= total <=100:
    
elif total >= 99:    
    print(round(total), "Your grade point is 1.00 - Excellent")
elif total >= 96: 
    print("Your grade points is 1.25 - Outstanding")
elif total >= 93: 
    print("Your grade points is 1.50 - Superior")
elif total >= 90: 
    print("Your grade points is 1.75 - Very Good")
elif total >= 87: 
    print("Your grade points is 2.00 - Good")
elif total >= 84: 
    print("Your grade points is 2.25 - Satisfactory")
elif total >= 81: 
    print("Your grade points is 2.50 - Fairly Satisfactory")
elif total >= 78: 
    print("Your grade points is 2.75 - Fair")
elif total >= 75:
    print("Passed- ")
elif total <75:
    print("failed")
    