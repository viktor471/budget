from records.category import Category
import pandas as pd
from service.property import check_type
from typing import Any, Mapping, Iterable


class Record(dict):
    _property_dict = {"date":     str,
                      "name":     str,
                      "time":     str,
                      "category": str | list | Category,
                      "price":    float | int}

    def __init__(self, seq=None, **kwargs):
        def check_mapping(mapping: Mapping):
            for key, value in mapping.items():
                self.check_arg(key, value)

        if kwargs:
            check_mapping(kwargs)

        if isinstance(seq, Mapping):
            check_mapping(seq)

        if isinstance(seq, Iterable):
            for key, value in seq:
                self.check_arg(key, value)

        super().__init__(seq, **kwargs)


    def check_arg(self, key, value=None):
        assert key in self._property_dict, f"field {key} is not part of Record"
        assert check_type(value, self._property_dict[key], key), (f"field {key} with value {value} "
                                                                  f"must be {self._property_dict[key]}")

    def __setitem__(self, key, value):
        self.check_arg(key, value)
        print("setitem")
        super(Record, self).__setitem__(key, value)


    def __getitem__(self, key):
        self.check_arg(key)

        return super(Record, self).__getitem__(key)


    def __setattr__(self, key: str, value: Any) -> Any:
        self.__setitem__(key, value)

        return value


    def __getattr__(self, key):
        return self.__getitem__(key)


    @property
    def dataframe(self) -> pd.DataFrame:
        return pd.DataFrame({key: [self.__getitem__(key)] for key in self})


    def __str__(self):
        return f"Record: {super().__str__()}"
