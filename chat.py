userName = raw_input("What is your name? ")
message = raw_input("Enter a message: ")

while message != "exit":
    print userName + ": " + message
    message = raw_input("Enter a message: ")
    
