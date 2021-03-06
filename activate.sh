# !/usr/bin/bash

# Activate the virtual environments
source /acc/local/share/python/acc-py/base/pro/setup.sh
source venv/bin/activate

# Alias the BI Python GUI Manager (https://gitlab.cern.ch/bisw-python/bipy-gui-manager)
alias bipy-gui-manager="/user/bdisoft/operational/python/gui/bipy-gui-manager"

# Alias the shared Acc-Py PyCharm instance. 
alias pycharm="/acc/local/share/python/pycharm/pycharm-community-2019.2.3/bin/pycharm.sh"
# NOTE: This PyCharm distro is kind of unofficial and might change!
# See https://wikis.cern.ch/display/ACCPY/PyCharm#PyCharm-Performanceissues
# if you encounter performance issues with PyCharm
