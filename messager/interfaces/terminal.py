from datetime import datetime
from typing import (
    Any,
    NoReturn,
    Optional,
    Self,
    Union
)
from zoneinfo import ZoneInfo
from messager.interfaces import Interface


class Terminal(Interface):
    app: str = 'undefined'
    module: str = 'undefined'

    def __init__(
        self: Self,
        *args: Union[dict, None],
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        super().__init__(*args, **kwargs)

    def write(
        self: Self,
        message: Union[Any],
        level: int,
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        self.message = message
        self.level = level
        self._set_attributes(kwargs)
        if self.level >= self.min or self.level <= self.max:
            color = {
                0: '\033[1;97m ',
                1: '\033[1;92m ',
                2: '\033[1;96m ',
                3: '\033[1;93m ',
                4: '\033[1;91m ',
                5: '\033[1;101;97m '
            }
            formated_message = color[self.level] +\
                datetime.now(ZoneInfo(self.timezone)).strftime(self.mask) + ' - ' +\
                self.app + ' - ' +\
                self.module + ' - ' +\
                str(self.message) + ' \033[0m'
            print(
                formated_message
            )
