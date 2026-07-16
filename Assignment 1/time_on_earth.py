print("TIME ON EARTH")
#ask to print time on Earth
second = int(input(f"Input a time in seconds:\n"))
#ask the user to input a time in second
Totalminutes = second //60
Totalhour = Totalminutes // 60
remainingsecond =  second % 60
#calculate remaining secs
remainingminute = Totalminutes % 60
#calculate remaining minutes
print(f"\nThe time on Earth is {Totalhour} hours {remainingminute} minutes and {remainingsecond} seconds.")
