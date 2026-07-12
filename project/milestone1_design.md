# Course Project Milestone 1

## Cybersecurity Login Attempt Tracker

## Problem Description

The purpose of this program is to help track login attempts for a user account. The program will ask the user for a username and password, determine whether the login is successful, and keep track of failed login attempts. If too many failed attempts occur, the program can notify the user that the account should be locked or reviewed for security purposes.

The intended users are students, employees, or anyone who wants a simple way to monitor login attempts. This project is useful because it demonstrates basic cybersecurity concepts while also using Python programming skills such as user input, decisions, loops, and functions.

For this project, I will assume that usernames and passwords are entered correctly as text. This version of the program will only simulate login attempts and will not connect to a real database or online account.

## Inputs and Outputs

### Inputs
- Username entered by the user
- Password entered by the user
- Number of failed login attempts

### Outputs
- Login successful message
- Login failed message
- Warning message after multiple failed attempts
- Account locked notification if the maximum failed attempts are reached

### Example

Input:
Username: admin
Password: password123

Output:
Login successful.

Input:
Username: admin
Password: wrongpassword

Output:
Login failed.

## Algorithm Overview

1. Ask the user to enter a username.
2. Ask the user to enter a password.
3. Compare the entered information to the stored username and password.
4. If the information matches, display a successful login message.
5. If the information does not match, increase the failed login attempt counter.
6. If the user reaches the maximum number of failed attempts, display an account locked message.
7. Otherwise, allow the user to try again until they log in successfully or the account becomes locked.

## Planned Structure and Functions

### get_login()
Gets the username and password from the user.
Input: Username and password
Output: Username and password values

### check_login()
Checks whether the username and password are correct.
Input: Username and password
Output: True or False

### display_result()
Displays whether the login was successful, failed, or locked.
Input: Login result
Output: Message displayed to the user 