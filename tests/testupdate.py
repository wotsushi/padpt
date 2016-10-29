#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
import csv
import shutil

from padpt import update


class TestUpdate(unittest.TestCase):

    def test_update_00(self):
        url = 'http://localhost/db'
        monsters_csv_path = 'tests/out/db/monsters.csv'
        icons_dir = 'tests/out/db/icons'
        if os.path.exists(monsters_csv_path):
            os.remove(monsters_csv_path)
        if os.path.exists(icons_dir):
            shutil.rmtree(icons_dir)
        os.makedirs(icons_dir)
        update.update_data(
            url,
            monsters_csv_path,
            icons_dir)
        with open(monsters_csv_path) as monsters:
            for monster_id in (
                    monster['monster_id']
                    for monster in csv.DictReader(monsters)):
                self.assertTrue(
                    os.path.exists(
                        os.path.join(
                            icons_dir,
                            '{icon:0>4}.jpg'.format(icon=monster_id))))


if __name__ == '__main__':
    unittest.main()
