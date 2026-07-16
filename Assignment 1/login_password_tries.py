secretusername = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
password = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111", "apple", "hello", "admin"]
#initial the attempts to 0 and maxattempts to 3
attempts = 0
max_attempts = 3

while attempts < 3:
    username = input("Enter username: ")
    word = input("Enter password: ")
#if username in secretusername and word in password
    if username in secretusername and word in password:
        print(f"Login successful. Welcome {username} !")
        break
    else:
#give user to try attemepts 3 time if password or username and password then can success login
        attempts = attempts + 1
        remaining_attempts = max_attempts - attempts
        if attempts < 4:
            print(f"Login incorrect. Tries left: {remaining_attempts}")
        else:
            break
