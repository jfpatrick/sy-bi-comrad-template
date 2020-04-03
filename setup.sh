
echo "_________________________________________________________________________"
echo "       ___       __   __         ___    ___  __     ___       ___        "
echo " |  | |__  |    /  ` /  \  |\/| |__      |  /  \     |  |__| |__         "
echo " |/\| |___ |___ \__, \__/  |  | |___     |  \__/     |  |  | |___        "
echo "     ____        ____  __     _       ___                      __        "
echo "    / __ \__  __/ __ \/ /_   | |     / (_)___  ____ __________/ /        "
echo "   / /_/ / / / / / / / __/   | | /| / / /_  / / __ `/ ___/ __  /         "
echo "  / ____/ /_/ / /_/ / /_     | |/ |/ / / / /_/ /_/ / /  / /_/ /          "
echo " /_/    \__, /\___\_\__/     |__/|__/_/ /___/\__,_/_/   \__,_/           "
echo "       /____/                                                            "
echo "_________________________________________________________________________"

# Activate Acc-Py
echo "=> Setting up temporary virtualenv"
deactivate
source /acc/local/share/python/acc-py-pyqt/setup.sh

# Create local virtualenv
acc-py venv .temp-venv
source .temp-venv/bin/activate

# Checkout template code and run wizard
# git clone https://gitlab.cern.ch/szanzott/be-bi-pyqt-template.git wizard
# Temporary debugging replacement
mkdir wizard
cp -r ../be-bi-pyqt-template/!(venv) wizard

cp wizard/wizard.py .
python wizard.py

# Remove temporary venv and wizard.py
echo "=> Removing temporary virtualenv"
deactivate
rm -rf .temp-venv
rm wizard.py

# Move into the only available folder, setup venv and install
cd */
acc-py venv venv
source venv/bin/activate
pip install -e .

# remove yourself
rm setup.sh