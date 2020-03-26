import PyQt5
from PyQt5.QtWidgets import QTabWidget


def test_can_open_main_window(monkeypatch, main_window, mock_pyjapc):
    # Should be no error message, so if one is created, raise exception
    def raise_exception():
        raise RuntimeError("A QMessageBox opened!")
    monkeypatch.setattr(PyQt5.QtWidgets.QMessageBox, "exec", raise_exception)
    assert main_window is not None
