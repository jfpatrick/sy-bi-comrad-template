
# Activate Acc-Py
deactivate
source /acc/local/share/python/acc-py-pyqt/setup.sh

# Create local virtualenv
acc-py venv venv
source venv/bin/activate

# Checkout template code and run wizard
git clone https://gitlab.cern.ch/szanzott/be-bi-pyqt-template.git wizard
cd wizard
python wizard.py