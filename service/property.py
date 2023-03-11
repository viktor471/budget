from typing import Union, Any, Callable
import typing
import inspect
from enum import Enum

def get_enum_value(value: Union[Enum, str], type_of_enum) -> str:
    if isinstance(value, type_of_enum):
        return value.value
    elif isinstance(value, str):
        return value
    else:
        raise RuntimeWarning(f"unknown type of {type_of_enum.__name__}. Type of {type_of_enum.__name__}: {type(value)}")

def check_type(value, types: Union[list, Any], name: str = None):
    assert isinstance(name, str) or name is None

    if name is None:
        name = "variable"

    print(f"{types = } {type(types) = }")

    print(f"{value = }")

    assert value is not None
    if value is not None:
        if isinstance(types, typing.UnionType):
            types = tuple(types.__args__)
            print("!!!!")
            assert isinstance(value, types), f"{name} must be one of {types} or None"
        else:
            print("$$$")
            assert isinstance(value, types)

    return True

def get_function_arguments(func: Callable) -> tuple:
    assert isinstance(func, Callable)

    return tuple(inspect.getfullargspec(func).args)


def get_protected_attr(obj, name) -> Any:
    return getattr(obj, f"_{name}", None)

def set_protected_attr(obj, name, value) -> Any:
    return setattr(obj, f"_{name}", value)

class Field:

    def __init__(self,
                 get_item_function: Callable = get_protected_attr,
                 set_item_function: Callable = set_protected_attr):

        self._get_item_function = get_item_function
        self._set_item_function = set_item_function

    @property
    def get_item_function(self):
        return self._get_item_function

    @get_item_function.setter
    def get_item_function(self, func: Callable):
        assert isinstance(func, Callable)
        assert all(arg in ["obj", "name"] for arg in get_function_arguments(func))

        self._get_item_function = func

        return func

    @property
    def set_item_function(self):
        return self._set_item_function

    @set_item_function.setter
    def set_item_function(self, func):
        assert isinstance(func, Callable)
        assert all(arg in ["obj", "name", "value"] for arg in get_function_arguments(func))

        self._set_item_function = func

        return func

    @property
    def field_getter(self):

        get_item_function = self.get_item_function

        def _field_getter(obj, name: str) -> Any:

            assert isinstance(name, str), f"field must be str type"

            value = get_item_function(obj, name)

            # assert value is not None, f"{name} is not already set in {type(obj).__name__} object"

            return value

        return _field_getter

    @property
    def field_setter(self) -> Callable:
        # if isinstance(types, UnionType):
        #     types = list(types.__args__)

        def _field_setter(obj, name: str, value: Any, types: Union["Union", Any]) -> Any:

            check_type(value, types, name)

            if isinstance(value, Enum):
                value = value.value

            setattr(obj, f"_{name}", value)

            self.set_item_function(obj, name, value)

            return value

        return _field_setter


class Property:
    def __init__(self,
                 get_method = Field().field_getter,
                 set_method = Field().field_setter,
                 property_set: set = None):

        self._get_method    = get_method
        self._set_method    = set_method
        self._property_set = property_set

    @property
    def property_set(self) -> set:
        return self._property_set

    @property_set.setter
    def property_set(self, new_set: set) -> set:
        assert isinstance(new_set, set)

        self._property_set = new_set

        return new_set

    @property
    def get_method(self) -> Callable:
        return self._get_method

    @get_method.setter
    def get_method(self, new_get_method: Callable) -> Callable:
        assert isinstance(new_get_method, Callable)

        self._get_method = new_get_method

        return new_get_method

    @property
    def set_method(self) -> Callable:
        return self._set_method

    @set_method.setter
    def set_method(self, new_set_method: Callable) -> Callable:
        assert isinstance(new_set_method, Callable)

        self._set_method = new_set_method

        return new_set_method

    def create_property_with_name(self, name: str, types: type):
        if self._property_set is not None:
            self._property_set.add(name)

        def getter(obj) -> types:
            f"""позволяет установить / прочитать параметр {name}"""
            return self.get_method(obj, name)

        def setter(obj, value) -> types:
            f"""позволяет установить / прочитать параметр {name}"""

            signature = get_function_arguments(self.set_method)

            args = {"value": value}

            if "name" in signature:
                args["name"] = name

            if "types" in signature:
                args["types"] = types

            set_method = self.set_method
            return set_method(obj, **args)

        def deleter(obj):
            delattr(obj, f"_{name}")

        return property(getter, setter, deleter)

    def __call__(self, name: str, types: type) -> property:
        return self.create_property_with_name(name, types)

