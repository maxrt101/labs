# IoT python labs

## Lab 6
### Task:
 - Implement REST service (GET/POST/PUT/DELETE requests) for one of the classes from 3rd lab.
 - Implement saving of the object of the chosen class in the database.
 - Use Flask, Python 3.x, SQLAlchemy and MySQL-8.0.

### Usage
```
 main.py [-h] [-c CONFIGFILE] [--host HOST] [--port PORT] [--debug]
```
 - `-h`, `--help` - Show help message and exit
 - `-c CONFIGFILE`, `--config CONFIGFILE` - Config file path, default `server.cfg`
 - `--host HOST` - Server host address
 - `--port PORT` - Server port
 - `--debug` - Flask debug mode

### Config file
Configuration info is stored in config file. Default config file is `server.cfg`.  
The syntax for property is `KEY=VALUE`. The line is considered a comment, if it starts with `#`.   
You can override the config file with `-c` flag.  
`--host` and `--port` flags override `HOST` and `PORT` config props.  
Important notice: config parser DOESN'T ignore spaces. Every space will be considered as a part of key or value.  
Config should contain such properties:  
 - `USER` - MySQL user name
 - `PASS` - MySQL user password
 - `DB_SERVER` - MySQL server name
 - `DB_NAME` - Database name
 - `HOST` - Flask server hostname
 - `PORT` - Flask server port

### To run:
  - Clone/Download lab6 branch
  - Go into repo folder
  - Create virtual env using `python3 -m venv .venv` command
  - Activate venv using `source .venv/bin/activate` on \*nix systems and `.venv\Scripts\activate.bat` on Windows cmd.
  - Install dependencies using `pip3 install -r requirements.txt`
  - Run the app using `./main.py` or `python3 main.py`

