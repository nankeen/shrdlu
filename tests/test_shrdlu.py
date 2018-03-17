#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shrdlu.shrdlu import Shrdlu

__author__ = "NaNkeen"
__copyright__ = "NaNkeen"
__license__ = "gpl3"


def test_frequencies():
    shrdlu = Shrdlu("AAAaaBbC1,32")
    assert shrdlu.frequencies == {'a': 5, 'b': 2, 'c': 1}


def test_chisquared_calculations():
    shrdlu = Shrdlu("AAAaaBbC1,32eee")
    print(shrdlu.frequencies)
    print(shrdlu.text)
    print(shrdlu.chi_squared())
    assert shrdlu.chi_squared() == 1.838582133379139


def test_english():
    shrdlu = Shrdlu("This is quite the test might I say, so fun to conduct")
    print(shrdlu.chi_squared())
    assert shrdlu.test()
    shrdlu = Shrdlu("Are you here to take your gift?")
    print(shrdlu.chi_squared())
    assert shrdlu.test()
    shrdlu = Shrdlu("fdafsasdfjnvklsakdlkasduhg8mgbbbbbkmznbvuqefaf")
    print(shrdlu.chi_squared())
    assert shrdlu.test() is False
    shrdlu = Shrdlu("1313;'..2")
    print(shrdlu.chi_squared())
    assert shrdlu.test() is False
