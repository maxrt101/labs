#!/usr/bin/env python3

import sys
import parser
import argparse

from datetime import datetime


START_TIME = '01/Jul/1995:02:35:00 -0400'
END_TIME   = '01/Jul/1995:03:18:00 -0400'


class Cli:
    def __init__(self, args):
        self.args = args
        self.args.file = self.args.file[0]
        self.parser = parser.LogParser() 
        self.count = {}
        self.start_time = datetime.strptime(self.args.start_time, parser.LogEntry.time_format)
        self.end_time   = datetime.strptime(self.args.end_time,   parser.LogEntry.time_format)
        if self.args.by_domain and self.args.by_resource:
           parser.error(f'Can have only one --by-X argument at a time.')
           exit()

    def run(self): 
        if self.args.count:
            self._count()
        else:
            self._parse()

    def _count(self):
        lineno, matched, found = 0, 0, 0
        for lineno, entry in self.parser.parse(self.args.file): 
            matched += 1
            if (entry.request.method != self.args.method or entry.response_code != self.args.status or
                entry.timestamp <= self.start_time or entry.timestamp >= self.end_time):
                continue
            found += 1
            key = self._get_key(entry)
            self.count[key] = self.count[key]+1 if key in self.count else 1
        
        self.count = sorted(self.count.items(), key=lambda i: i[1], reverse=not self.args.reverse)
        
        if self.count:
            for i, tup in enumerate(self.count):
                self._display(i, '{}: {}'.format(tup[0], tup[1]))
        else:
            print('No records found for chosen criteria.')
        self._print_summary(f'File "{self.args.file}" summanry: {lineno+1} lines parsed '
                            f'{matched} lines mathched {found} lines counted')

    def _parse(self):
        p = parser.LogParser()
        lineno, matched = 0, 0
        for lineno, entry in self.parser.parse(self.args.file):
            matched += 1
            self._display(lineno, entry)
        self._print_summary(f'File "{self.args.file}" summanry: {lineno+1} lines parsed {matched} lines mathched')

    def _print_summary(self, summary):
        print(f'{parser.BLUE}{summary}{parser.RESET}')

    def _display(self, lineno, line, override=False):
        if (self.args.first and lineno < self.args.first) or self.args.display or override:
            print(line)

    def _get_key(self, entry: parser.LogEntry) -> str:
        if self.args.by_resource:
            return entry.request.url
        if self.args.by_domain:
            return entry.uri
        return entry.uri + entry.request.url


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Counts requests to servers in NSCA access logs with specific HTTPS method and time.'
                    'By default just parses the file and prints summary,')
    ap.add_argument('file', metavar='FILE', nargs=1, help='Log file to parse')
    ap.add_argument('-c', '--count', dest='count', action='store_true', help='Start in count mode.')
    ap.add_argument('-m', '--method', dest='method', default='GET', help='HTTP Method to count on')
    ap.add_argument('-s', '--start', dest='start_time', default=START_TIME, help='Start time')
    ap.add_argument('-e', '--end', dest='end_time', default=END_TIME, help='End time')
    ap.add_argument('-d', '--display', dest='display', action='store_true', help='Display every log line (default false)')
    ap.add_argument('--by-resource', dest='by_resource', action='store_true', help='Count by resource url (default: by url).')
    ap.add_argument('--by-domain', dest='by_domain', action='store_true', help='Count by domain names (default: by url).')
    ap.add_argument('--first', dest='first', type=int, help='Display first N lines')
    ap.add_argument('--status', dest='status', default=200, type=int, help='HTTP response status code')
    ap.add_argument('--sort-reverse', dest='reverse', action='store_true', help='Sort count table desc (default asc)')

    cli = Cli(ap.parse_args())
    cli.run()
else:
    print('WARNING: This script is for console use only!')

