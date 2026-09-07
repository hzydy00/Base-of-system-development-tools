import pytest
from my_pkg import mean, stddev, variance


def test_mean():
    assert mean([1, 2, 3, 4, 5]) == pytest.approx(3.0)


def test_variance_population():
    assert variance([1, 2, 3, 4, 5], ddof=0) == pytest.approx(2.0)


def test_variance_sample():
    assert variance([1, 2, 3, 4, 5], ddof=1) == pytest.approx(2.5)


def test_stddev():
    assert stddev([1, 2, 3, 4, 5]) == pytest.approx(2.0**0.5)


def test_empty_raises():
    with pytest.raises(ValueError):
        mean([])
