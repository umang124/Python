# Sample data
users_data = [
    ("1", "admin1", "admin"),
    ("2", "student1", "student"),
    ("3", "student2", "student"),
]

passwords_data = [
    "adminpassword1",
    "studentpassword1",
    "studentpassword2",
]

grades_data = [
    ("2", "Math: A, Science: B, English: A, History: C, Geography: B"),
    ("3", "Math: B, Science: A, English: B, History: B, Geography: A"),
]

eca_data = [
    ("2", "Sports: Football, Debate Club: Member"),
    ("3", "Music: Piano, Drama Club: President"),
]

# Write data to users.txt
with open('users.txt', 'w') as file:
    for user_data in users_data:
        file.write(','.join(user_data) + '\n')

# Write data to passwords.txt
with open('passwords.txt', 'w') as file:
    for password in passwords_data:
        file.write(password + '\n')

# Write data to grades.txt
with open('grades.txt', 'w') as file:
    for grade_data in grades_data:
        file.write(','.join(grade_data) + '\n')

# Write data to eca.txt
with open('eca.txt', 'w') as file:
    for eca_entry in eca_data:
        file.write(','.join(eca_entry) + '\n')

print("Sample data generated successfully.")
