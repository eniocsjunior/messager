# Messager
Package to create log messages.

## How to use
Initially, we must configure the messaging server with the interfaces we want to use:
```python

>>> from messager import Message, File, SQL
>>> file = File()
>>> message = Message(app='my_app', interfaces=[file])
```
You can also add interfaces after instantiating the Message class:
```python
>>> message.interfaces
[<messager.interfaces.files.File object at 0xffffba9d1fd0>]
>>> postgres = SQL(uri='postgres://user:password@localhost:5432/database')
>>> sqlite = SQL(uri='sqlite:///mylogfile.db')
>>> message.add_interface(postgres)
>>> message.add_interface(sqlite)
>>> message.interfaces
[<messager.interfaces.files.File object at 0xffffba9d1fd0>, <messager.interfaces.sql.SQL object at 0xffffbad7a7d0>, <messager.interfaces.sql.SQL object at 0xffffbad78ac9>]
```
After instantiating the Message class, you can call the instance again in another part of the code:
```python
>>> message(module='my_module')
```
Now just create your messages:
```python
>>> message.debug('A debug message')
>>> message.success('A success message')
>>> message.info('A info message')
>>> message.warning('A warning message')
>>> message.error('A error message')
>>> message.critical('A critical message')
```
