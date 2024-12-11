from datetime import datetime
from pathlib import Path
from typing import (
    Any,
    LiteralString,
    NoReturn,
    Optional,
    Self,
    Union
)
from zoneinfo import ZoneInfo
from messager.utils import levels
from messager.interfaces import Interface


class File(Interface):
    app: str = 'undefined'
    module: str = 'undefined'


    def __init__(
        self: Self,
        path: Path,
        *args: Union[dict, None],
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.path = Path(path).absolute()
        self.path.mkdir(
            parents=True,
            exist_ok=True
        )

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
            path = Path(self.path / levels[self.level])
            try:
                content = path.read_text()
            except FileNotFoundError:
                content = ''
            finally:
                date = datetime.now(
                    ZoneInfo(self.timezone)
                )
                content += f'{ date } | { self.app } | { self.module } | { self.message }\n'
                path.write_text(content)
