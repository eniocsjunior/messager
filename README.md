# Messager
Package to create log messages.

## How to use
Initially we must instantiate the interfaces we want to use:
```python
from messager import Terminal
terminal = Terminal()
```
The interfaces have 2 optional parameters:
* min: Minimum level to run the interface.
* max: Maximum level to run the interface.

The levels are:
* 0: Debug
* 1: Info
* 2: Warning
* 3: Error
* 4: Critical

After configuring the interfaces, it is necessary to add the interfaces to a Messages instance:
```python
from messager import Message
message = Message(
    app='Test',
    interfaces=[terminal]
)
```

It is recommended but not mandatory to call the Message class in each module of your code:
```python
message(module='my_module')
```

Then, just call the appropriate method for your message:
```python
message.debug('My debug message')
message.info('My info message')
message.warning('My warning message')
message.error('My error message')
message.critical('My critical message')
```
