from __future__ import annotations
from typing import Iterable
import numpy as np


def mean(values: Iterable[float]) -> float:
    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        raise ValueError("不能对空序列计算平均值")
    return float(arr.mean())


def variance(values: Iterable[float], ddof: int = 0) -> float:
    arr = np.asarray(list(values), dtype=float)
    if arr.size == 0:
        raise ValueError("不能对空序列计算方差")
    return float(arr.var(ddof=ddof))


def stddev(values: Iterable[float], ddof: int = 0) -> float:
    return float(np.sqrt(variance(values, ddof=ddof)))
