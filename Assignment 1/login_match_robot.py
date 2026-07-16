# Define lists to store valid usernames and passwords
secret = {"Ava": "12345", "Leo": "abcde", "Raj": "pass1", "Zoe": "qwert", "Max": "aaaaa", "Sam": "zzzzz", "Eli": "11111", "Mia": "apple", "Ian": "hello", "Kim": "admin"}


robotagain = ["n"]
robotstop = ["Y",""]
def login():
    attempts = 3
    while attempts != 0:
        
        username = input("Enter username: ")
        password = input("Enter password: ")


        # Check if username exists and password is correct
        if username in secret and secret[username] == password:
            print(f"Login successful. Welcome {username} !")
            break
        else:
            attempts -= 1
            if attempts >= 0:
                print(f"Login incorrect. Tries left: {attempts}")
        while attempts == 0:
#ask user are you a robot
            robot = input("Are you a robot (Y/n)? ")
            if robot in robotstop:
                break
            elif robot in robotagain:
                return login()
            else:
                continue

login()
