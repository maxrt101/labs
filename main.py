#!/usr/bin/env python3

import log_parser
import argparse


class Cli:
    def __init__(self, args):
        self.args = args
        self.args.file = self.args.file[0]
        self.parser = log_parser.LogParser() 
        self.count = {}
        if self.args.by_domain and self.args.by_resource:
            log_parser.error(f'Can have only one --by-X argument at a time.')
            exit()
        if not self.args.count and (self.args.by_domain or self.args.by_resource):
            log_parser.error(f'--by-X arguments are useless in parse mode (use -c)')
            exit()

    def run(self): 
        if self.args.count:
            self._count()
        else:
            self._parse()

    def _parse(self):
        lineno, matched =  0, 0
        for lineno, entry in self.parser.find(self.args.file, self.args.method, self.args.status, \
                                              self.args.begin_time, self.args.end_time ): 
            matched += 1
            self._display(lineno, entry)

        self._print_summary(f'File "{self.args.file}" summanry: {lineno} lines parsed '
                            f'{matched} lines mathched')

    def _count(self):
        lineno, matched= 0, 0
        for lineno, entry in self.parser.find(self.args.file, self.args.method, self.args.status, \
                                              self.args.begin_time, self.args.end_time ): 
            matched += 1
            key = self._get_key(entry)
            self.count[key] = self.count[key]+1 if key in self.count else 1
        
        self.count = sorted(self.count.items(), key=lambda i: i[1], reverse=not self.args.reverse)
        
        if self.count:
            for i, tup in enumerate(self.count):
                self._display(i, '{}: {}'.format(tup[0], tup[1]))
        else:
            print('No records found for chosen criteria.')
        self._print_summary(f'File "{self.args.file}" summanry: {lineno} lines parsed '
                            f'{matched} lines mathched')

    def _print_summary(self, summary):
        print(f'{log_parser.BBLUE}{summary}{log_parser.RESET}')

    def _display(self, lineno, line, override=False):
        if (self.args.first and lineno < self.args.first) or self.args.display or override:
            print(line)

    def _get_key(self, entry: log_parser.LogEntry) -> str:
        if self.args.by_resource:
            return entry.request.url
        if self.args.by_domain:
            return entry.uri
        return entry.uri + entry.request.url


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Counts requests to servers in NSCA access logs with specific HTTPS method and response code. '
                    'It is also possible to specify time bounds. Status and method parameters can take regexes. '
                    'Default values for status and method are wildcard.'
                    'By default just parses the file and prints summary.')
    ap.add_argument('file', metavar='FILE', nargs=1, help='Log file to parse')
    ap.add_argument('-c', '--count', dest='count', action='store_true', help='Start in count mode')
    ap.add_argument('-m', '--method', dest='method', default='.+', help='HTTP Method (Default ".+")')
    ap.add_argument('-s', '--status', dest='status', default='\d{3}', help='HTTP Status code (Default "\d{3}")')
    ap.add_argument('-b', '--begin', dest='begin_time', help='Lower time bound')
    ap.add_argument('-e', '--end', dest='end_time', help='Upper time bound')
    ap.add_argument('-d', '--display', dest='display', action='store_true', help='Display every log line (Default off)')
    ap.add_argument('--first', dest='first', type=int, help='Display first N lines')
    ap.add_argument('--by-resource', dest='by_resource', action='store_true', help='Count by resource url (Default: by url).')
    ap.add_argument('--by-domain', dest='by_domain', action='store_true', help='Count by domain names (Default: by url).')
    ap.add_argument('--sort-reverse', dest='reverse', action='store_true', help='Sort count table DESC instead of default ASC')

    cli = Cli(ap.parse_args())
    cli.run()
else:
    print('WARNING: This script is for console use only!')

