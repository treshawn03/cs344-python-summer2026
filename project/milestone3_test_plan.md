# Milestone 3 Test Plan

## Overview and Scope

This milestone tests the current version of my login authentication program. The program asks the user to enter a username and password, checks the information against the correct login credentials, and displays whether the login was successful. The program also tracks failed login attempts and locks the account after three incorrect attempts.

The purpose of this test plan is to verify that correct credentials are accepted, incorrect credentials are rejected, multiple attempts are handled properly, and the account-locking feature works as expected.

## Test Environment

- Computer: MacBook Pro
- Operating System: macOS
- Python Version: Python 3
- Code Editor: Visual Studio Code
- Execution Method: Local VS Code terminal
- Program File: `project_main.py`

## Test Cases

| Test # | Description | Input Values | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Correct username and password on first attempt | Username: `admin`; Password: `python123` | Program displays `Login successful!` and ends | Program displayed "Login successful" and ended | Pass | 
| 2 | Correct username with incorrect password, followed by correct credentials | First: `admin` / `wrong`; Second: `admin` / `python123` | First attempt fails, second attempt succeeds, and program ends | Program displayed "incorrect username or password." on the first attempt, then "Login successful!" on the second attempt. | Pass|
| 3 | Incorrect username with correct password, followed by correct credentials | First: `user` / `python123`; Second: `admin` / `python123` | First attempt fails and second attempt succeeds | Program displayed "incorrect username or password." on the first attempt, then "Login successful!" on the second attempt. | Pass |
| 4 | Incorrect username and incorrect password, followed by correct credentials | First: `guest` / `password`; Second: `admin` / `python123` | First attempt fails and second attempt succeeds | Program displayed "incorrect username or password." on the first attempt, then "Login successful!" on the second attempt. | Pass |
| 5 | Three incorrect login attempts | `user1` / `wrong1`, `user2` / `wrong2`, `user3` / `wrong3` | Program displays an incorrect-login message after each attempt and locks the account after the third attempt | Project displayed an incorrect username/password message after each failed attempt and locked the account after the third login. | Pass |
| 6 | Correct credentials entered on the third attempt | Two incorrect attempts, then `admin` / `python123` | Program accepts the third attempt and does not lock the account | Project rejected the first two attempts, accepted the correct credentials on the third attempt, and did not lock the account. | Pass |
| 7 | Username entered with incorrect capitalization | Username: `Admin`; Password: `python123`, followed by correct credentials | Capitalized username is rejected because the comparison is case-sensitive | Program rejected the capitalized username because the login is case-sensitive, then accepted the correct lowercase credentials. | Pass |
| 8 | Password entered with incorrect capitalization | Username: `admin`; Password: `Python123`, followed by correct credentials | Capitalized password is rejected because the comparison is case-sensitive | Program rejected the password with incorrect capitalization, then accepted the correctly capitalized password. | Pass |
| 9 | Blank username and password, followed by correct credentials | First attempt left blank; Second: `admin` / `python123` | Blank values are rejected and the correct second attempt succeeds | Program rejected blank username and password, then accepted the correct credentials on the second attempt. | Pass |
| 10 | Username containing extra spaces, followed by correct credentials | First: ` admin ` / `python123`; Second: `admin` / `python123` | Username with spaces is rejected because spaces are not removed | Program rejected the username with extra spaces, then accepted the correctly entered username on the second attempt. | Pass |

## Findings and Next Steps

The testing process will determine whether the login validation, retry loop, and account-locking features work correctly. Any failed tests will be documented with the actual behavior that occurred.

Possible future improvements include hiding the password while it is entered, removing accidental spaces from user input, allowing usernames without case sensitivity, and storing login credentials more securely instead of placing them directly in the source code.