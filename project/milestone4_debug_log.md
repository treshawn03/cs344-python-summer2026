## Bug 1 – Login Validation Was Not Checking Both Fields Correctly

### Description

One issue I ran into was making sure the program checked both the username and password before allowing a successful login. I wanted the login to succeed only when both values matched the correct credentials.

### Context

This happened in the `check_login()` function inside `project_main.py` while I was testing different username and password combinations.

### Symptoms

Some test combinations were not giving the result I expected. This made me realize I needed to carefully check the condition that compared the entered username and password.

### Root Cause and Fix

The problem was in the login condition. I reviewed the comparison and made sure it used `and` so both the username and password had to match before the function returned `True`.

### Debugging Process

I tested the function using the correct username with a wrong password, a wrong username with the correct password, and both correct values. Testing each combination separately helped me confirm that the login condition was working correctly.

## Bug 2 – Failed Login Attempts Were Not Being Counted Correctly

### Description

Another issue I had was making sure failed login attempts were counted correctly. The program was supposed to allow only three failed attempts before locking the account.

### Context

This issue appeared in the main loop of `project_main.py` while I was testing repeated incorrect usernames and passwords.

### Symptoms

During testing, I noticed that the number of failed attempts did not always match what I expected. I needed to make sure the counter increased only after an unsuccessful login.

### Root Cause and Fix

The problem was related to where `failed_attempts += 1` was placed in the loop. I reviewed the order of the statements and made sure the counter only increased after `check_login()` returned `False`.

### Debugging Process

I used small test cases by intentionally entering incorrect credentials several times and keeping track of the attempts by hand. This helped me compare what the program was doing with what I expected. After correcting the counter logic, I tested it again and confirmed that the account locked after the third failed attempt.

## Bug 3 – Successful Login Did Not Stop the Retry Loop

### Description

One issue I worked through was making sure the program stopped asking for login information after the user entered the correct credentials. Once a login was successful, I wanted the program to end the retry loop immediately.

### Context

This issue involved the `while` loop in `project_main.py` while I was testing a correct login after entering incorrect credentials.

### Symptoms

Without the correct loop control, the program could continue through the retry process even after a successful login. This was not the behavior I wanted.

### Root Cause and Fix

The issue was related to controlling when the `while` loop should stop. I added the `if success:` condition followed by `break` so a successful login immediately exits the loop.

### Debugging Process

I traced the loop one attempt at a time and tested an incorrect login followed by a correct login. This helped me see when the loop should continue and when it should stop. After adding the `break`, I tested the same sequence again to confirm that the program ended the retry process after a successful login.

## Bug 4 – Account Lockout Message Appeared at the Wrong Time

### Description

Another issue I encountered was getting the account lockout message to display at the correct time. I wanted the message to appear only after the user failed all three allowed login attempts.

### Context

This issue occurred in the main loop of `project_main.py` while I was testing three incorrect login attempts in a row.

### Symptoms

The lockout message was not displaying at the point I expected during my testing. This made me check how the failed attempt counter was connected to the lockout condition.

### Root Cause and Fix

The problem involved the condition that checked `failed_attempts` against `max_attempts`. I made sure the failed attempt counter increased first and then checked whether it had reached the maximum of three attempts before displaying the lockout message.

### Debugging Process

I tested the program by intentionally entering incorrect credentials three times and tracing the value of `failed_attempts` after each attempt. This helped me verify exactly when the condition became true. After adjusting the order of the logic, I ran the same test again and confirmed that the lockout message appeared after the third failed login.

## Bug 5 – Login Result Message Did Not Match the Login Outcome

### Description

The last issue I worked through involved making sure the correct message displayed after each login attempt. I wanted the program to clearly show either a successful login message or an incorrect username or password message.

### Context

This issue was connected to the `display_result()` function in `project_main.py` while I was testing both successful and unsuccessful login attempts.

### Symptoms

During testing, I needed to make sure the message shown to the user matched the value returned by `check_login()`. If that value was handled incorrectly, the wrong message could be displayed.

### Root Cause and Fix

The issue was related to how the `success` value was passed into `display_result()`. I checked the function logic and made sure `True` displayed the successful login message while `False` displayed the incorrect username or password message.

### Debugging Process

I tested the program once with the correct credentials and again with incorrect credentials. I compared the returned result with the message printed in the terminal. Testing both outcomes helped me confirm that `display_result()` was responding correctly.

## Reflection and Patterns

One pattern I noticed while working through these bugs was that most of my problems came from the order of the program logic and making sure each condition happened at the correct time. Testing smaller sections made it much easier to figure out where something was going wrong instead of changing several things at once.

In future projects, I plan to test each function as I create it instead of waiting until the entire program is finished. I also want to test both correct and incorrect user inputs more often and keep my functions separated so problems are easier to isolate. These steps should help me catch errors earlier and make debugging less frustrating.
