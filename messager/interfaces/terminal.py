from blessed import Terminal as BlessedTerminal
from datetime import datetime
from typing import (
    NoReturn,
    Optional,
    Self
)
from messager.interfaces import Interface


class Terminal(Interface):
    terminal = BlessedTerminal()

    def write(
        self: Self,
        message: str,
        weight: int
    ) -> NoReturn:
        if weight >= self.min or weight <= self.max:
            color = {
                0: self.terminal.bold_italic_bright_black,
                1: self.terminal.bold_italic,
                2: self.terminal.bold_white_on_yellow,
                3: self.terminal.bold_italic_white_on_red,
                4: self.terminal.bold_italic_yellow_on_red_blink
            }
            formated_message = ' ' +\
                self.app + ' - ' +\
                self.module + ' - ' +\
                datetime.now().strftime(self.mask) + ' - ' +\
                message + ' '
            print(
                color[weight](formated_message)
            )
