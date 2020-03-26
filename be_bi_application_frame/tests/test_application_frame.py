import pytest
import PyQt5
from PyQt5.QtWidgets import QPushButton, QLabel


def test_can_open_main_window(monkeypatch, main_window, mock_pyjapc):
    # Should be no error message, so if one is created, raise exception
    def raise_exception():
        raise RuntimeError("A QMessageBox opened!")
    monkeypatch.setattr(PyQt5.QtWidgets.QMessageBox, "exec", raise_exception)
    assert main_window is not None


def test_main_window_has_all_elements(monkeypatch, main_window, mock_pyjapc):
    top_toolbar = main_window.top_toolbar
    assert top_toolbar is not None
    assert top_toolbar.findChild(QLabel, "future_timing_display") is not None
    assert top_toolbar.findChild(QPushButton, "future_rbac_button") is not None

    assert main_window.central_widget.count() == 2
    assert main_window.central_widget.tabText(0) == "First Tab"
    assert main_window.central_widget.tabText(1) == "Second Tab"

    assert main_window.bottom_logbox is not None


@pytest.mark.skip("Implement when the timing widget will be here")
def test_timing_widget_runs():
    pass


@pytest.mark.skip("Implement when the rbac button will be here")
def test_rbac_button_works():
    pass