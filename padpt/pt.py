# -*- coding: utf-8 -*-

"""This module parses pt files.
"""

import collections
import re


Member = collections.namedtuple(
    'Member',
    ('monster', 'assist'))

Member.__new__.__defaults__ = (None,)

PT = collections.namedtuple(
    'PT',
    ('title', 'party_a', 'party_b', 'note'))

_NOTE = r'((.|\n)*)'
_NAMECHAR = r'([^\n,])'
_MONSTER = r'({namechar}+)'.format(namechar=_NAMECHAR)
_MEMBER = r'(({monster}|{monster},{monster})\n)'.format(monster=_MONSTER)
_PARTY = r'({member}{{0,5}})'.format(member=_MEMBER)
_TITLE = r'((({namechar}|,))*)'.format(namechar=_NAMECHAR)


class PTError(Exception):
    """Raised when a parsed pt file has a syntax error.
    """

    def __init__(self, pt_path):
        self.pt_path = pt_path

    def __str__(self):
        return '{} has a syntax error.'.format(self.pt_path)


class AliasError(KeyError):
    """Raised when a parsed pt file contains an unknown
    monster name.
    """

    def __init__(self, name):
        super().__init__(name)

    def get_name(self):
        return self.args[0]

class MonsterError(KeyError):
    """Raised when a parsed pt file contains a monster name
    whose monster id is not registered.
    """

    def __init__(self, monster_id):
        super().__init__(monster_id)

    def get_monster_id(self):
        return self.args[0]



def parse_pt(pt_path, alias, monsters):
    """Parses the input pt file at the specified path.
    Then returns a PT object corresponding the input pt file.
    """

    with open(pt_path) as pt:
        tokens = re.match(
            r'(?P<title>{title})\n'
            r'\n'
            r'(?P<party_a>{party})'
            r'\n'
            r'(?P<party_b>{party})'
            r'\n'
            r'(?P<note>{note})'.format(
                title=_TITLE,
                party=_PARTY,
                note=_NOTE),
            pt.read())
    if tokens is None:
        raise PTError(pt_path)

    def resolute_monster_name(monster_name):
        try:
            return alias[monster_name]
        except KeyError as e:
            raise AliasError(monster_name)

    def get_monster(monster_id):
        try:
            return monsters[monster_id]
        except KeyError as e:
            raise MonsterError(monster_id)

    def parse_party(party):
        return tuple(
            Member(*(
                get_monster(
                    resolute_monster_name(
                        monster_name))
                for monster_name in member.split(',')))
            for member in party.rstrip().splitlines())

    return PT(
        title=tokens.group('title'),
        party_a=parse_party(tokens.group('party_a')),
        party_b=parse_party(tokens.group('party_b')),
        note=tokens.group('note'))
