import time
import datetime
from threading import Event, Thread

from papc.device import Device


class IntervalUpdateDevice(Device):

    def __init__(self, field_to_update, selector_to_update, frequency=30, *args, **kwargs):
        # Take out the `frequency` argument from the kwargs, or default to 30Hz
        self.field_to_update = field_to_update
        self.selector_to_update = selector_to_update
        super().__init__(*args, **kwargs)
        # Start the internal timer (RepeatedTimer is defined below)
        self.timer = RepeatedTimer(1 / frequency, self.time_tick)

    def time_tick(self):
        now = datetime.datetime.now()
        t = time.mktime(now.timetuple()) + now.microsecond
        self.set_state({self.field_to_update: t}, self.selector_to_update)


class RepeatedTimer:

    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = self._orig_function = function
        self.args = args
        self.kwargs = kwargs
        self.start = time.time()
        self.event = Event()
        self.thread = Thread(target=self._target)
        self.thread.daemon = True
        self.thread.start()

    def _target(self):
        while not self.event.wait(self._time):
            self.function(*self.args, **self.kwargs)

    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def pause(self):
        self.function = lambda *args, **kwargs: None

    def resume(self):
        self.function = self._orig_function

    def stop(self):
        self.event.set()
        self.thread.join()
