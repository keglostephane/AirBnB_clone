# Welcome to AirBnB clone project

This project is a series of mini projets as an attempt to recreate a clone of
AirBnB platform.
It does not aim to reproduce a fully functional AirBnB platform but serves
only as education purpose. **Use at your own RISK!**

AirBnB project is an important part of [ALX](https://www.alxafrica.com/)
Software Engineering Program as it help to evaluate and demonstrate effective
skills in Python language.

## AirBnB clone - The console

It's the first in the series of mini project to create a AirBnB platform.

In this project, we will create:

- A model (class) to define each entity (object) and its associated data.
- A modular storage engine to store and retrieve our entities at each program
execution.
- A command line interface (the console) to ease the management of our entities.

### Important concepts covered in this project

- Object Oriented Programming (classes, methods, inheritance , ...)
- Positional and Keyword arguments
- Code organization (package, module, class, function)
- Code Testing: unittest
- Code Documentation: Docstring
- Code Formatting: Pycodestyle
- Serialization / Deserialization with JSON
- Command Line Interface
- Modules: **json**, **datime**, **cmd**

### Requirements:

- *Python3.8* or above
- Command line interpreter : *Bash* or others

### Instrunctions

1. Clone the repository

  ```bash
  git clone https://github.com/keglostephane/AirBnB_clone.git
  ```

2. Launch the console

  ```bash
  cd ./AirBnB_clone
  ```

  ```bash
  ./console.py
  ```

  The console is ready to accept commands:

  ```
  (hbnb)
  ```


### Documentation

List of console commands:

| Command | Description |
| --- | --- |
| `help` | list available commands |
| `quit` | exit the console |
| `EOF` or `Ctrl^D` | exit the console |
| `create` | create a new instance, print the `id` and save it |
| `show` | print the string represensation of an instance |
| `update` | update an instance |
| `destroy` | delete an instance |

List of Classes:

`BaseModel`: Base Class

- Attributes :

  - `id` (uuid.uuid4)

  - `created_at` (datetime.datetime)

  - `updated_at` (datetime.dateime)


`User`: Define a user

- Attributes:

  - `last_name` (str)

  - `first_name` (str)

  - `email` (str)

  - `password` (str)


`State`: Define a state

- Attributes:

  - `name` (str)

`City` : Define a city

- Attributes:

  - `state_id` (str)

  - `name` (str)


`Amenity`: Define an amenity

- Attributes:

  - `name` (str)

`Place` : Define a place

- Attributes:

  - `city_id` (str)

  - `user_id` (str)

  - `name` (str)

  - `description` (str)

  - `number_rooms` (int)

  - `number_bathrooms` (int)

  - `max_guest` (int)

  - `price_by_night` (int)

  - `latitude` (float)

  - `longitude` (float)

  - `amenity_ids` (list)


`Review` : Define a review

- Attributes

  - `place_id` (str)

  - `user_id` (str)

  - `text` (str)


### Usage

```bash
(hbnb)help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

```

```bash
(hbnb)help create
Create command to create a new instance, save it and print the id
```

```bash
(hbnb)create BaseModel
f0d6c5ee-0ff3-4298-a585-80c8db620478
```

```bash
(hbnb)show BaseModel f0d6c5ee-0ff3-4298-a585-80c8db620478
[BaseModel] (f0d6c5ee-0ff3-4298-a585-80c8db620478) {'id': 'f0d6c5ee-0ff3-4298-a585-80c8db620478', 'created_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556178), 'updated_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556183)}
```

```bash
(hbnb)create User
0aef86f5-0ac4-486c-8fdb-57db61b197c6
```

```bash
(hbnb)create State
4530ac8f-f8a2-4bf7-ae83-a2ab013bd403
```

```bash
(hbnb)all
["[BaseModel] (f0d6c5ee-0ff3-4298-a585-80c8db620478) {'id': 'f0d6c5ee-0ff3-4298-a585-80c8db620478', 'created_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556178), 'updated_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556183)}", "[User] (0aef86f5-0ac4-486c-8fdb-57db61b197c6) {'id': '0aef86f5-0ac4-486c-8fdb-57db61b197c6', 'created_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641645), 'updated_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641657)}", "[State] (4530ac8f-f8a2-4bf7-ae83-a2ab013bd403) {'id': '4530ac8f-f8a2-4bf7-ae83-a2ab013bd403', 'created_at': datetime.datetime(2023, 12, 11, 17, 39, 52, 969584), 'updated_at': datetime.datetime(2023, 12, 11, 17, 39, 52, 969597)}"]
```

```bash
(hbnb)all BaseModel
["[BaseModel] (f0d6c5ee-0ff3-4298-a585-80c8db620478) {'id': 'f0d6c5ee-0ff3-4298-a585-80c8db620478', 'created_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556178), 'updated_at': datetime.datetime(2023, 12, 11, 17, 35, 16, 556183)}"]
```

```bash
(hbnb)all User
["[User] (0aef86f5-0ac4-486c-8fdb-57db61b197c6) {'id': '0aef86f5-0ac4-486c-8fdb-57db61b197c6', 'created_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641645), 'updated_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641657)}"]
```

```bash
(hbnb)update User 0aef86f5-0ac4-486c-8fdb-57db61b197c6 last_name Doe
```

```bash
update User 0aef86f5-0ac4-486c-8fdb-57db61b197c6 first_name John
```

```bash
(hbnb)show User 0aef86f5-0ac4-486c-8fdb-57db61b197c6
[User] (0aef86f5-0ac4-486c-8fdb-57db61b197c6) {'id': '0aef86f5-0ac4-486c-8fdb-57db61b197c6', 'created_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641645), 'updated_at': datetime.datetime(2023, 12, 11, 17, 37, 59, 641657), 'last_name': 'Doe', 'first_name': 'John'}
```

```bash
(hbnb)destroy User 0aef86f5-0ac4-486c-8fdb-57db61b197c6
```

```bash
(hbnb)show User 0aef86f5-0ac4-486c-8fdb-57db61b197c6
** no instance found **
```

### Contributors

[keglostephane](https://github.com/keglostephane)

[Chesterkxng](https://github.com/Chesterkxng)
