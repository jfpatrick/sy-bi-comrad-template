import os
import shutil
from time import sleep

def main():
    os.system('clear')
    print("""
================================================================================================
  ___   ___     ___           ___    _     ___    __      __  _                        _ 
 | _ ) |_ _|   | _ \  _  _   / _ \  | |_  | __|   \ \    / / (_)  ___  __ _   _ _   __| |
 | _ \  | |    |  _/ | || | | (_) | |  _| |__ \    \ \/\/ /  | | |_ / / _` | | '_| / _` |
 |___/ |___|   |_|    \_, |  \__\_\  \__| |___/     \_/\_/   |_| /__| \__,_| |_|   \__,_|
                     |__/                                                               

================================================================================================
""")
    print("Welcome to the PyQt5 Project Setup Wizard!")
    project_name = input("Please enter your projects' name:  ")
    # Validate
    print("A folder called '{} will be created as your project's root directory".format(project_name))
    short_description = input("Please enter a short description of your project (~100 characters max):  ")
    author_name = input("Please enter the project's author name:  ")
    author_email = input("And his/her CERN email address:  ")
    print("Thank you! Your project is being generated...")

    # Generate project root
    os.mkdir(project_name)

    # Copy files from the template app
    shutil.copytree("be_bi_pyqt_template", project_name)

    # Change the root name in all files
    for dname, dirs, files in os.walk(project_name):
        for fname in files:
            fpath = os.path.join(dname, fname)
            with open(fpath) as f:
                s = f.read()
            s = s.replace("be_bi_pyqt_template", project_name)
            with open(fpath, "w") as f:
                f.write(s)

    print("The project is read and it will now be pip installed in the local virtual environment."
          "Please run 'source activate.sh' and then 'charm {}' to open the project in the IDE".format(project_name))



if __name__ == '__main__':
    main()