# !/usr/bin/bash

# Activate the virtual environments
source venv/bin/activate

# Hook the accwidgets plugin for Qt Designer
#export PYQTDESIGNERPATH=$PWD/venv/lib/python3.7/site-packages/accwidgets/graph/designer
#export PYQTDESIGNERPATH=$PYQTDESIGNERPATH:$PWD/venv/lib/python3.7/site-packages/accwidgets/app_frame/designer
#export PYQTDESIGNERPATH=$PYQTDESIGNERPATH:$PWD/venv/lib/python3.7/site-packages/accwidgets/timing_bar/designer
#export PYQTDESIGNERPATH=$PYQTDESIGNERPATH:$PWD/venv/lib/python3.7/site-packages/accwidgets/led/designer
#export PYQTDESIGNERPATH=$PYQTDESIGNERPATH:$PWD/venv/lib/python3.7/site-packages/accwidgets/log_console/designer
#export PYQTDESIGNERPATH=$PYQTDESIGNERPATH:$PWD/venv/lib/python3.7/site-packages/accwidgets/property_edit/designer
export PYQTDESIGNERPATH=$PWD/venv/lib/python3.7/site-packages/accwidgets/app_frame/designer

# Put CO's PyCharm on the PATH
#alias pycharm=/acc/local/share/python/pycharm/pycharm-community-2019.2.3/bin/pycharm.sh

# Make sure all templates are installed
#accwidgets-cli install-templates
