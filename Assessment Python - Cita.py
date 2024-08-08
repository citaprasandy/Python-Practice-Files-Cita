# Global function starts here 

# Example of encryption key creation logic

def choice1 ():
    # Collect user input for storing personal details
    credentials = input("\nEnter your credentials: ")
    password = input("\nEnter your password: ")
    #Encryption key starts here
    clearText = "myPassword"
    charSet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|}]{[\"':;?/>.<, "
    encText = "".join([charSet[(charSet.find(c) + 3) % 95] for c in clearText])
    print(f"\nEncrypted text: {encText}\n")
     #Encryption key ends here
    url = input("\nEnter your url: ")
        
    # Open file in append mode and write the collected information
    with open("file.txt", "a") as f:
        f.write(f"{credentials}   {password}   {url}   \n")
        
    print("\nYour new details have now been stored\n")

    # Read and display stored credentials from the file
def choice2 ():
    # Local variable: "border"
    border = "|"
    print(f"\n{border}{'Credentials' : ^20}{border}{'Password' : ^20}{border}{'URL' : ^20}{border}")
    print("----------------------------------------------------------------")

    """
    Open "file.txt" in read mode and assign to variable f
    Read the entire content of the file and store it in variable data
    END TRY
    """

    try:
        with open("file.txt", "r") as f:
            data = f.read() # 'data' now contains the contents of the file as a string
            
            # Display the raw content of the file
            print("\nStored credentials:\n")
            print(data)
            
            # Check if there's any data and display a corresponding message
            if data.strip():  # Use strip() to remove any extra whitespace
                print("Below is your credentials:\n")
                
                # Display formatted table if there's data
                dataList = data.strip().split('\n')
                for line in dataList:
                    fields = line.strip().split('   ')
                    if len(fields) == 3:
                        print(f"{border}{fields[0] : ^20}{border}{fields[1] : ^20}{border}{fields[2] : ^20}{border}")
                print("\nAll data has now been displayed\n")
            else:
                print("No data.")
                
    except FileNotFoundError:
            print("\nNo data found. Please store some details first.\n")
        
           

#Main menu starts here

# Give the user some context.
print("\nClick on the menu below:")

# Set an initial value for choice other than the value for 'quit'.

#Global variable: "choice"
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

