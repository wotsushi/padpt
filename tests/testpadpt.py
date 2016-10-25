#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import io
import shutil
import warnings
import unittest
from unittest.mock import patch

from PIL import Image

from padpt import padpt


class TestPadPT(unittest.TestCase):

    def setUp(self):
        if os.path.exists('tests/tmp'):
            shutil.rmtree('tests/tmp')
        os.mkdir('tests/tmp')

        self.conf_dir = os.path.join(
            os.path.expanduser('~'),
            '.padpt/')
        shutil.move(
            self.conf_dir,
            'tests/tmp/.padpt')
        shutil.copytree(
            'tests/.padpt',
            self.conf_dir)

        self.db_dir = os.path.join(
            os.path.dirname(sys.modules['padpt'].__file__),
            'data/db')
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)
        shutil.move(
            self.db_dir,
            'tests/tmp/data/db')
        shutil.copytree(
            'tests/data/db',
            self.db_dir)

    def tearDown(self):
        shutil.rmtree(self.conf_dir)
        shutil.move(
            'tests/tmp/.padpt',
            self.conf_dir)
        shutil.rmtree(self.db_dir)
        shutil.move(
            'tests/tmp/data/db',
            self.db_dir)

    @patch.object(
        sys,
        'argv',
        ['padpt'])
    @patch.object(
        sys,
        'stdout',
        io.StringIO())
    def test_main_00(self):
        padpt.main()
        self.assertEqual(
            sys.stdout.getvalue(),
            'usage: padpt [-h] [-u] [pt] [out]\n'
            '\n'
            'generates a walkthrough sheet.\n'
            '\n'
            'positional arguments:\n'
            '  pt            pt file to be parsed\n'
            '  out           path of the output file\n'
            '\n'
            'optional arguments:\n'
            '  -h, --help    show this help message and exit\n'
            '  -u, --update  updates database\n'
        )

    @patch.object(
        sys,
        'argv',
        ['padpt', 'tests/in/mill.pt'])
    def test_main_01(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            padpt.main()
            Image.open('tests/in/mill.png').show()
            self.assertEqual(
                'y',
                input('OK? [y/n]'))
        os.remove('tests/in/mill.png')

    @patch.object(
        sys,
        'argv',
        ['padpt', 'tests/in/friday.pt', 'tests/out/testpadpt_02.png'])
    def test_main_02(self):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            padpt.main()
            Image.open('tests/out/testpadpt_02.png').show()
            self.assertEqual(
                'y',
                input('OK? [y/n]'))

if __name__ == '__main__':
    unittest.main()
