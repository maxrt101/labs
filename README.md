# IoT python labs

## Lab 5
Count and print top-5 successful POST requests in span from 02:35 to 03:18 01/Jul/1995  
[Log file archive](https://drive.google.com/open?id=0B1k21nkk13PYZ0l5eUdkOUtOa2M)  

### Usage
```
main.py [-h] [-c] [-m METHOD] [-s START_TIME] [-e END_TIME] [-d] [--by-resource]
        [--by-domain] [--first FIRST] [--status STATUS] [--sort-reverse] FILE
```
 - `FILE` - File to parse (required)
 - `-h`, `--help` - Print help message
 - `-c`, `--count` - Start in count mode, by default the script will just parse the file and print summary
 - `-m METHOD`, `--method METHOD` - HTTP request method
 - `-s STATUS`, `--status STATUS` - Filter by HTTP response status code
 - `-b START_TIME`, `--begin START_TIME` - Specify begin time for log entries, entries before that time, will not be counted
 - `-e END_TIME`, `--end END_TIME` - Similar as above, but sets the upper bound
 - `-d`, `--display` - Flag to print all parsed lines in parse mode
 - `--first FIRST` - Print only first FIRST number of lines in output
 - `--by-resource` - Count using web page address, exluding domain (default is full url)
 - `--by-domain` - Count using only domain, excluding resource (default is full url)
 - `--sort-reverse` - Reverse count table

### To run:
  - Clone/Download lab5 branch
  - Go into repo folder
  - Type `./main.py LOGFILE` or `python3 main.py LOGFILE` (replace LOGFILE with actual file name)
  - To run as specified in task, type `./main.py LOGFILE -c -m POST -b "01/Jul/1995:02:35:00" -e "01/Jul/1995:03:18:00"`

