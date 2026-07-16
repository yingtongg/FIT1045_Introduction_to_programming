print("TIME ON EARTH")
second = int(input(f"Input a time in seconds:\n"))

# Calculate total minutes and hours on Earth
Totalminutes = second // 60
Totalhours = Totalminutes // 60

# Calculate remaining seconds and minutes
remainingsecond = second % 60
remainingminute = Totalminutes % 60

# Print Earth time in hours, minutes, and seconds
print(f"\nThe time on Earth is {Totalhours} hours {remainingminute} minutes and {remainingsecond} seconds.")

# Print introductory message for Trisolaris time
print(f"\nTIME ON TRISOLARIS")

# Get input for Trisolaris time conversion
trisolarissec = int(input(f"Input the number of seconds in a minute on Trisolaris:\n"))
trisolarismin = int(input(f"Input the number of minutes in an hour on Trisolaris:\n"))

# Convert Earth seconds into Trisolaris time
Totalminutes = second // trisolarissec
Totalhours = Totalminutes // trisolarismin

# Calculate remaining seconds and minutes on Trisolaris
remainingsecond = second % trisolarissec
remainingminute = Totalminutes % trisolarismin

# Print Trisolaris time in hours, minutes, and seconds
print(f"\nThe time on Trisolaris is {Totalhours} hours {remainingminute} minutes and {remainingsecond} seconds.")

# Print introductory message for Trisolaris time after waiting
print("\nTIME AFTER WAITING ON TRISOLARIS")

# Get input for waiting duration on Trisolaris
durationinsolaris = int(input("Input a duration in seconds:\n"))

# Calculate total seconds after waiting
totalsecondsafterwaiting = second + durationinsolaris

# Convert the new total seconds into Trisolaris time
Totalminutesafterwaiting = totalsecondsafterwaiting // trisolarissec
Totalhoursafterwaiting = Totalminutesafterwaiting // trisolarismin

# Calculate remaining seconds and minutes after waiting on Trisolaris
remainingsecondafterwaiting = totalsecondsafterwaiting % trisolarissec
remainingminuteafterwaiting = Totalminutesafterwaiting % trisolarismin

# Print the updated Trisolaris time after waiting
print(f"\nThe time on Trisolaris after waiting is {Totalhoursafterwaiting} hours {remainingminuteafterwaiting} minutes and {remainingsecondafterwaiting} seconds.")

