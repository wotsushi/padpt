#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main program.
"""

import os
import sys
import argparse
import datetime

from padpt import padptdb, conf, pt, sheet, update


def main():
    argparser = argparse.ArgumentParser(
        description='generates a walkthrough sheet.')
    argparser.add_argument(
        '-u',
        '--update',
        action='store_true',
        help='updates database')
    argparser.add_argument(
        'pt',
        nargs='?',
        help='pt file to be parsed')
    argparser.add_argument(
        'out',
        nargs='?',
        help='path of the output file')
    args = argparser.parse_args()

    if not args.update and args.pt is None:
        argparser.print_help()
    else:
        def get_conf_path(resource):
            return os.path.join(
                os.path.expanduser('~'),
                '.padpt',
                resource)
        padpt_conf = conf.read_conf(get_conf_path('padpt.conf'))

        def get_data_path(resource):
            return os.path.join(
                os.path.dirname(sys.modules['padpt'].__file__),
                'data',
                resource)
        if args.update:
            if not os.path.exists(get_data_path('db/icons')):
                os.makedirs(get_data_path('db/icons'))
            update.update_data(
                padpt_conf['PadPT']['DB_URL'],
                get_data_path('db/monsters.csv'),
                get_data_path('db/icons'))
        if args.pt is not None:
            sheet.generate_sheet(
                pt=pt.parse_pt(
                    pt_path=args.pt,
                    alias=conf.read_alias(get_conf_path('alias.csv')),
                    monsters=padptdb.read_monsters(
                        get_data_path('db/monsters.csv'),
                        get_data_path('db/icons'))),
                timestamp=str(datetime.date.today()),
                font_path=padpt_conf['PadPT']['Font'],
                png_path=get_data_path('png'),
                out_path=args.out if args.out is not None
                else os.path.splitext(args.pt)[0]+'.png')

if __name__ == '__main__':
    main()
