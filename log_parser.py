"""
Libary for parsing NCSA Common access log format

The format is as follows:
  IP/URI CLIENT_IDENTITY USERID [DATETIME] REQUEST_HEADER STATUS_CODE PAYLOAD_SIZE

Regex pattern used to parse the entries:
  (.+) (.+) (.+) \[([^\]]+)\] "(.+)" (\d{3}) (.+)

Classes:
  RequestHeader
  LogEntry
  LogParser

Functions:
  error

"""

import re
import calendar
from datetime import datetime
from typing import List, Dict, Tuple, Generator, Final


GREEN: Final[str] = '\x1b[32m'
BLUE:  Final[str] = '\x1b[34m'
BBLUE: Final[str] = '\x1b[94m'
RED:   Final[str] = '\x1b[31m'
RESET: Final[str] = '\x1b[0m'


def error(*args):
    print(f'{RED}ERROR{RESET}:', *args)


class RequestHeader:
    def __init__(self, request_header: str):
        request_header = request_header.split(' ')
        self.method = request_header[0] if len(request_header) > 0 else ''
        self.url = request_header[1] if len(request_header) > 1 else ''
        self.protocol = request_header[2] if len(request_header) > 2 else ''

    def __str__(self) -> str:
        return '{} {} {}'.format(self.method, self.url, self.protocol)


class Timestamp:
    regex = r'(\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2})' # (-\d{4}) # utc offset
    pattern = re.compile(regex)

    mon_names = {month: index for index, month in enumerate(calendar.month_abbr) if month}

    def __init__(self, string: str):
        self.valid = False
        if string:
            match = Timestamp.pattern.search(string)
            if match:
                self.day = int(match.group(1))
                self.mon = match.group(2)
                self.yr  = int(match.group(3))
                self.hr  = int(match.group(4))
                self.min = int(match.group(5))
                self.sec = int(match.group(6))
                self.valid = True

    def __str__(self) -> str:
        return f'{self.day}/{self.mon}/{self.yr}:{self.hr}:{self.min}:{self.sec}' if self.valid else ''

    def __bool__(self) -> bool:
        return self.valid

    def __gt__(self, rhs) -> bool:
        return datetime(self.yr, Timestamp.mon_names[self.mon], self.day, self.hr, self.min, self.sec) > \
               datetime(rhs.yr, Timestamp.mon_names[rhs.mon], rhs.day, rhs.hr, rhs.min, rhs.sec)

    def __lt__(self, rhs) -> bool:
        return datetime(self.yr, Timestamp.mon_names[self.mon], self.day, self.hr, self.min, self.sec) < \
               datetime(rhs.yr, Timestamp.mon_names[rhs.mon], rhs.day, rhs.hr, rhs.min, rhs.sec)


class LogEntry:
    regex =  r'(.+?) (.+?) (.+?) \[([^\]]+)\] "(.+?)" (\d{3}) (.+)'

    def __init__(self, client_addr: str, client_identity: str,  userid: str, timestamp: str,
                 request_header: str, response_code: str, payload_size: str):
        self.client_addr = client_addr
        self.client_identity = client_identity
        self.userid = userid
        self.timestamp = timestamp
        self.request = RequestHeader(request_header)
        self.response_code = int(response_code)
        self.payload_size = int(payload_size) if payload_size != '-' else 0

    def __str__(self) -> str:
        return '{} {} {} [{}] "{}" {} {}'.format(
            self.client_addr, self.client_identity, self.userid, self.timestamp,
            self.request, self.response_code, self.payload_size)


class LogParser:
    def __init__(self):
        self.pattern = re.compile(LogEntry.regex)

    def find(self, filename: str, method: str, status: str, begin_time: str = None, end_time: str = None) -> \
            Generator[Tuple[int, LogEntry], None, None]:
        ''' Yields line number and parsed log entry for that line '''

        method_pattern = re.compile(f'"{method} ')
        status_pattern = re.compile(f' {status} ')
        date_pattern   = re.compile(r' \[([^\]]+)\] ')

        begin_ts = Timestamp(begin_time)
        end_ts   = Timestamp(end_time)

        with open(filename, 'r', errors='ignore') as f: # File can contain non-ascii characters
            lineno = 0
            for line in f:
                lineno += 1
                if begin_ts or end_ts:
                    date = date_pattern.search(line)
                    if not date: continue
                    ts = Timestamp(date.group(1))
                    if begin_ts and ts < begin_ts: continue
                    if end_ts   and ts > end_ts: print('end ts')
                    if end_ts   and ts > end_ts: return
                status_match = status_pattern.search(line)
                if not status_match: continue
                method_match = method_pattern.search(line)
                if not method_match: continue
                result = self.pattern.search(line)
                if result:
                    yield lineno, LogEntry(result.group(1), result.group(2), result.group(3),
                                           Timestamp(result.group(4)),
                                           result.group(5), result.group(6), result.group(7))
                else:
                    error(f'Matching line {lineno}: "{line}"')
