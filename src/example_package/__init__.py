from __future__ import annotations

import dataclasses
import platform
import numpy as np
from pathlib import Path

from typing import TypeVar  # Could use Self eventually

__version__ = "0.0.1"

__all__ = ["platform_system", "write_a_file", "Vector"]


Self = TypeVar("Self")


def platform_system() -> str:
    return platform.system()


def write_a_file(filename: Path) -> None:
    with filename.open("x") as f:
        f.write("Hello from write_a_file")


@dataclasses.dataclass
class Vector:
    x: float
    y: float

    def mag(self) -> float:
        return (self.x**2 + self.y**2) ** (0.5)

    __abs__ = mag

    def __add__(self: Self, other: Self) -> Self:
        return self.__class__(self.x + other.x, self.y + other.y)
