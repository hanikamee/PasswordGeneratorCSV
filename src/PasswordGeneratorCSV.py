# This project uses OOP to generate a randomly shuffled password and saves it to a CSV file.

import csv
import string
import random

class Password:
    
    # Constructor 
    def __init__(self) -> None:
        # Public variables
        self.csv_path = 'passwordgeneration.csv'
        self.password = ''
        
    def generate(self) -> str:
        
        password_length = int(input("Please enter the desired length for your password (must be at least 5 characters): "))

        # input validation 
        while password_length < 5:
            print("Your password length is too short")
            password_length = int(input("Please enter the desired length for your password (must be at least 5 characters): "))

        # string.printable includes lowercase and uppercase letters, numbers, and printable symbols
        password_characters = list(string.printable.strip(" \t\n\r\x0b\x0c"))
    
        # Shuffling increases the randomness and unpredictability 
        random.shuffle(password_characters)

        password = []
        for x in range(password_length):
            password.append(random.choice(password_characters))
    
        # Shuffling the password to enhance its security
        random.shuffle(password)
    
        # Using list comprehension to convert the password from list to string
        password = ''.join([str(s) for s in password])
        
        self.password = password
        
    # Writing the password to the CSV file. Returning indicates whether the
    # operation succeeded or not    
    def store(self, password, name) -> bool:
        print("opening ", self.csv_path)
        with open(self.csv_path, 'a', newline = '') as csv_file:
            writer = csv.writer(csv_file, delimiter = ',')
            writer.writerow([name, password])
            return 0
        return 1
    
def main():
    
    running = True
    while running:
        print("Enter 'exit' at any moment to exit the program")
        if(name := input('Enter your desired name: ').lower()) == 'exit':
            print("You have successfully exited the program")
            break
        
        password = Password()
        password.generate() # Calling the generate function
        print(f'The newly generated password for {name} is {password.password}')
        
        if (save_password := input("Would you like the password and username to be saved? (y/exit): ").lower()) == 'y':
            if password.store(password.password, name) == 0:
                print("Your password was successfully saved!")
            else:
                print('Error!')
        
        elif save_password.lower() == 'exit':
            print("You have successfully exited the program")
            running = False
        
        else:
            print("You entered an invalid command!")
            
if __name__ == '__main__':
    main()
