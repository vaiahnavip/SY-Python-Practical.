name = input("Enter student name :")

marks1 = float(input("Enter marks for subject 1 :"))
marks2 = float(input("Enter marks for subject 2 :"))
marks3 = float(input("Enter marks for subject 3 :"))

total  = marks1 + marks2 + marks3
average = total  / 3

print("--------STUDENT RECORD---------")

print("student name :", name)
print("subject 1 :", marks1)
print("subject 2 :", marks2)
print("subject 3 :", marks3)

print("------------------------------")

print("Total marks :", total)
print("Average = %2f" % average)