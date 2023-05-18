def print_help():
    print("Available")
    print("help - Find usable commands")
    print("version - Find software version")
    print("about - About G64-P")
    
def print_version():
    print("G64-P Version 1.0")
    
def print_about():
    print("G(avin Pardee - Creator)(Based off of Commodore)64-P(ython Edition)")
    
def print_credits():
    print("Coder - Gavin Pardee")
    print("Programming Language - Python")
    print("Programming Application - Thonny")
    print("Special Thanks - Samuel Hicks")

def process_command(command):
    if command == "credits":
        print_credits()
    elif command == "about":
        print_about()
    elif command == "version":
        print_version()
    elif command == "help":
        print_help()
    else:
        print("Unknown command")
        print("Please type 'help' for usable commands")
        
def main():
    while True:
        command = input("> ")
        process_command(command)
        
if __name__ == "__main__":
    print("******* G64-P *******")
    print("Please type a command")
    main()
