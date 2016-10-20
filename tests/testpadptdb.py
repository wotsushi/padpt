#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from padpt import padptdb


class TestPadPTDB(unittest.TestCase):

    def assertMonster(self, monster, monster_id,
                      skill_boost, skill_lock, jammers, poison, dark):
        return self.assertEqual(
            monster,
            padptdb.Monster(
                monster_id=monster_id,
                awoken_skills=padptdb.AwokenSkills(
                    skill_boost=skill_boost,
                    skill_lock=skill_lock,
                    jammers=jammers,
                    poison=poison,
                    dark=dark),
                icon_path='tests/data/db/icons/{0:0>4}.jpg'.format(
                    monster_id)))

    def test_read_monsters_00(self):
        monsters = padptdb.read_monsters(
            'tests/data/db/monsters.csv',
            'tests/data/db/icons')
        self.assertMonster(
            monster=monsters[2903],
            monster_id=2903,
            skill_boost=2,
            skill_lock=0,
            jammers=1,
            poison=0,
            dark=0)

    def test_read_monsters_01(self):
        monsters = padptdb.read_monsters(
            'tests/data/db/monsters.csv',
            'tests/data/db/icons')
        self.assertMonster(
            monster=monsters[923],
            monster_id=923,
            skill_boost=1,
            skill_lock=0,
            jammers=0,
            poison=0,
            dark=0)


if __name__ == '__main__':
    unittest.main()
