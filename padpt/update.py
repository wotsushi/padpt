# -*- coding: utf-8 -*-

"""This module updates data files.
"""

import csv
from urllib import request
import os
import tqdm


def update_data(url, monsters_csv_path, icons_dir):
    """Updates the specified csv file and icon files from
    the specified URL.
    """
    with request.urlopen(
            '{url}/monsters.csv'.format(
                url=url)) as updated_monsters,\
        open(
            monsters_csv_path, 'w') as monsters:
        monsters.write(updated_monsters.read().decode('utf-8'))
    with open(monsters_csv_path) as monsters:
        for monster_id in tqdm.tqdm(tuple(
                monster['monster_id']
                for monster in csv.DictReader(monsters))):
            with request.urlopen(
                    '{url}/icons/{icon}.jpg'.format(
                        url=url,
                        icon=monster_id)) as updated_icon,\
                 open(
                     os.path.join(
                         icons_dir,
                         '{icon:0>4}.jpg'.format(icon=monster_id)),
                     'wb') as icon:
                icon.write(updated_icon.read())
