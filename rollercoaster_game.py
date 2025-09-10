print("Wellcoe to rollercoaster")
height = int(input("What is ur hieght in cm"))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("Enter your age "))
    
    if age < 12:
        bill = 5
        print("CHild ticket pay $5")
    
    elif age <= 18  :
        bill = 7
        print(" YOuth pay 7$")
    elif age >= 45 and age <=55:
        print("Everything will be free")    
    else:
        bill = 12
        print(" Adult pay $12")
    wants_photo = input("Do you want photo ")
    if wants_photo =="Y":
        bill =+ 3
    print(f"Your finale bill is {bill}")

else:
    print("sorry, you have to grow taller before you ride")
