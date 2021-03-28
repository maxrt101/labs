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
import mmap
from datetime import datetime
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


class LogEntry:
    time_format = '%d/%b/%Y:%H:%M:%S %z'

    def __init__(self, uri: str, client_identity: str,  userid: str, timestamp: str,
                 request_header: str, response_code: str, payload_size: str):
        self.uri = uri
        self.client_identity = client_identity
        self.userid = userid
        self.timestamp = datetime.strptime(timestamp, LogEntry.time_format)
        self.request = RequestHeader(request_header)
        self.response_code = int(response_code)
        self.payload_size = int(payload_size) if payload_size != '-' else 0

    def __str__(self) -> str:
        return '{} {} {} [{}] "{}" {} {}'.format(
            self.uri, self.client_identity, self.userid,
            self.timestamp.strftime(LogEntry.time_format),
            self.request, self.response_code, self.payload_size
        )


class LogParser:
    regex_pattern = r'(.+?) (.+?) (.+?) \[([^\]]+)\] "(.+?)" (\d{3}) (.+)'

    def __init__(self):
        self.pattern = re.compile(LogParser.regex_pattern)

    def parse(self, filename: str) -> Generator[Tuple[int, LogEntry], None, None]:
        ''' Yields line number and parsed log entry for that line '''
        with open(filename, 'r', errors='ignore') as f: # File can contain non-ascii characters
            lineno = 0
            for line in f:
                lineno += 1
                result = self.pattern.search(line)
                if result:
                    yield lineno, LogEntry(result.group(1), result.group(2),
                                           result.group(3), result.group(4), result.group(5),
                                           result.group(6), result.group(7))
                else:
                    error(f'Matching line {lineno}: "{line}"')
