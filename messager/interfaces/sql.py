from datetime import datetime
from peewee import CharField, DateTimeField, Model
from playhouse.db_url import connect
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


class SQL(Interface):
    app: str = 'undefined'
    module: str = 'undefined'

    class Log(Model):
        app = CharField(max_length=16)
        module = CharField(max_length=16)
        message = CharField()
        level = CharField(max_length=8)
        date = DateTimeField()

        class Meta:
            table_name = 'logs'
            dbatabase = None

    def __init__(
        self: Self,
        uri: LiteralString,
        *args: Union[dict, None],
        **kwargs: Union[dict, None]
    ) -> NoReturn:
        super().__init__(*args, **kwargs)
        self.db = connect(uri)
        self.__set_database(self.db)

        self.db.create_tables([self.Log])

    @classmethod
    def __set_database(
        cls: Self,
        database: LiteralString
    ) -> NoReturn:
        cls.Log._meta.database = database

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
            self.Log(
                app=self.app,
                module=self.module,
                message=self.message,
                level=levels[self.level],
                date=datetime.now(
                    ZoneInfo(self.timezone)
                )
            ).save()
