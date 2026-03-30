from datetime import datetime

name = input("Enter your name: ")

age = 21          
gpa = 3.71         
is_student = True 

# current date and time
current_time = datetime.now()

# welcome message
print("-" * 50)
print(f" Welcome to CPSC 24500, {name}!")
print("-" * 50)

#Welcome/time
print(f"Hello, {name}! Happy your here with us !!!")
print(f"Current date and time: {current_time}")
print("-" * 50)

print(f"Age: {age}")
print(f"GPA: {gpa}")
print(f"Student: {is_student}")
