from datetime import datetime
from typing import (
    NoReturn,
    Optional,
    Self
)
from messager.interfaces import Interface


class Terminal(Interface):

    def write(
        self: Self,
        message: str,
        weight: int
    ) -> NoReturn:
        if weight >= self.min or weight <= self.max:
            color = {
                0: '\033[1;96m ',
                1: '\033[1;92m ',
                2: '\033[1;93m ',
                3: '\033[1;91m ',
                4: '\033[1;101;97m '
            }
            formated_message = color[weight] +\
                self.app + ' - ' +\
                self.module + ' - ' +\
                datetime.now().strftime(self.mask) + ' - ' +\
                message + ' \033[0m'
            print(
                formated_message
            )
