# Simple Authentication System
 
## Exercise 1: User Authentication System
### Objective: Implement a basic user authentication system.

Instructions:

User Registration:

Ask the user to input a username and password.
Store the username and a hashed version of the password in a dictionary.
Save the dictionary to a file (users.txt) using file handling.

User Login:

Ask the user to input a username and password.
Verify the username and password by checking the stored dictionary.
Use conditional statements to validate the login credentials.
Error Handling:

If the file doesn't exist when trying to read the user data, handle the FileNotFoundError and create a new file.
Handle incorrect login attempts and raise custom exceptions if the username is not found or the password is incorrect.
