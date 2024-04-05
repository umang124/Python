# user_manager.py

from admin import Admin
from student import Student

class UserManager:
    def __init__(self):
        self.users = []
    
    def load_data(self):
        try:
            # Load data from users.txt
            with open('users.txt', 'r') as file:
                for line in file:
                    user_id, username, role = line.strip().split(',')
                    if role == 'admin':
                        self.users.append(Admin(user_id, username))
                    elif role == 'student':
                        self.users.append(Student(user_id, username))

            # Load data from passwords.txt
            with open('passwords.txt', 'r') as file:
                passwords = file.readlines()

            # Load data from grades.txt
            with open('grades.txt', 'r') as file:
                grades_data = file.readlines()

            # Load data from eca.txt
            with open('eca.txt', 'r') as file:
                eca_data = file.readlines()

            # Assign grades and ECA details to respective users
            for i, user in enumerate(self.users):
                user_id = str(i + 1)
                for grades_entry in grades_data:
                    if grades_entry.startswith(user_id):
                        grades = grades_entry.strip().split(',')[1]
                        user.grades = grades
                for eca_entry in eca_data:
                    if eca_entry.startswith(user_id):
                        eca_details = eca_entry.strip().split(',')[1]
                        user.eca_details = eca_details
        except FileNotFoundError:
            print("Error: One or more files not found.")
            
    
    def login(self, username, password):
        for user in self.users:
            if user.username == username:
                # Assuming passwords are stored in a separate file
                try:
                    with open('passwords.txt', 'r') as file:
                        passwords = file.readlines()
                        password = password.strip()
                        if passwords[self.users.index(user)].strip() == password:
                            return user
                        else:
                            return None
                except FileNotFoundError:
                    print("Error: Password file not found.")
                    return None
        return None
    
    