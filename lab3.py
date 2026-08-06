print("***College Admission Eligibillity Cheaker***")

age = int(input("Enter age:"))
marks = float(input("enter marks:"))

if age >= 19 and age <= 27:
    print("elligible for college addimision:")

    
    if marks >= 65:
        print("elligible for college addmission:")

        if marks >= 85:
                 print("AIML Department:")

        elif marks >= 75:
                 print("CSE Department:")
   
        else:
                 print("General Department:") 

    else:
            print("not elligible for college addmision based on marks:")
else:
     print("addmision is not elligible based on age:")    
