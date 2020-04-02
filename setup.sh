
# Activate Acc-Py
deactivate
source /acc/local/share/python/acc-py-pyqt/setup.sh

# Create local virtualenv
acc-py venv venv
source venv/bin/activate

# Install template code and run wizard
git clone --depth 1 --no-checkout https://gitlab.cern.ch/szanzott/be-bi-pyqt-template.git wizard
cd wizard
git checkout master -- wizard.py

python wizard.py