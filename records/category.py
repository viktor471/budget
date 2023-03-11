from enum import Enum

class Category(Enum):
    entertainment = "entertainment"
    hygiene       = "hygiene"
    health        = "health"
    food          = "food"
    clothes       = "clothes"
    household     = "household"
    longevous     = "longevous"

    def __init__(self, value, parent = None):
        # print(f"{args = } {kwargs = }")
        # self.value = value
        super().__init__()
        self._parent = parent

