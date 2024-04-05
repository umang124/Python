# main.py

from user_manager import UserManager
from user import User
from admin import Admin
from student import Student

def main():
    user_manager = UserManager()
    user_manager.load_data()

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        try:
            user = user_manager.login(username, password)
            if user:
                if isinstance(user, Admin):
                    user.show_admin_dashboard()
                elif isinstance(user, Student):
                    user.show_student_dashboard()
                else:
                    print("Invalid user type.")
            else:
                print("Invalid username or password. Please try again.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
