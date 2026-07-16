print("TIME ON EARTH")
#ask the user to input a time in second 
second = int(input(f"Input a time in seconds:\n"))
Totalminutes = second //60
Totalhour = Totalminutes // 60
remainingsecond =  second % 60
remainingminute = Totalminutes % 60
#print total hour , remaining minute and remaining second
print(f"\nThe time on Earth is {Totalhour} hours {remainingminute} minutes and {remainingsecond} seconds.")

print(f"\nTIME ON TRISOLARIS")
trisolarissec = int(input(f"Input the number of seconds in a minute on Trisolaris:\n"))
trisolarismin = int(input(f"Input the number of minutes in an hour on Trisolaris:\n"))
Totalminutes = second // trisolarissec
Totalhour = Totalminutes // trisolarismin
remainingsecond =  second % trisolarissec
remainingminute = Totalminutes % trisolarismin
print(f"\nThe time on Trisolaris is {Totalhour} hours {remainingminute} minutes and {remainingsecond} seconds.")
