from typing import (
    NoReturn,
    Optional,
    Self,
    Union
)
from messager.interfaces import Interface


class Message:
    module = 'undefined'
    def __init__(
        self: Self,
        app: str,
        interfaces: Optional[list[Interface | None]] = [],
        mask: Optional[str] = '%d/%m/%Y %H:%M',
        min: Optional[int] = 0,
        max: Optional[int] = 4
    ) -> NoReturn:
        self.app = app
        self.interfaces = interfaces
        self.mask = mask
        self.min = min
        self.max = max

    def __call__(
        self: Self,
        module: Optional[str] = 'undefined'
    ) -> NoReturn:
        self.module = module

    def __send(
        self: Self,
        message: str,
        weight: int
    ) -> NoReturn:
        for interface in self.interfaces:

            interface(
                app=self.app,
                module=self.module,
                mask=self.mask
            )
            interface.write(
                message=message,
                weight=weight
            )

    def debug(
        self: Self,
        message: str
    ) -> NoReturn:
        self.__send(
            message=message,
            weight=0
        )

    def info(
        self: Self,
        message: str
    ) -> NoReturn:
        self.__send(
            message=message,
            weight=1
        )

    def warning(
        self: Self,
        message: str
    ) -> NoReturn:
        self.__send(
            message=message,
            weight=2
        )

    def error(
        self: Self,
        message: str
    ) -> NoReturn:
        self.__send(
            message=message,
            weight=3
        )

    def critical(
        self: Self,
        message: str
    ) -> NoReturn:
        self.__send(
            message=message,
            weight=4
        )
