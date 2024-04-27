import time

#Secret code = GDSCPUP

def main():
    print("Welcome to my Personal Details!\n")
    
    while True:
        code = input("Before proceeding, please type the secret code: ")
        
        print("Initializing the data...\n")
        time.sleep(1)

        if code.lower() == "gdscpup":
            print("Access secured...\n")
            time.sleep(2)
            
            print("Ella Mae D. Lumawag")
            print("A 2nd Year Computer Engineering Student")
            print("Let's Go Software Development Team")
            
            time.sleep(2)
            print("\nSuccess. Thank you!")
            
            break
        
        else:
            print("Access Denied. Try again.\n")
            main()
            break
        
main()