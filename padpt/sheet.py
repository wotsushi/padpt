# -*- coding: utf-8 -*-

"""This module generates a walkthrough sheet.
"""

import os
import itertools
import operator
from PIL import Image, ImageColor, ImageDraw, ImageFont

from padpt import padptdb


def _join_h(imgs, align_ratio=0):
    joined_img = Image.new(
        mode='RGB',
        size=(sum(map(operator.attrgetter('width'), imgs)),
              max(0, *map(operator.attrgetter('height'), imgs))),
        color=ImageColor.getrgb('white'))
    for img, offset in zip(
            imgs,
            itertools.accumulate(
                itertools.chain(
                    (0,),
                    map(
                        operator.attrgetter('width'),
                        imgs)))):
        joined_img.paste(
            img,
            (offset, int(align_ratio * (joined_img.height - img.height))))
    return joined_img


def _join_v(imgs, align_ratio=0):
    joined_img = Image.new(
        mode='RGB',
        size=(max(0, *map(operator.attrgetter('width'), imgs)),
              sum(map(operator.attrgetter('height'), imgs))),
        color=ImageColor.getrgb('white'))
    for img, offset in zip(
            imgs,
            itertools.accumulate(
                itertools.chain(
                    (0,),
                    map(
                        operator.attrgetter('height'),
                        imgs)))):
        joined_img.paste(
            img,
            (int(align_ratio * (joined_img.width - img.width)), offset))
    return joined_img


def generate_sheet(pt, timestamp, font_path, png_path, out_path):
    """Generates a waklthrough sheet corresponding
    the specified pt object into the specified directory.
    """
    def new_txtimg(txt, font_size=20):
        font = ImageFont.truetype(
            font=font_path,
            size=font_size)
        txtimg = Image.new(
            mode='RGB',
            size=ImageDraw.Draw(Image.new('RGB', (0, 0))).textsize(
                text=txt,
                font=font),
            color=ImageColor.getrgb('white'))
        ImageDraw.Draw(txtimg).text(
            xy=(0, 0),
            text=txt,
            fill=ImageColor.getrgb('black'),
            font=font)
        return txtimg

    def open_png(png):
        return Image.open(os.path.join(
            png_path,
            '{}.png'.format(png)))

    title_img = new_txtimg(
        txt=pt.title,
        font_size=36)
    timestamp_img = new_txtimg(timestamp)
    party_a_img = _join_h(
        imgs=(
            open_png('A'),
            *(_join_v(
                imgs=(Image.open(member.monster.icon_path),)
                if member.assist is None
                else (Image.open(member.assist.icon_path),
                      open_png('extend_a'),
                      Image.open(member.monster.icon_path)),
                align_ratio=1/2) for member in pt.party_a)),
        align_ratio=1)
    party_b_img = _join_h(
        imgs=(
            open_png('B'),
            *(_join_v(
                imgs=(Image.open(member.monster.icon_path),)
                if member.assist is None
                else (Image.open(member.monster.icon_path),
                      open_png('extend_b'),
                      Image.open(member.assist.icon_path)),
                align_ratio=1/2) for member in pt.party_b)),
        align_ratio=0)
    awoken_skills_img = _join_v(tuple(
        _join_h(
            imgs=(
                open_png(awoken_skill),
                new_txtimg(str(sum(map(
                    operator.attrgetter(awoken_skill),
                    (member.monster.awoken_skills
                     for member in itertools.chain(
                             pt.party_a,
                             pt.party_b))))))),
            align_ratio=1/2)
        for awoken_skill in padptdb.AwokenSkills._fields))
    note_img = new_txtimg(pt.note)

    sheet = _join_v((
        title_img,
        timestamp_img,
        _join_h(
            imgs=(_join_v((
                party_a_img,
                party_b_img)),
                  awoken_skills_img),
            align_ratio=1/2),
        note_img))
    sheet.save(out_path, 'PNG')
