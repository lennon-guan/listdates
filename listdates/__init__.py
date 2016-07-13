#!/usr/bin/env python

from __future__ import print_function
import sys
import re
import datetime
import operator

__version__ = '0.0.1'

_DATE_PATTERNS = (
    (re.compile(r'^\d{8}$'), '%Y%m%d'),
    (re.compile(r'^\d{6}$'), '%y%m%d'),
    (re.compile(r'^\d{4}\-\d{2}\-\d{2}$'), '%Y-%m-%d'),
    (re.compile(r'^\d{2}\-\d{2}\-\d{2}$'), '%y-%m-%d'),
)

def _parse_date(datestr):
    for pattern, fmt in _DATE_PATTERNS:
        if pattern.match(datestr):
            return datetime.datetime.strptime(datestr, fmt)
    raise ValueError('invalid date string %s' % datestr)

def iter_dates(d1, d2, fmt):
    d1 = _parse_date(d1)
    d2 = _parse_date(d2)
    if d1 > d2:
        op = operator.ge
        step = -1
    else:
        op = operator.le
        step = 1
    res = []
    while op(d1, d2):
        yield d1.strftime(fmt)
        d1 += datetime.timedelta(days=step)

def main(args=None, options=None):
    if args is None:
        args = sys.argv[1:]
    if len(args) != 3:
        print('Usage: listdates <first_date> <last_date> <output_date_format>')
        return
    d1, d2, fmt = args
    for d in iter_dates(d1, d2, fmt):
        print(d)

if '__main__' == __name__:
    main(sys.argv[1:])

