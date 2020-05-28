deactivate >/dev/null 2>&1
source /acc/local/share/python/acc-py-pyqt/setup.sh
source venv/bin/activate

# Hook the accwidgets plugin for Qt Designer
export PYQTDESIGNERPATH=$PWD/venv/lib/python3.6/site-packages/accwidgets/graph/designer

# Put CO's PyCharm on the PATH
export PATH=$PATH:/acc/local/share/python/pycharm/pycharm-community-2019.2.3/bin