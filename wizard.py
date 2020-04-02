from os import system
from time import sleep

def main():
    system('clear')
    print("""
#################################################################################################
  ___   ___     ___           ___    _     ___    __      __  _                        _ 
 | _ ) |_ _|   | _ \  _  _   / _ \  | |_  | __|   \ \    / / (_)  ___  __ _   _ _   __| |
 | _ \  | |    |  _/ | || | | (_) | |  _| |__ \    \ \/\/ /  | | |_ / / _` | | '_| / _` |
 |___/ |___|   |_|    \_, |  \__\_\  \__| |___/     \_/\_/   |_| /__| \__,_| |_|   \__,_|
                     |__/                                                               

#################################################################################################
""")
    print("Welcome to the PyQt5 Project Setup Wizard!")
    project_name = input("Please enter your projects' name:  ")
    # Validate
    print("A folder called '{} will be created as your project's root directory".format(project_name))
    short_description = input("Please enter a short description of your project (~100 characters max):  ")
    author_name = input("Please enter the project's author name:  ")
    author_email = input("And his/her CERN email address:  ")
    print("Thank you! Your project is being generated...")
    # Generate project
    sleep(1)
    print("The project is ready. Please run 'charm {}' to open the project in the IDE".format(project_name))

if __name__ == '__main__':
    main()