# -*- coding: utf-8 -*-

import glob
import setuptools
import os
import shutil


def main():
    setuptools.setup(
        name='PadPT',
        version='1.0.0',
        description='PadPT generates a walkthrough sheet'
        'for Puzzle & Dragons.',
        long_description=('PadPT generates a walkthrough sheet'
                          'for Puzzle & Dragons from a text file.'),
        author='wotsushi',
        author_email='wotsushi@gmail.com',
        license='MIT',
        platforms='any',
        install_requires=('Pillow',),
        url='https://github.com/wotsushi',
        packages=setuptools.find_packages(
            exclude=['docs', 'tests', '.padpt']),
        zip_safe=False,
        entry_points="""
        [console_scripts]
        padpt = padpt.padpt:main
        """,
        data_files=(('padpt/data/png', glob.glob('padpt/data/png/*.png')),),
        test_suite='tests')
    if not os.path.exists(os.path.expanduser('~/.padpt')):
        shutil.copytree('.padpt', os.path.expanduser('~/.padpt'))

if __name__ == '__main__':
    main()
