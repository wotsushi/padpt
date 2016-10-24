# -*- coding: utf-8 -*-

"""This module handles config files.
"""

import configparser
import csv


def read_conf(conf_path):
    """Reads padpt.conf at the specified path.
    Then returns a configparser for padpt.conf.
    """
    config_parser = configparser.ConfigParser()
    config_parser.read(conf_path)
    return config_parser


def read_alias(alias_csv_path):
    """Reads alias.csv at the specified path.
    Then returns a dict mapping from alias to monster id.
    """
    with open(alias_csv_path) as alias_csv:
        return {
            alias: int(monster_id)
            for alias, monster_id in csv.reader(alias_csv)}
