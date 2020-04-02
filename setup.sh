
# Activate Acc-Py
deactivate
source /acc/local/share/python/acc-py-pyqt/setup.sh

# Create local virtualenv
acc-py venv venv
source venv/bin/activate

# Install template code and run wizard
pip install "git+https://:@gitlab.cern.ch:8443/szanzott/be-bi-pyqt-template.git"  # Replace with package name once released!
setup-pyqt5-project