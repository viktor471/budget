import pandas as pd
from records.record import Record
from typing import Mapping, Callable
from service.algorithms import OnlyOneIsTrue
from dataclasses import dataclass

# r = Record({"date": 33, "price": "a"})
# df = pd.DataFrame(columns=["date", "price"])
# print(r)
# df = pd.concat([df, pd.DataFrame({"date": ["some_date"], "price": [33]})], ignore_index=True)

# print(r.dataframe)
# print(df)
# print(isinstance({}, Mapping))


# def func(a = None, b = None, c = None, d = None):
#     OnlyOneIsTrue(all(arg is not None for arg in [a, b, c]),
#                   d is not None)
#
# @dataclass
# class bestParams:
#     distance_func: Callable
#     kernel_func: Callable
#     window_width: float = None
#     neighbourhood_count: int = None
#
#
# params = bestParams(func, func, window_width=3.0)

# print(params)

my_typle = (3)

print(my_typle)

my_typle = (3,)

print(my_typle)
