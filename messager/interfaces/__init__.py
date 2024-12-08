from abc import ABC
from typing import (
    NoReturn,
    Optional,
    Self
)


class Interface(ABC):

    def __init__(
        self: Self,
        min: Optional[int] = 0,
        max: Optional[int] = 4
    ) -> NoReturn:
        self.min = min
        self.max = max

    def __call__(
        self: Self,
        app: str,
        module: str,
        mask: str
    ) -> NoReturn:
        self.app = app
        self.module = module
        self.mask = mask

    def write(
        self: Self,
        weight: int
    ) -> Exception:
        raise NotImplementedError
