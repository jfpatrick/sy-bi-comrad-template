from be_bi_pyqt_template.widgets.main_widget import MainWidget
from be_bi_pyqt_template.models.papc_setup.papc_devices import setup_papc_devices

import pytest
import pyjapc


@pytest.fixture()
def my_gui(qtbot):
    """
    This fixture returns a properly setup instance of your GUI,
    ready to be manipulated with qtbot.
    It will be available in your tests as 'my_gui'
    (change the function name to change this)
    """
    my_gui = MainWidget()
    my_gui.show()
    qtbot.addWidget(my_gui)
    yield my_gui


@pytest.fixture(autouse=True)
def mock_pyjapc(monkeypatch):
    """
    This fixture intercepts PyJapc calls and redirects them to a papc instance.
    Make sure you setup papc to simulate the same devices your GUI usually
    connects to.
    This fixture will make an object called 'mock_pyjapc' available in your tests
    without the need to instantiate it.
    """
    # Monkey-patch PyJapc
    pyjapc.PyJapc = setup_papc_devices()
    japc = pyjapc.PyJapc()
    japc.setSelector("")
    # Run test
    yield japc
    # Clean up
    pyjapc.PyJapc = None

