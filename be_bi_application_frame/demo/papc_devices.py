from papc.interfaces.pyjapc import SimulatedPyJapc
from papc.system import System
from papc.fieldtype import FieldType, EquationFieldType
from papc.deviceproperty import Acquisition, Setting, Command
from papc.timingselector import TimingSelector

from be_bi_application_frame.demo.papc_utils import IntervalUpdateDevice


def setup_papc_devices():
    # Create the System and the simulated PyJapc
    list_of_devices = create_my_devices()
    my_system = System(devices=list_of_devices)
    return SimulatedPyJapc.from_simulation_factory(lambda: my_system, strict=False)


def create_my_devices():
    device_properties = (
        Setting('Settings', (
            FieldType("status", "int", initial_value=1),
            FieldType("name", "str", initial_value="My System"),
            FieldType("amplitude", "float", initial_value=1),
            FieldType("theta", "float", initial_value=0)
        )),
        Acquisition('Acquisition', (
            EquationFieldType('sin', 'float', 'sin({Settings#theta})'),
        )),
        # Command('systemOn', (), start_the_device),
        # Command('systemOff', (), stop_the_device),
    )
    device = IntervalUpdateDevice(
                        name="TEST_DEVICE",
                        device_properties=device_properties,
                        field_to_update="Settings#theta",
                        selector_to_update=TimingSelector("LHC.USER.ALL"),
                        timing_selectors=(TimingSelector(""), TimingSelector("LHC.USER.ALL")),
                        frequency=30
                    )
    return [device]


def start_the_device(device, param, value, selector):
    device.set_state({"SystemStatus#status": 1}, selector)
    device.timer.resume()


def stop_the_device(device, param, value, selector):
    device.set_state({"SystemStatus#status": 0}, selector)
    device.timer.pause()
