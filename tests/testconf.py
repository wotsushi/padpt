#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from padpt import conf


class TestConf(unittest.TestCase):

    def test_read_conf00(self):
        config = conf.read_conf('tests/.padpt/padpt.conf')
        self.assertEqual(
            config['PadPT']['Font'],
            '/System/Library/Fonts/ヒラギノ角ゴ ProN W6.otf')
        self.assertEqual(
            config['PadPT']['DB_URL'],
            'http://www.foo.jp/padpt')

    def test_read_alias_00(self):
        alias = conf.read_alias('tests/.padpt/alias.csv')
        self.assertEqual(
            alias['覚醒劉備'],
            2903)

if __name__ == '__main__':
    unittest.main()
