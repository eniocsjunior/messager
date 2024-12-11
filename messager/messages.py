from typing import (
    LiteralString,
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
        timezone: Optional[LiteralString] = 'UTC',
        mask: Optional[str] = '%d/%m/%Y %H:%M:%S',
        min: Optional[int] = 0,
        max: Optional[int] = 5
    ) -> NoReturn:
        self.app = app
        self.interfaces = interfaces
        self.timezone = timezone
        self.mask = mask
        self.min = min
        self.max = max

    def __call__(
        self: Self,
        module: Optional[str] = 'undefined'
    ) -> NoReturn:
        self.module = module

    @property
    def __send(
        self: Self
    ) -> NoReturn:
        if self.level >= self.min and self.level <= self.max:
            for interface in self.interfaces:
                interface(
                    app=self.app,
                    module=self.module,
                    timezone=self.timezone,
                    mask=self.mask
                )
                interface.write(
                    message=self.message,
                    level=self.level
                )

    def add_interface(
        self: Self,
        interface: Interface
    ) -> NoReturn:
        self.interfaces.append(interface)

    def debug(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 0
        self.message = message
        self.__send

    def success(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 1
        self.message = message
        self.__send

    def info(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 2
        self.message = message
        self.__send

    def warning(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 3
        self.message = message
        self.__send

    def error(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 4
        self.message = message
        self.__send

    def critical(
        self: Self,
        message: str
    ) -> NoReturn:
        self.level = 5
        self.message = message
        self.__send
