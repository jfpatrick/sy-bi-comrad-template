# Color Escapes
NC='\033[0;m'
BOLD='\033[1;m'
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'

# Actual script
deactivate
clear
echo -e ${YELLOW}
echo -e "_________________________________________________________________________"
echo -e "       ___       __   __         ___    ___  __     ___       ___        "
echo -e " |  | |__  |    /    /  \  |\/| |__      |  /  \     |  |__| |__         "
echo -e " |/\| |___ |___ \__  \__/  |  | |___     |  \__/     |  |  | |___        "
echo -e "     ____        ____  __     _       ___                      __        "
echo -e "    / __ \__  __/ __ \/ /_   | |     / (_)___  ____ __________/ /        "
echo -e "   / /_/ / / / / / / / __/   | | /| / / /_  / / __ '/ ___/ __  /         "
echo -e "  / ____/ /_/ / /_/ / /_     | |/ |/ / / / /_/ /_/ / /  / /_/ /          "
echo -e " /_/    \__, /\___\_\__/     |__/|__/_/ /___/\__,_/_/   \__,_/           "
echo -e "       /____/                                                            "
echo -e "_________________________________________________________________________"
echo -e ""
echo -e "Welcome to BI's PyQt5 Project Setup Wizard!"
echo -e "_________________________________________________________________________"
echo -e ${NC}

while true
do
  echo -ne "${YELLOW}=>${NC} Please enter your ${GREEN}project's name${NC}:  "
  read project_name
  if [[ $project_name =~ ^[a-z0-9\-]+$ ]]; then
    echo -e "${GREEN}=>${NC} A folder called ${BLUE}"$project_name"${NC} will be created as your project's root directory."
    break
  else
    echo -e "${RED}=> Error!${YELLOW} The project name can contain only letters, numbers and dashes${NC}"
  fi
done

while true
do
  echo -ne "${YELLOW}=>${NC} Please enter a ${GREEN}one-line description${NC} of your project:  "
  read project_desc
  if [[ $project_desc =~ ^.*[\"].*$ ]]; then
    echo -e "${RED}=> Error!${YELLOW} The project description cannot contain the character \" ${NC}"
  else
    break
  fi
done

while true
do
  echo -ne "${YELLOW}=>${NC} Please enter the project's ${GREEN}author name${NC}:  "
  read project_author
  if [[ $project_author =~ ^.*[\"].*$ ]]; then
    echo -e "${RED}=> Error!${YELLOW} The name cannot contain the character \" ${NC}"
  else
    break
  fi
done

while true
do
  echo -ne "${YELLOW}=>${NC} And the author's ${GREEN}CERN email address${NC}:  "
  read project_email
  if [[ "${project_email}" =~ ^.*[\"].*[@cern\.ch]$ ]]; then
    echo -e "${RED}=> Error! ${YELLOW}Invalid CERN email, try again${NC}"
  else
    break
  fi
done

echo -e "${YELLOW}_________________________________________________________________________${NC}"
echo -e ""
echo -e "${GREEN}=>${NC} Starting project generation"

echo -ne "${GREEN}=>${NC} Downloading template from GitLab...  "

# Checkout template code
while ! git clone https://gitlab.cern.ch/szanzott/be-bi-pyqt-template.git template >/dev/null 2>&1
do
  echo -ne "${RED}=>${YELLOW} Failed to clone the template! Do you want to retry? (yes/no)${NC}  "
  read answer
  if [[ $answer == "no" ]]; then
    exit 1
  fi
  echo -e "${GREEN}=>${NC} Downloading template from GitLab...  "
done

# Temporary debugging replacement
#mkdir wizard
#cp -r ../be-bi-pyqt-template/!(venv) wizard
#rm -rf wizard/*.egg-info
echo -e "   ${GREEN}Done${NC}"

echo -ne "${GREEN}=>${NC} Applying customizations...  "

# Replace eventual dashes with underscores
project_name_underscores="${project_name/-/_}"

# Rename tree root
mv template/be_bi_pyqt_template template/$project_name_underscores
mv template $project_name

# Replace strings into files
grep -rl "be-bi-pyqt-template" . | xargs sed -i "s/be-bi-pyqt-template/${project_name}/g"
grep -rl "be_bi_pyqt_template" . | xargs sed -i "s/be_bi_pyqt_template/${project_name_underscores}/g"
cd $project_name
sed -i "s/BE BI PyQt Template/${project_desc}/g" setup.py
sed -i "s/Sara Zanzottera/${project_author}/g" setup.py
sed -i "s/sara.zanzottera@cern.ch/${project_email}/g" setup.py
echo -e "   ${GREEN}Done${NC}"


echo -ne "${GREEN}=>${NC} Activating virtualenvs... "
# Setup venvs
source /acc/local/share/python/acc-py-pyqt/setup.sh  >/dev/null 2>&1
acc-py venv venv  >/dev/null 2>&1
source venv/bin/activate
echo -e "   ${GREEN}Done${NC}"

# Install with pip
echo -ne "${GREEN}=>${NC} Installing the project...  "
if pip install -e . -qqqq; then

  # Success!
  echo -e "   ${GREEN}Done${NC}"
  echo -e "_________________________________________________________________________"
  echo -e "${GREEN}=>${NC} New project installed successfully!"
  echo -e "${GREEN}=>${NC} Please make sure all went well by typing 'example-app' in the console"
  # remove yourself
  rm setup.sh

else

  # Failure
  echo -e "   ${RED}Fail!${NC}"
  echo -e "_________________________________________________________________________"
  echo -e "${RED}=> Error!${YELLOW} New project failed to install ${NC}"
  echo -e "Please execute ${YELLOW}pip install -e $project_name${NC} and, if it fails, send the log to the maintainers."
fi

# Go back to the dir we started from
cd ../