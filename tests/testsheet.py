#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import warnings

from PIL import Image

from padpt import padptdb, pt, sheet


class TestSheet(unittest.TestCase):

    def setUp(self):
        self.monsters = padptdb.read_monsters(
            'tests/data/db/monsters.csv',
            'tests/data/db/icons')

    def test_generate_sheet_00(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sheet.generate_sheet(
                pt=pt.PT(
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
                          '8F: A0コンボ，Bタナトス，A0コンボ，B0コンボ，A0コンボ，Bディオス\n')),
                timestamp='2016-09-22',
                font_path='/System/Library/Fonts/ヒラギノ角ゴ ProN W6.otf',
                png_path='tests/data/png/',
                out_path='tests/out/testsheet_00.png')
            Image.open('tests/out/testsheet_00.png').show()
            self.assertEqual(
                'y',
                input('OK? [y/n]'))

    def test_generate_sheet_01(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            sheet.generate_sheet(
                pt=pt.PT(
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
                          '4F: 崩す\n')),
                timestamp='2016-09-22',
                font_path='/System/Library/Fonts/ヒラギノ角ゴ ProN W6.otf',
                png_path='tests/data/png/',
                out_path='tests/out/testsheet_01.png')
            Image.open('tests/out/testsheet_01.png').show()
            self.assertEqual(
                'y',
                input('OK? [y/n]'))

if __name__ == '__main__':
    unittest.main()
