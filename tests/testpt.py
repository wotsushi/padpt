#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from padpt import pt, padptdb, conf


class TestPT(unittest.TestCase):

    def setUp(self):
        self.monsters = padptdb.read_monsters(
            'tests/data/db/monsters.csv',
            'tests/data/db/icons')
        self.alias = conf.read_alias('tests/.padpt/alias.csv')

    def test_parse_pt_00(self):
        mill_pt = pt.parse_pt('tests/in/mill.pt', self.alias, self.monsters)
        self.assertEqual(
            mill_pt,
            pt.PT(
                title='ミル降臨',
                party_a=(
                    pt.Member(
                        monster=self.monsters[2903],
                        assist=self.monsters[2012]),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[1730],
                        assist=self.monsters[3162]),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None)),
                party_b=(
                    pt.Member(
                        monster=self.monsters[2903],
                        assist=self.monsters[923]),
                    pt.Member(
                        monster=self.monsters[2752],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2948],
                        assist=None)),
                note=('1F: Aディオス\n'
                      '2F: Bアヴァロン\n'
                      '3F: Aハーデス，ディオス\n'
                      '4F: Bディオス\n'
                      '5F: Aラー\n'
                      '6F: Aディオス\n'
                      '7F: Bディオス\n'
                      '8F: A0コンボ，Bタナトス，A0コンボ，B0コンボ，A0コンボ，Bディオス\n')))

    def test_parse_pt_01(self):
        friday_pt = pt.parse_pt('tests/in/friday.pt', self.alias, self.monsters)
        self.assertEqual(
            friday_pt,
            pt.PT(
                title='金曜ダンジョン（超地獄級）',
                party_a=(
                    pt.Member(
                        monster=self.monsters[2657],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2368],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2179],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2179],
                        assist=None),
                    pt.Member(
                        monster=self.monsters[2006],
                        assist=None)),
                party_b=(pt.Member(
                    monster=self.monsters[2657],
                    assist=None),),
                note=('1F: ハンジ，赤オーディン\n'
                      '2F: 赤オーディン\n'
                      '3F: 五右衛門\n'
                      '4F: 崩す\n')))

if __name__ == '__main__':
    unittest.main()
