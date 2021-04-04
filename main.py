#!/usr/bin/env python3

from os.path import dirname, abspath

import rest_server
import argparse

# Config should have such properties: USER, PASS, DB_SERVER, DB_NAME, HOST, PORT
DEFAULT_CFG = 'server.cfg'

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='REST API example with mysql usage.')
    ap.add_argument('-c', '--config', dest='configfile', help='Config file path, default server.cfg')
    ap.add_argument('--host', dest='host', help='Server host address')
    ap.add_argument('--port', dest='port', help='Server port')
    ap.add_argument('--debug', dest='debug', action='store_true', help='Flask debug mode')
    args = ap.parse_args()

    config_file = args.configfile if args.configfile else dirname(abspath(__file__)) + '/' + DEFAULT_CFG
    config = rest_server.config.read(config_file)

    try:
        rest_server.init(config['USER'], config['PASS'], config['DB_SERVER'], config['DB_NAME'])
        
        host = args.host if args.host else config['HOST']
        port = args.port if args.port else config['PORT']
        
        rest_server.app.run(host=host, port=port, debug=args.debug)
    except KeyError as e:
        print(f'Key {e} is missing from config file \'{config_file}\'.')
        exit(1)
