from user import User

class Student(User):
    def __init__(self, user_id, username):
        super().__init__(user_id, username, "student")
    
    def show_student_dashboard(self):
        print("Student Dashboard")
        print("1. Update profile")
        print("2. View ECA details")
        print("3. View grades")
        option = input("Enter your choice: ")
        
        if option == '1':
            new_username = input("Enter new username: ")
            new_password = input("Enter new password: ")
            self.update_profile(new_username, new_password)
        elif option == '2':
            self.view_eca_details()
        elif option == '3':
            self.view_grades()
        else:
            print("Invalid option.")
        
    def update_profile(self, new_username, new_password):
        try:
            # Read the contents of the file
            with open('users.txt', 'r') as file:
                lines = file.readlines()

            # Find the line corresponding to the user ID and modify the username
            found = False
            for i, line in enumerate(lines):
                parts = line.strip().split(',')
                if parts[0] == str(self.user_id):
                    lines[i] = f"{self.user_id},{new_username},{parts[2]}\n"  # Replace old username with new_username
                    found = True
                    break

            if not found:
                print("User not found.")
                return

            # Write the modified content back to the file
            with open('users.txt', 'w') as file:
                file.writelines(lines)

            print(f"Username for user ID {self.user_id} modified successfully.")

        except FileNotFoundError:
            print("Error: Users file not found.")

    def view_eca_details(self):
        try:
            with open('eca.txt', 'r') as file:
                for line in file:
                    parts = line.strip().split(',', 1)  # Split only on the first comma
                    if len(parts) == 2:
                        user_id, eca_str = parts
                        if user_id.strip() == self.user_id.strip():  # Compare stripped user IDs
                            eca_details = {}
                            eca_list = eca_str.split(',')
                            for item in eca_list:
                                activity, detail = item.split(':')
                                eca_details[activity.strip()] = detail.strip()
                            print("ECA details:", eca_details)
                            return
                print("ECA details not found.")
        except FileNotFoundError:
            print("Error: ECA file not found.")

    def view_grades(self):
        try:
            with open('grades.txt', 'r') as file:
                for line in file:
                    user_id, grades = line.strip().split(',')
                    if user_id == self.user_id:
                        print("Grades:", grades)
                        return
            print("Grades not found.")
        except FileNotFoundError:
            print("Error: Grades file not found.")