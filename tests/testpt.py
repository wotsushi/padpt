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

    def test_PTError_00(self):
        self.assertEqual(
            str(pt.PTError('tests/in/mill.pt')),
            'tests/in/mill.pt has a syntax error.')

    def test_AliasError_00(self):
        self.assertEqual(
            pt.AliasError('覚醒劉備').get_name(),
            '覚醒劉備')

    def test_MonsterError_00(self):
        self.assertEqual(
            pt.MonsterError(2903).get_monster_id(),
            2903)

    def test_parse_pt_00(self):
        mill_pt = pt.parse_pt(
            'tests/in/mill.pt',
            self.alias,
            self.monsters)
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
        friday_pt = pt.parse_pt(
            'tests/in/friday.pt',
            self.alias,
            self.monsters)
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

    def test_parse_pt_02(self):
        """Assume that tests/in/pterror.pt does not exist.
        """
        with self.assertRaises(pt.PTError):
            mill_pt = pt.parse_pt(
                pt_path='tests/in/pterror.pt',
                alias=self.alias,
                monsters=self.monsters)

    def test_parse_pt_03(self):
        with self.assertRaises(pt.AliasError):
            mill_pt = pt.parse_pt(
                pt_path='tests/in/aliaserror.pt',
                alias=self.alias,
                monsters=self.monsters)

    def test_parse_pt_04(self):
        with self.assertRaises(pt.MonsterError):
            mill_pt = pt.parse_pt(
                pt_path='tests/in/mill.pt',
                alias=self.alias,
                monsters=padptdb.read_monsters(
                    'tests/data/db/monstererror.csv',
                    'tests/data/db/icons'))

if __name__ == '__main__':
    unittest.main()
