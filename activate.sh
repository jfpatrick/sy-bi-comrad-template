
# For reference, see
# https://acc-py.web.cern.ch/gitlab/bisw-python/pyqt-tutorial/docs/stable/2-project-structure.html#activate-sh

# Activate the virtual environments
source venv/bin/activate

# Hook the accwidgets plugin for Qt Designer
export PYQTDESIGNERPATH=$PWD/venv/lib/python3.7/site-packages/accwidgets/graph/designer

# Put CO's PyCharm on the PATH
alias pycharm=/acc/local/share/python/pycharm/pycharm-community-2019.2.3/bin/pycharm.sh