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
    assert shrdlu.chi_squared() == 11.946038246429259
    assert shrdlu.chi_squared() == shrdlu.chi_squared()


def test_english_positive():
    a = Shrdlu("I'll never forget this experience.")
    b = Shrdlu("Are you here to take your gift?")
    c = Shrdlu("I recommend 7 doses of herbal medication")
    d = Shrdlu("She went shopping with him last Monday.")
    assert a.test()
    assert b.test()
    assert c.test()
    assert d.test()


def test_english_negative():
    a = Shrdlu("\xe3\x21\x43\x56\xf0\x12\xff")
    b = Shrdlu("nasiwawujipaban nasiwawujipaban aikizepuiki")
    c = Shrdlu("123;'./,'[o\[]]]]';';/..129!@#$%^&")
    d = Shrdlu("mlopllmzkzzzzi12zz[llas2]pmelakpz")
    assert a.test() is False
    assert b.test() is False
    assert c.test() is False
    assert d.test() is False

