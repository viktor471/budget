from typing import Union
from enum import Enum
from service.property import Property, check_type

# TODO not used
class Colors:
    green = "\033[1;32;48m"
    white = "\033[1;37;48m"
    yellow = "\033[1;33;48m"
    base = "\033[0m"

# TODO not used
class ProgressBar:

    class IncrementType(Enum):
        INTERNAL_VALUE = "internal_value"
        DO_NOT_INCREMENT = "do_not_increment"

    class _Progress:

        increment_step = Property().create_property_with_name("increment_step", Union[float, int])
        value          = Property().create_property_with_name("value",          Union[float, int])

        def __init__(self, value: float = 0.0, increment_step: float = 1.0):
            check_type(value, Union[float, int])
            check_type(increment_step, Union[float, int])

            self.value = value
            self.increment_step = increment_step

        def increment(self, increment_step: Union[float, int] = None):
            check_type(increment_step, Union[float, int])

            if increment_step is not None:
                self.value += increment_step
            else:
                self.value += self.increment_step

    @property
    def progress(self) -> _Progress:
        return self._progress

    hide_bar = Property().create_property_with_name("hide_bar", bool)

    def __init__(self, total: Union[float, int], increment_step: Union[float, int] = 1.0, hide_bar = False):
        self._total = float(total)
        self.progress_symbol = '\u258b'
        self.left_progress_symbol = '-'
        self._progress = self._Progress(0.0, increment_step)
        self._first_call = True
        self.hide_bar = hide_bar

    @property
    def progress_symbol(self) -> str:
        return self._progress_symbol

    @progress_symbol.setter
    def progress_symbol(self, new_symbol) -> str:
        assert isinstance(new_symbol, str)
        assert len(new_symbol) == 1

        self._progress_symbol = new_symbol

        return new_symbol

    @property
    def left_progress_symbol(self) -> str:
        return self._left_progress_symbol

    @left_progress_symbol.setter
    def left_progress_symbol(self, new_symbol) -> str:
        assert isinstance(new_symbol, str)
        assert len(new_symbol) == 1

        self._left_progress_symbol = new_symbol

        return new_symbol

    @property
    def percent(self):
        return 100 * (self.progress.value / self._total)

    @property
    def left_percent(self):
        return 100 - self.percent

    @property
    def _bar(self):
        percent = int(self.percent)
        left_percent = int(self.left_percent)

        return f"{self.progress_symbol * percent}{self.left_progress_symbol * left_percent}"

    def change_progress(self,
                        progress:       Union[int, float] = None,
                        increment_step: Union[int, float, IncrementType] = IncrementType.INTERNAL_VALUE):

        if progress is not None:
            self.progress.value = progress

        elif isinstance(increment_step, int) or isinstance(increment_step, float):
            self.progress.increment(increment_step)

        elif increment_step is ProgressBar.IncrementType.INTERNAL_VALUE:
            self.progress.increment()

        elif increment_step is ProgressBar.IncrementType.DO_NOT_INCREMENT:
            pass  # do nothing

    def print_progress(self,
                       progress:       Union[int, float] = None,
                       increment_step: Union[int, float] = IncrementType.INTERNAL_VALUE):

        self.change_progress(progress, increment_step)

        if self._first_call:
            self.print("\n")
            self._first_call = False

        print(f"\r", end = "\r")
        colored_percent = f"{Colors.green}{self.percent:>6.2f}%{Colors.base}"
        print(f"\r|{self._bar}| {colored_percent} ", end = "\r")

        if self.percent == 100:
            self.print("\n")
