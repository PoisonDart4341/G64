import random

def print_help():
    print("Available")
    print("help - Find usable commands")
    print("version - Find software version")
    print("credits - People who helped")
    print("diceroll - Roll a dice")
    
def print_version():
    print("Python64 GitHub Prototype")
    
def print_credits():
    print("Coder - Gavin Pardee")
    print("Programming Language - Python")
    print("Programming Application - Thonny")
    
def print_diceroll():
    list1 = [1, 2, 3, 4, 5, 6]
    print(random.choice(list1))
    
    
def process_command(command):
    if command == "diceroll":
        print_diceroll()
    elif command == "credits":
        print_credits()
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
    print("******* Python64 GitHub Prototype *******")
    print("Please type a command")
    main()