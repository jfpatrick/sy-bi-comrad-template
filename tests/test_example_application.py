import PyQt5
from PyQt5.QtWidgets import QPushButton, QSpinBox
from accwidgets.graph import ScrollingPlotWidget, CyclicPlotWidget


def test_can_open_main_window(monkeypatch, my_gui):
    # Should be no error message, so if one is created, raise exception
    def raise_exception():
        raise RuntimeError("A QMessageBox opened!")
    monkeypatch.setattr(PyQt5.QtWidgets.QMessageBox, "exec", raise_exception)
    assert my_gui is not None


def test_main_window_has_all_tabs(my_gui):
    assert my_gui.count() == 3
    assert my_gui.tabText(0) == "First Tab"
    assert my_gui.tabText(1) == "Second Tab"
    assert my_gui.tabText(2) == "Image"


def test_first_tab(my_gui, mock_pyjapc, qtbot):
    assert my_gui.first_tab.findChild(ScrollingPlotWidget) is not None

    amplitude_spinbox = my_gui.first_tab.findChild(QSpinBox, "amplitude_sin")
    assert amplitude_spinbox is not None
    amplitude_spinbox.clear()
    qtbot.keyClicks(amplitude_spinbox, "50")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#amplitude_sin") == 50

    period_spinbox = my_gui.first_tab.findChild(QSpinBox, "period_sin")
    assert period_spinbox is not None
    period_spinbox.clear()
    qtbot.keyClicks(period_spinbox, "20")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#period_sin") == 20


def test_second_tab(my_gui, mock_pyjapc, qtbot):
    assert my_gui.second_tab.findChild(CyclicPlotWidget) is not None

    amplitude_spinbox = my_gui.second_tab.findChild(QSpinBox, "amplitude_cos")
    assert amplitude_spinbox is not None
    amplitude_spinbox.clear()
    qtbot.keyClicks(amplitude_spinbox, "30")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#amplitude_cos") == 30

    period_spinbox = my_gui.second_tab.findChild(QSpinBox, "period_cos")
    assert period_spinbox is not None
    period_spinbox.clear()
    qtbot.keyClicks(period_spinbox, "40")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#period_cos") == 40
