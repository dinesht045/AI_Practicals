#Menu-Driven Student Information System
Student={}
def add_student():
    roll=input("Enter Roll No :")
    name=input("enter Name :")
    dept=input("Enter Department :")
    Student[roll]={"Name":name,"Department":dept}
    print("Student added successfully")
 