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

    def parse_party(party):
        return tuple(
            Member(*(
                monsters[alias[monster_name]]
                for monster_name in member.split(',')))
            for member in party.rstrip().splitlines())

    return PT(
        title=tokens.group('title'),
        party_a=parse_party(tokens.group('party_a')),
        party_b=parse_party(tokens.group('party_b')),
        note=tokens.group('note'))
