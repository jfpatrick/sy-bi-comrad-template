import pytest
import pyjapc

from be_bi_pyqt_template.widgets.example_widget import ExampleWidget
from be_bi_pyqt_template.models.papc_setup.papc_devices import setup_papc_devices


@pytest.fixture()
def my_gui(qtbot):
    my_gui = ExampleWidget()
    my_gui.show()
    qtbot.addWidget(my_gui)
    yield my_gui


@pytest.fixture(autouse=True)
def mock_pyjapc(monkeypatch):
    # Monkey-patch PyJapc
    pyjapc.PyJapc = setup_papc_devices()
    japc = pyjapc.PyJapc()
    japc.setSelector("LHC.USER.ALL")
    # Run test
    yield japc
    # Clean up
    pyjapc.PyJapc = None

