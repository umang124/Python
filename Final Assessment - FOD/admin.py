from student import Student
from user import User
import uuid

class Admin(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username, "admin")
    
    def show_admin_dashboard(self):
                
        print("Admin Dashboard")
        print("1. Register a new user")
        print("2. Modify user record")
        print("3. Delete user record")
        
        option = input("Enter your choice: ")
        
        if option == '1':
            username = input("Enter new user's username: ")
            password = input("Enter new user's password: ")
            role = input("Enter new user's role (admin/student): ")       
            self.register_user(username, password, role)
            
        elif option == '2':
            user_id = input("Enter user ID to modify: ")
            new_username = input("Enter new username: ")
            self.modify_user(user_id, new_username)
            
        elif option == '3':
            user_id = input("Enter user ID to delete: ")
            self.delete_user(user_id);
        else:
            print("Invalid option.")            
    
    def register_user(self, username, password, role):
        with open('users.txt', 'r') as file:
            num_users = sum(1 for line in file)

        user_id = num_users + 1
        if role == 'admin':
            user = Admin(user_id, username)
        elif role == 'student':
            user = Student(user_id, username)

        if user:            
            try:
                with open('passwords.txt', 'a') as file:
                    file.write(password + '\n')
                with open('users.txt', 'a') as file:
                    file.write(f"{user_id},{username},{role}\n")
                print("User registered successfully.")
            except FileNotFoundError:
                print("Error: Files not found.")
        else:
            print("Invalid role.")

    def modify_user(self, user_id, new_username):
        try:
            # Read the contents of the file
            with open('users.txt', 'r') as file:
                lines = file.readlines()

            # Find the line corresponding to the user ID and modify the username
            found = False
            for i, line in enumerate(lines):
                parts = line.strip().split(',')
                if parts[0] == str(user_id):
                    lines[i] = f"{user_id},{new_username},{parts[2]}\n"  # Replace old username with new_username
                    found = True
                    break

            if not found:
                print("User not found.")
                return

            # Write the modified content back to the file
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            print(f"Username for user ID {user_id} modified successfully.")

        except FileNotFoundError:
            print("Error: Users file not found.")

    def delete_user(self, user_id):
        try:
            # Read the contents of the file
            with open('users.txt', 'r') as file:
                lines = file.readlines()

            # Find the line corresponding to the user ID and remove it
            found = False
            for i, line in enumerate(lines):
                parts = line.strip().split(',')
                if parts[0] == str(user_id):
                    del lines[i]
                    found = True
                    break

            if not found:
                print("User not found.")
                return

            # Write the modified content back to the file
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            print(f"User with ID {user_id} deleted successfully.")

        except FileNotFoundError:
            print("Error: Users file not found.")


    
    def count_users():
        # Read the contents of the file
        with open("users.txt", 'r') as file:
            lines = file.readlines()

        # Count the number of users
        num_users = len(lines)

        return num_users
