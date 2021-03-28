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
from typing import List, Dict, Tuple, Generator, Final

GREEN: Final[str] = '\u001b[32m'
BLUE:  Final[str] = '\u001b[34m'
RED:   Final[str] = '\u001b[31m'
RESET: Final[str] = '\u001b[0m'


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
    regex = r'(\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2})' # (-\d{4})' # utc offset
    pattern = re.compile(regex)

    def __init__(self, string: str):
        self.valid = False
        if string:
            match = Timestamp.pattern.search(string)
            if match:
                self.day = match.group(1)
                self.mon = match.group(2)
                self.yr  = match.group(3)
                self.hr  = match.group(4)
                self.min = match.group(5)
                self.sec = match.group(6)
                self.valid = True

    def __str__(self) -> str:
        return f'{self.day}/{self.mon}/{self.yr}:{self.hr}:{self.min} {self.sec}' if self.valid else ''

    def __bool__(self) -> bool:
        return self.valid

    def __gt__(self, rhs) -> bool:
        return self.day > rhs.day and self.mon > rhs.mon and self.yr > rhs.yr and \
               self.hr > rhs.hr and self.min > rhs.min and self.sec > rhs.sec

    def __lt__(self, rhs) -> bool:
        return self.day < rhs.day and self.mon < rhs.mon and self.yr < rhs.yr and \
               self.hr < rhs.hr and self.min < rhs.min and self.sec < rhs.sec


class LogEntry:
    regex =  r'(.+?) (.+?) (.+?) \[([^\]]+)\] "(.+?)" (\d{3}) (.+)'
    def __init__(self, uri: str, client_identity: str,  userid: str, timestamp: str,
                 request_header: str, response_code: str, payload_size: str):
        self.uri = uri
        self.client_identity = client_identity
        self.userid = userid
        self.timestamp = timestamp
        self.request = RequestHeader(request_header)
        self.response_code = int(response_code)
        self.payload_size = int(payload_size) if payload_size != '-' else 0

    def __str__(self) -> str:
        return '{} {} {} [{}] "{}" {} {}'.format(
            self.uri, self.client_identity, self.userid, self.timestamp,
            self.request, self.response_code, self.payload_size
        )


class LogParser:
    def __init__(self):
        self.pattern = re.compile(LogEntry.regex)

    def find(self, filename: str, method: str, status: int, begin_time: str = None, end_time: str = None) -> \
            Generator[Tuple[int, LogEntry], None, None]:
        ''' Yields line number and parsed log entry for that line '''

        method_pattern = re.compile(rf'"{method} ')
        status_pattern = re.compile(rf' {status} ')
        date_pattern   = re.compile(r' \[([^\]]+)\] ')

        begin_ts = Timestamp(begin_time)
        end_ts   = Timestamp(end_time)

        with open(filename, 'r', errors='ignore') as f: # File can contain non-ascii characters
            lineno = 0
            for line in f:
                lineno += 1
                ts = None
                if begin_ts or end_ts:
                    date = date_pattern.search(line)
                    if not date: continue
                    ts = Timestamp(date.group(1))
                    if begin_ts and ts < begin_ts: continue
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
