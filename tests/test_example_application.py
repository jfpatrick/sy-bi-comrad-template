import PyQt5
from PyQt5.QtWidgets import QPushButton, QSpinBox
from accwidgets.graph import ScrollingPlotWidget, CyclicPlotWidget
from be_bi_pyqt_template.widgets.example_widget import ExampleWidget


def test_can_open_main_window(monkeypatch):
    """
    This test showcases how to check whether specific Qt operations are performed during
    your test (in this case, opening a dialog).
    The ideas is to monkey-patch the interesting operation with a lambda that throws a
    recognizable exception, and then monitor the code for such exception.
    """
    # Define what to do if a QMessageBox tries to open
    def raise_exception_if_qmessagebox_opens():
        raise RuntimeError("A QMessageBox opened!")

    # Replace the 'exec' function of the QMessageBox with the custom function above
    monkeypatch.setattr(PyQt5.QtWidgets.QMessageBox, "exec", raise_exception_if_qmessagebox_opens)

    # No QMessageBox should open, so no RuntimeError should be thrown
    # If you expect a QMessageBox, then use 'with pytest.raises(RuntimeException):' to catch the exception
    my_gui = ExampleWidget()
    my_gui.show()
    assert my_gui is not None


def test_main_window_has_all_tabs(my_gui):
    """ Make sure the example application has all the expected tabs in the right order. """
    assert my_gui.count() == 3
    assert my_gui.tabText(0) == "First Tab"
    assert my_gui.tabText(1) == "Second Tab"
    assert my_gui.tabText(2) == "Image"


def test_first_tab(my_gui, mock_pyjapc, qtbot):
    """ Test the first tab looks right and does what it's expected to do. """

    # Does it contain a ScrollingPlotWidget?
    assert my_gui.first_tab.findChild(ScrollingPlotWidget) is not None

    # Does it contain a QSpinBox called 'amplitude_sin'?
    amplitude_spinbox = my_gui.first_tab.findChild(QSpinBox, "amplitude_sin")
    assert amplitude_spinbox is not None
    # Does it set the right value on the right device?
    amplitude_spinbox.clear()
    qtbot.keyClicks(amplitude_spinbox, "50")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#amplitude_sin") == 50

    # Does it contain a QSpinBox called 'period_sin'?
    period_spinbox = my_gui.first_tab.findChild(QSpinBox, "period_sin")
    assert period_spinbox is not None
    # Does it set the right value on the right device?
    period_spinbox.clear()
    qtbot.keyClicks(period_spinbox, "20")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#period_sin") == 20


def test_second_tab(my_gui, mock_pyjapc, qtbot):
    """ Test the second tab looks right and does what it's expected to do. """

    # Does it contain a CyclicPlotWidget?
    assert my_gui.second_tab.findChild(CyclicPlotWidget) is not None

    # Does it contain a QSpinBox called 'amplitude_cos'?
    amplitude_spinbox = my_gui.second_tab.findChild(QSpinBox, "amplitude_cos")
    assert amplitude_spinbox is not None
    # Does it set the right value on the right device?
    amplitude_spinbox.clear()
    qtbot.keyClicks(amplitude_spinbox, "30")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#amplitude_cos") == 30

    # Does it contain a QSpinBox called 'period_cos'?
    period_spinbox = my_gui.second_tab.findChild(QSpinBox, "period_cos")
    assert period_spinbox is not None
    # Does it set the right value on the right device?
    period_spinbox.clear()
    qtbot.keyClicks(period_spinbox, "40")
    assert mock_pyjapc.getParam("TEST_DEVICE/Settings#period_cos") == 40
