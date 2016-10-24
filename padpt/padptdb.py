# -*- coding: utf-8 -*-

"""This module handles data files.
"""

import os
import csv
import collections

AwokenSkills = collections.namedtuple(
    'AwokenSkills',
    ('skill_boost', 'skill_lock', 'jammers',
     'poison', 'dark'))

Monster = collections.namedtuple(
    'Monster',
    ('monster_id', 'awoken_skills', 'icon_path'))


def read_monsters(monsters_csv_path, icons_dir):
    """Reads the specified csv file about monsters.
    Then returns a dict mapping from monster id to monster data.
    """
    with open(monsters_csv_path) as monsters_csv:
        return {
            int(monster['monster_id']): Monster(
                monster_id=int(monster['monster_id']),
                awoken_skills=AwokenSkills(**{
                    awoken_skill: int(monster[awoken_skill])
                    for awoken_skill in AwokenSkills._fields}),
                icon_path=os.path.join(
                    icons_dir,
                    '{0:0>4}.jpg'.format(monster['monster_id'])))
            for monster in csv.DictReader(monsters_csv)}
