from abc import ABC, abstractmethod
from typing import (
    Any,
    LiteralString,
    NoReturn,
    Optional,
    Self,
    Union
)


class Interface(ABC):

    def _set_attributes(
        self: Self,
        kwargs: Union[dict, None]
    ) -> NoReturn:
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __init__(
        self: Self,
        min: Optional[int] = 0,
        max: Optional[int] = 5,
        timezone: Optional[LiteralString] = 'UTC',
        mask: Optional[str] = '%d/%m/%Y %H:%M:%S',
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        self.min = min
        self.max = max
        self.mask = mask,
        self.timezone = timezone
        self._set_attributes(kwargs)

    def __call__(
        self: Self,
        **kwargs: Union[dict]
    ) -> NoReturn:
        self._set_attributes(kwargs)

    @abstractmethod
    def write(
        self: Self,
        message: Union[Any],
        level: int,
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        ...
