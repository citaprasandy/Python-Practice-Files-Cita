def encrypt(text):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c) + 3) % len(charSet)] for c in text])
    return encText

def decrypt(text):
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\\}]{[\"':;?/>.<, "
    decText = "".join([charSet[(charSet.find(c) - 3) % len(charSet)] for c in text])
    return decText

def choice1():
    # Collect user input for storing personal details
    credentials = input("\nEnter your credentials: ")
    password = input("\nEnter your password: ")
    
    # Encryption key starts here
    encrypted_password = encrypt(password)
    url = input("\nEnter your url: ")
    
    # Open file in append mode and write the collected information
    with open("file.txt", "a") as f:
        f.write(credentials + "   " + encrypted_password + "   " + url + "\n")
    print("\nYour new details have now been stored\n")

def choice2():
    # Local variable: "border"
    border = "|"
    print(f"\n{border}{'Credentials' : ^20}{border}{'Password' : ^20}{border}{'URL' : ^20}{border}")
    print("----------------------------------------------------------------")

    try:
        with open("file.txt", "r") as f:
            data = f.read()  # 'data' now contains the contents of the file as a string
      
            
            # Check if there's any data and display a corresponding message
            if data.strip():  # Use strip() to remove any extra whitespace
                
                # Display formatted table if there's data
                dataList = data.strip().split('\n')
                for line in dataList:
                    fields = line.strip().split('   ')
                    if len(fields) == 3:
                        # Decrypt the password for display
                        decrypted_password = decrypt(fields[1])
                        print(f"{border}{fields[0] : ^20}{border}{decrypted_password : ^20}{border}{fields[2] : ^20}{border}")
                print("\nAll data has now been displayed\n")
            else:
                print("No data.")
                
    except FileNotFoundError:
        print("\nNo data found. Please store some details first.\n")

# Main menu starts here

# Give the user some context.
print("\nClick on the menu below:")

# Set an initial value for choice other than the value for 'quit'.
choice = ''

# Start a loop that runs until the user enters the value for 'quit'.
while choice != 'q':
    # Give all the choices in a series of print statements.
    print("[1] Enter 1 to store personal details.")
    print("[2] Enter 2 to view your stored credentials.")
    print("[q] Enter q to quit.")
    
    # Ask for the user's choice.
    choice = input("\nMake your choice: ")
    
    # Respond to the user's choice.
    if choice == '1':
        choice1()
    elif choice == '2':
        choice2()
    elif choice == 'q':
        print("\nExiting the menu\n")
    else:
        print("\nInvalid option, please try again.\n")

# Print a message that we are all finished.
print("Program has been closed.")

