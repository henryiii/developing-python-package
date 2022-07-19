import example_package

import platform
import pytest


def test_mag():
    vec = example_package.Vector(3, 4)
    assert abs(vec) == 5
    assert vec.mag() == 5
