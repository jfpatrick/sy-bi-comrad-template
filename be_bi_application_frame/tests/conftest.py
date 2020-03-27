import pytest
import pyjapc

from be_bi_application_frame.widgets.application_frame import ApplicationFrame
from be_bi_application_frame.models.papc_setup.papc_devices import setup_papc_devices


@pytest.fixture()
def main_window(qtbot):
    main_window = ApplicationFrame()
    main_window.show()
    qtbot.addWidget(main_window)
    yield main_window


@pytest.fixture(autouse=True)
def mock_pyjapc(monkeypatch):
    # Monkey-patch PyJapc
    pyjapc.PyJapc = setup_papc_devices()
    # Run test
    yield
    # Clean up
    pyjapc.PyJapc = None

