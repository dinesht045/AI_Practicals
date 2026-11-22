#Student Marks,Percentage,Grade
name=input("Enter the Name of the Student: ")
n=int(input("Enter the no.of subjects:  "))
total=0
for i in range(1,n+1):
    subject=int(input(f"Enter the Marks for Subject {i}: "))
    total+=subject
percentage=total/n
if percentage>=90:
    grade="A+"
    performance="Outstanding"
elif percentage >=80:
    grade="A"
    performance="Excellent"
elif percentage >=70:
    grade="B"
    performance="Very Good"
elif percentage >=60:
    grade="C"
    performance="Good"
elif percentage>=50:
    grade="D"
    performance="Average"
else:
    grade="F"
    performance="Needs Improvement"
print(f"Name: {name}")
print(f"Total: {total}")
print(f"Percentage: {round(percentage,2)} %")
print(f"Grade: {grade}")
print(f"Performane: {performance}")
