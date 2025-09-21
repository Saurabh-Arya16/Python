# Program to validate user
while True:
    username = "user123"
    password = "pass123"
    
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    
    if (input_username == username) and (input_password == password):
        print("Login successful!")
        break
    else:
        print("Login failed! Please check your username and password.")
        