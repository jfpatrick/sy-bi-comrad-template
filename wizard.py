import os
import shutil
from pathlib import Path

def main():
    try:
        os.system('clear')
        print("""
_________________________________________________________________________
       ___       __   __         ___    ___  __     ___       ___    
 |  | |__  |    /  ` /  \  |\/| |__      |  /  \     |  |__| |__     
 |/\| |___ |___ \__, \__/  |  | |___     |  \__/     |  |  | |___                                                                       
     ____        ____  __     _       ___                      __
    / __ \__  __/ __ \/ /_   | |     / (_)___  ____ __________/ /
   / /_/ / / / / / / / __/   | | /| / / /_  / / __ `/ ___/ __  / 
  / ____/ /_/ / /_/ / /_     | |/ |/ / / / /_/ /_/ / /  / /_/ /  
 /_/    \__, /\___\_\__/     |__/|__/_/ /___/\__,_/_/   \__,_/   
       /____/                                                    
_________________________________________________________________________
    """)
        print("Welcome to BI's PyQt5 Project Setup Wizard!")
        project_name = input("Please enter your projects' name:  ")
        # Validate
        print("A folder called '{}' will be created as your project's root directory".format(project_name))
        short_description = input("Please enter a short description of your project (~100 characters max):  ")
        author_name = input("Please enter the project's author name:  ")
        author_email = input("And his/her CERN email address:  ")
        print("_________________________________________________________________________")
        print("Your project is being generated...")

        # Generate project root
        # os.mkdir(project_name)

        # Copy files from the template app
        parent_path = Path(__file__)
        project_path = parent_path.parent / project_name
        print(" - Setting up folder structure under {}".format(project_path.absolute()))
        os.rename("wizard", project_name)
        # shutil.copytree(parent_path, project_path)

        # Change the root name in all files
        for dname, dirs, files in os.walk(project_path):
            for dirname in dirs:
                if "be_bi_pyqt_template" in dirname:
                    dpath = os.path.join(dname, dirname)
                    os.rename(dpath, dpath.replace("be_bi_pyqt_template", project_name))
            for fname in files:
                # Temporary check, remove later
                fpath = os.path.join(dname, fname)
                if fname.split(".")[-1] in ["py", "ui", "qrc", "md", "gitignore", "yml", "sh"]:
                    print(" - Processing {}".format(fpath))
                    with open(fpath, "r") as f:
                        s = f.read()
                    s = s.replace("be_bi_pyqt_template", project_name)
                    with open(fpath, "w") as f:
                        f.write(s)
                else:
                    os.remove(fpath)

        print("The project is ready and it will now be pip installed in the local virtual environment.\n"
              "Please run 'source activate.sh' and then 'charm {}' to open the project in the IDE.".format(project_name))

    except KeyboardInterrupt:
        print("\nStopping here. Bye!")


if __name__ == '__main__':
    main()