# Messager
Package to create log messages.

![Terminal](terminal.png)

## How to use
Initially, we must configure the messaging server with the interfaces we want to use:
```python
>>> from messager import Message, File, SQL
>>> file = File()
>>> message = Message(app='my_app', interfaces=[file])
```
You can also add interfaces after instantiating the Message class:
```python
>>> len(message.interfaces)
1
>>> postgres = SQL(uri='postgres://user:password@localhost:5432/database')
>>> sqlite = SQL(uri='sqlite:///mylogfile.db')
>>> mariadb = SQL(uri='mysql://user:password@localhost:3306/database')
>>> mysql = SQL(uri='mysql://user:password@localhost:3306/database')
>>> message.add_interface(postgres)
>>> message.add_interface(sqlite)
>>> message.add_interface(mariadb)
>>> message.add_interface(mysql)
>>> len(message.interfaces)
5
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

## Default interfaces

### Interface
Main interface. The arguments passed in this class are common to all interfaces.
#### Arguments
* min - Minimum level to send the message effectively. Default: 0
* min - Maximum level to send the message effectively. Default: 5
* timezone - Your preferred timezone. Default: UTC
* mask - Mask used in date formatting. Default: '%d/%m/%Y %H:%M:%S'

### Terminal
Show message on console.

### File
Uses a folder to store log files.
#### Argument
* path - Folder where the log files will be created. REQUIRED!

### SQL
Store logs in a SQL database.
SQL databases officially supported by the [Peewee](https://docs.peewee-orm.com/en/latest/index.html) library are:
* SQLite3
* PostgreSQL
* MariaDB
* MySQL
#### Argument
* uri - Uniform Resource Identifier. REQUIRED!
