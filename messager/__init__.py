from pathlib import Path
from tomllib import loads
from messager.interfaces import Interface
from messager.interfaces.terminal import Terminal
from messager.messages import Message


__all__ = [
    'Interface',
    'Message',
    "Terminal"
]
__data = loads(
    Path('pyproject.toml').read_text()
)['tool']['poetry']
__version__ = __data['version']
__description__ = __data['description']
__author__ = __data['authors']
