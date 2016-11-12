#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""This is the main program.
"""

import os
import sys
import argparse
import datetime
import configparser
import urllib.error

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
                os.path.expanduser('~/.padpt'),
                resource)

        try:
            padpt_conf = conf.read_conf(get_conf_path('padpt.conf'))
        except FileNotFoundError as e:
            sys.exit(
                '{} does not exist.'.format(
                    e.filename))
        except configparser.Error:
            sys.exit(
                'There is an error in padpt.conf')

        def get_data_path(resource):
            return os.path.join(
                os.path.dirname(sys.modules['padpt'].__file__),
                'data',
                resource)

        monsters_csv_path = get_data_path('db/monsters.csv')
        icons_dir = get_data_path('db/icons')
        if args.update:
            if not os.path.exists(icons_dir):
                os.makedirs(icons_dir)
            try:
                update.update_data(
                    url=padpt_conf['PadPT']['DB_URL'],
                    monsters_csv_path=monsters_csv_path,
                    icons_dir=icons_dir)
            except KeyError as e:
                sys.exit(
                    'There is an error in padpt.conf')
            except urllib.error.URLError as e:
                sys.exit(
                    'Failed to download {}'.format(
                        padpt_conf['PadPT']['DB_URL']))
        if args.pt is not None:
            try:
                sheet.generate_sheet(
                    pt=pt.parse_pt(
                        pt_path=args.pt,
                        alias=conf.read_alias(get_conf_path('alias.csv')),
                        monsters=padptdb.read_monsters(
                            monsters_csv_path,
                            icons_dir)),
                    timestamp=str(datetime.date.today()),
                    font_path=padpt_conf['PadPT']['Font'],
                    png_path=get_data_path('png'),
                    out_path=(
                        args.out if args.out is not None
                        else os.path.splitext(args.pt)[0]+'.png'))
            except FileNotFoundError as e:
                sys.exit(
                    '{} does not exist.'.format(
                        e.filename))
            except pt.PTError as e:
                sys.exit(
                    '{} has a syntax error.'.format(
                        e.pt_path))
            except pt.AliasError as e:
                sys.exit(
                    '{} is undefined in alias.csv.'.format(
                        e.get_name()))
            except pt.MonsterError as e:
                sys.exit(
                    'The monster whose monster ID is {}'
                    'is not registerd with your monster DB.'.format(
                        e.get_monster_id()))
            except KeyError as e:
                sys.exit(
                    'There is an error in padpt.conf')

if __name__ == '__main__':
    main()
