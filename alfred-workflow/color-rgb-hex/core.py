#!/usr/bin/env python
# encoding: utf-8
import sys

from workflow import Workflow
'''颜色转换:RGB 转换十六进制'''
dec_hex_map = {'10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
hex_dec_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def dec_to_hex(dec):
    '''十进制转换十六进制'''
    first = str(dec / 16)
    second = str(dec % 16)
    hex_first = dec_hex_map[first] if (first in dec_hex_map) else first
    hex_second = dec_hex_map[second] if second in dec_hex_map else second
    return hex_first + hex_second


def rgb_to_hex(wf):
    str_args = wf.args
    int_agrs = map(lambda x: int(x), str_args)
    ret = ''.join(map(dec_to_hex, int_agrs))
    return ret


def hex_to_rgb(wf):
    hex_str = map(lambda x: hex_dec_map[x] if x in hex_dec_map else int(x), wf.args[0])
    red = hex_str[0] * 16 + hex_str[1]
    green = hex_str[2] * 16 + hex_str[3]
    black = hex_str[4] * 16 + hex_str[5]
    return red, green, black


def color_handler(wf):
    str_args = wf.args
    if len(str_args) == 1:
        ret = hex_to_rgb(wf)
        wf.add_item('RGB(%s %s %s)' % ret, 'HEX: %s' % str_args[0])
    else:
        ret = rgb_to_hex(wf)
        wf.add_item('HEX: %s' % ret, 'RGB(%s %s %s)' % tuple(str_args))
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(color_handler))
