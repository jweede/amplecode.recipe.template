#!/usr/bin/env python
# -*- coding: utf-8 -*-

def riba(s):
    """docstring for riba"""
    return s


def lwrap(l, w=None):
    """docstring for lwrap"""
    result = []
    o = w or '"'
    for elem in l:
        result.append(o + elem + o)
    return result
