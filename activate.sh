deactivate >/dev/null 2>&1
source /acc/local/share/python/acc-py-pyqt/setup.sh
source venv/bin/activate

# Hook the accwidgets plugin for QtDesigner
export PYQTDESIGNERPATH=$PWD/venv/lib/python3.6/site-packages/accwidgets/graph/designer