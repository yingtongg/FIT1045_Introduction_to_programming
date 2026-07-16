# List of usernames that are allowed to input
secretusername = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
def loginsuccessfull(secretusername):
#Create an empty list to store login data or attempts    
    store =[]

def main():
    while True:
# ask user enter their username
        username = input("Enter username: ")
#Verify if the entered username is in the list of allowed usernames
        if username in secretusername:
            print(f"Login successful. Welcome {username} !")
#if login successful then exit loop
            break
        else:
            print("Login incorrect.")
#return main
main()


