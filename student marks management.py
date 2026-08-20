# student marks management system

marks = []

while True:
    print("\n--- Student Marks Management Systeam ---")
    print("1. Insert Marks")
    print("2. Display Marks")
    print("3. Upadate marks")
    print("4. Delete Marks")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    # Insertion
    if choice == 1:
        mark = int(input("Enter student marks: "))
        marks.append(marks)
        print("marks inserted successfully.")
        
    # Traversal
    elif choice == 1:
        if len(marks) == 0:
            print("No marks available.")
        else:
            print("student marks:")
            for i in range(len(marks)):
                print("student",i + 1, ":", marks[i])
                
    # Updating
    elif choice == 3:
        student = int(input("Enter student marks to update: "))
        if 1 <= student <= len(marks):
            new_marks = int(input("Enter new marks: "))
            marks[student - 1] = new_marks
            print("Marks uodated successfully.")
        else:
            print("Invallid student number.")
            
    # Deletion
    elif choice == 4:
        student == int(input("Enter student number to delete: "))
        if 1 <= student <= len(marks):
            marks.pop(student - 1)
            print("Marks deleted successfully.")
        else:
            print("Invallid student number.")
            
    # Exit
    elif choice == 5:
        print("Program ended.")
        break
    
    else:
        print("Invallid choice.")                            
                           
    
