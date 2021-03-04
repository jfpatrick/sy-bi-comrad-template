# !/usr/bin/bash

# Activate the virtual environments
source /acc/local/share/python/acc-py/base/pro/setup.sh
source venv/bin/activate

# Alias the shared Acc-Py PyCharm instance. 
# NOTE: This PyCharm distro is kind of unofficial and might change!
alias pycharm="/acc/local/share/python/pycharm/pycharm-community-2019.2.3/bin/pycharm.sh"
# See https://wikis.cern.ch/display/ACCPY/PyCharm#PyCharm-Performanceissues
#   if you encounter performance issues with PyCharm
