# Documentation MazgaDB

Library made for testing.
All code is taken from file example.py (Весь код взят из файла example.py)
The library folder itself ```MazgaDB/__init__.py``` (Исходник библиотеки ```MazgaDB/__init__.py```)
## Import

You can use 2 types of imports: ```from MazgaDB import MazgaDB``` or ```import MazgaDB.MazgaDB```

## Class
| Field | Type     | Description |
|-------|----------|---------|
| db    | ```str```     | database name     |
| data_classes  | ```dict```      | data_class (not required to use) |

#### Description
Class creation

db - write with extension
data_classes - takes the form ```{'users': People..}```
#### Example: 
```
from MazgaDB import MazgaDB
db = MazgaDB('users.db', {'users': People})
```

## Methods
### create_table
| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| param  | ```dict```      |     table options |

#### Description

Adds a table to the database

Param only takes this form ```{'column_name1': 'data_type1', 'column_name2': 'data_type2'...}```<br>
Accepts data type only from ```sqlite3```

#### Example: 
```
from MazgaDB import MazgaDB
db = MazgaDB('users.db')
db.create_table('users',{'id':'INT', 'fname':'TEXT'})
```

| id | fname    | 
|-------|----------|
|      | |


### append_line
| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| values  | ```list```      |string values  |

#### Description
Adds a line to the table
#### Example:
```
db = MazgaDB('users.db')
db.append_line('users', [1,'Mazga'])
```

| id | fname    | 
|-------|----------|
|   1   | Mazga|

### update_line
| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| key1 | ```str```      |key (column)  |
|value1 | ```str``` | key1 value|
| key2 | ```str```      |key (column)  |
|value2| ```str``` | key2 value|

#### Description

Updates objects by criteria for certain data

#### Example:
```
db = MazgaDB('users.db')
db.update_line('users', key1 = 'id', value1 = '1', key2 = 'fname', value2 = 'Mazga2')
```

| id | fname    | 
|-------|----------|
|   1   | Mazga2|

We had a line with id 1 and a fname Mazga his fname changed to Mazga2

### delete_line
| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| key | ```str```      |key(column)  |
|value| ```str``` | key value|

#### Description

Removes a line from the table

#### Example:
```
db = MazgaDB('users.db')
db.delete_line('users', key = 'id', value = 1)
```


| id | fname    | 
|-------|----------|
|    |  |

### append_column

| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| name_column | ```str```      | column name  |
|type_column| ```str``` | column type|

#### Description

Adds a column to the table

```type_column``` - accepts only types from ```sqlite3```

#### Example:
```
db = MazgaDB('users.db')
db.append_column('users', 'lname', 'TEXT')
```

| id | fname    | lname |
|-------|----------|--------|
|   1   | Mazga| None|


### delete_column

| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| column | ```str```      | column name |

#### Description

Deletes a column in the table

```type_column``` - accepts only types from ```sqlite3```

#### Example:
```
db = MazgaDB('users.db')
db.delete_column('users', 'lname')
```

| id | fname    | 
|-------|----------|
|   1   | Mazga|

### select

| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| key | ```str```      |key(column)  |
|value| ```str``` | key value|


#### Description
Regular SELECT from ```sqlite3```

#### Example:
```
db = MazgaDB('users.db')
db.select('users', key = 'id', value = '1')
```
#### Output:
```
[(1, 'Mazga')]
```

### select_class

| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| key | ```str```      |key(column)  |
|value| ```str``` | key value|
|class_data| ```None``` | class to return|

#### Description
Returns values as a class

#### Example1:
```
db = MazgaDB('users.db')
db.select_class('users', key = 'id', value = '1', class_data = People)
```
#### Output1:
```
People(id = 1, fname = 'Mazga')
```


#### Example2:
```
db = MazgaDB('users.db', {'users': People})
db.select_class('users', key = 'id', value = '1')
```
#### Output2:
```
People(id = 1, fname = 'Mazga')
```

### read_table


| Field | Type     | Description |
|-------|----------|---------|
| name_table     | ```str```     | table name     |
| param | ```list```      | column name |

#### Description 
Returns a table of characters

#### Example1:
```
db = MazgaDB('users.db')
db.read_table('users')
```
#### Output1:

| id    | fname     |
|-------|----------|
| 1     | Mazga   |

#### Example2:
```
db = MazgaDB('users.db')
db.read_table('users', ['id'])
```
#### Output2:

| id    |
|-------|
| 1     |

### saw_tables

#### Description 
Accepts nothing

#### Example:
```
db = MazgaDB('users.db')
db.saw_tables()
```
#### Output:

```
[('users')]
```

### execute

| Field | Type     | Description |
|-------|----------|---------|
| sql_request     | ```str```     | sql request  |
| param | ```list```      | column name |

#### Description 
Normal ```execute``` from ```sqlite3``` (no need to write ```db.conn.commit()```, it's already built into the functions)
#### Example:
```
db = MazgaDB('users.db')
db.execute('SELECT * FROM users')
```

#### Output:
```
[(1, 'Mazga')]
```
