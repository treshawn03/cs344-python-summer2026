def get_login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password


def check_login(username, password):
    correct_username = "admin"
    correct_password = "python123"

    if username == correct_username and password == correct_password:
        return True
    else:
        return False


def display_result(success):
    if success:
        print("Login successful!")
    else:
        print("Incorrect username or password.")


failed_attempts = 0
max_attempts = 3

while failed_attempts < max_attempts:

    username, password = get_login()

    success = check_login(username, password)

    display_result(success)

    if success:
        break

    failed_attempts += 1

    if failed_attempts == max_attempts:
        print("Account locked. Too many failed login attempts.")