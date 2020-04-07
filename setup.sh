
deactivate
clear
echo "_________________________________________________________________________"
echo "       ___       __   __         ___    ___  __     ___       ___        "
echo " |  | |__  |    /    /  \  |\/| |__      |  /  \     |  |__| |__         "
echo " |/\| |___ |___ \__  \__/  |  | |___     |  \__/     |  |  | |___        "
echo "     ____        ____  __     _       ___                      __        "
echo "    / __ \__  __/ __ \/ /_   | |     / (_)___  ____ __________/ /        "
echo "   / /_/ / / / / / / / __/   | | /| / / /_  / / __ '/ ___/ __  /         "
echo "  / ____/ /_/ / /_/ / /_     | |/ |/ / / / /_/ /_/ / /  / /_/ /          "
echo " /_/    \__, /\___\_\__/     |__/|__/_/ /___/\__,_/_/   \__,_/           "
echo "       /____/                                                            "
echo "_________________________________________________________________________"

# Checkout template code and run wizard
# git clone https://gitlab.cern.ch/szanzott/be-bi-pyqt-template.git wizard
# Temporary debugging replacement
mkdir wizard
cp -r ../be-bi-pyqt-template/!(venv) wizard
rm -rf wizard/*.egg-info

echo "Welcome to BI's PyQt5 Project Setup Wizard!"

while true
do
  read -p "Please enter your project's name:  " project_name
  if [[ $project_name =~ ^[a-z0-9\-]+$ ]]; then
    echo "=> A folder called '"$project_name"' will be created as your project's root directory."
    break
  else
    echo "=> Error! The project name can contain only letters, numbers and dashes"
  fi
done

while true
do
  read -p "Please enter a one-line description of your project:  " project_desc
  if [[ $project_desc != "" ]]; then
    break
  fi
done

while true
do
  read -p "Please enter the project's author name:  " project_author
  if [[ $project_author != "" ]]; then
    break
  fi
done

while true
do
  read -p "And his/her CERN email address:  " project_email
  if [[ "${project_email}" =~ ^.*@.*$ ]]; then
    break
  else
    echo "=> Error! Invalid email, try again"
  fi
done

echo "_________________________________________________________________________"
echo "=> Your project is being generated..."

# Copy tree from the cloned repo
mv wizard/be_bi_pyqt_template wizard/$project_name
# Rename tree root
mv wizard $project_name

# Make replacements
project_name_underscores="${project_name/-/_}"
grep -rl "be-bi-pyqt-template" . | xargs sed -i "s/be-bi-pyqt-template/${project_name}/g"
grep -rl "be_bi_pyqt_template" . | xargs sed -i "s/be_bi_pyqt_template/${project_name_underscores}/g"
cd $project_name
sed -i "s/BE BI PyQt Template/${project_desc}/g" setup.py
sed -i "s/Sara Zanzottera/${project_author}/g" setup.py
sed -i "s/sara.zanzottera@cern.ch/${project_email}/g" setup.py

# Setup venvs
source /acc/local/share/python/acc-py-pyqt/setup.sh
acc-py venv venv
source venv/bin/activate

# Install with pip
echo "=> The project is being installed..."
if pip install -e . -q; then

  # Success!
  echo "_________________________________________________________________________"
  echo "=> New project installed successfully"
  echo "=> Please run 'source activate.sh' and then 'charm $project_name' to open the project in the IDE."
  # remove yourself
  rm setup.sh

else

  # Failure
  echo "_________________________________________________________________________"
  echo "=> New project failed to install! "
  echo "Please check the logs of 'pip install -e .' and report to the maintainers."
fi