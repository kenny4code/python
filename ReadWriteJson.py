import json


# Exercise 1: Read Json file

file_input = 'C:\\file_path\\students.json' 
file_output = 'C:\\file_path\\students_output.json'

# Load the JSON data
with open(file_input, 'r') as file:
   students = json.load(file)

# Print the entire list
print(students)
print(f'Total students: {len(students)}')

# Access individual student data
total_match_score = 0
for student in students:
    print(f"\n******* Student: {student['id']} *************")
    print(f"Name: {student['name']}, Age: {student['age']}")
    print(f"Math: {student['grades']['math']}, Sciene: {student['grades']['science']}")
    total_match_score = total_match_score + student['grades']['math']

print(f'Average math score: {total_match_score/len(students)}')

# Exercise 2: Add 1 more student and print out result 
student4 = {
    "id": 4,
    "name": "Ken",
    "age": 25,
    "grades": {
        "math": 90,
        "science": 95
    }
}



students.append(student4)

# Exercise 3: Write students to Json file

# Save to file
with open(file_output, 'w') as file:
    json.dump(students, file, indent=4)



# Exercise 3: Ask user to enter student info and then append to students file and save 
id = int(input("Please enter student id: "))
name = input("Please enter student name: ")
age = int(input("Please enter student age: "))
math_grade = int(input("Please enter math grade: "))
science_grade = int(input("Please enter science grade: "))

new_student = {
    "id": id,
    "name": name,
    "age": age,
    "grades": {
        "math": math_grade,
        "science": science_grade
    }
}

print(new_student)

students.append(new_student) 

# Print the entire list
print(students)

# Save to file
with open(file_output, 'w') as file:
    json.dump(students, file, indent=4)


# Exercise 4: Calculate Average Math Grades
print(f'Average math score: {total_match_score/len(students)}')



# Exercise 5: Update a Student's Grade of Student 1
for student in students:
    if student["name"] == "Bob":
        student["grades"]["math"] = 100
        break
print("****** Students after grade updated *****8")
print(students)




# Exercise 6: Delete a Student by ID 2
for i, student in enumerate(students):
    if student["id"] == 2:
        del students[i]
        break
print(students)