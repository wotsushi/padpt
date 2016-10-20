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
        monsters_csv = 'tests/out/db/monsters.csv'
        icons = 'tests/out/db/icons'
        os.remove(monsters_csv)
        shutil.rmtree(icons)
        os.mkdir(icons)
        update.update_data(
            url=url,
            monsters_csv=monsters_csv,
            icons=icons)
        with open(monsters_csv) as monsters:
            for monster_id in (monster['monster_id']
                               for monster in csv.DictReader(monsters)):
                self.assertTrue(os.path.exists(os.path.join(
                    icons,
                    '{icon:0>4}.jpg'.format(icon=monster_id))))

if __name__ == '__main__':
    unittest.main()
