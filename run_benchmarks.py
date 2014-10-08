#!/usr/bin/env python

from __future__ import division
import timeit
import os

cc = 'clang -Os'
cpp = 'clang++ -Os -std=c++11'

TRIALS = 5

tests = [
    'c1.c',
    'cpp1.cpp',
    '1000_structs.cpp',
    '1000_structs_no_free.cpp',
    '1000_unique_ptrs.cpp',
    '1000_identical_unique_ptrs.cpp',
]

def sys(s):
    result = os.system(s)
    if 0 != result:
        raise 'It failed. :('

def benchmarkCompile(fileName):
    compiler = cc if fileName.endswith('.c') else cpp

    outFile = fileName.replace('.cpp', '').replace('.c', '')
    totalTime = timeit.timeit(
        stmt=lambda: sys('%s %s -Wall -Werror -o %s' % (compiler, fileName, outFile)),
        number=TRIALS
    )

    size = os.stat(outFile).st_size

    return (totalTime / TRIALS, size)

for f in tests:
    seconds, size = benchmarkCompile(f)
    kb = size / 1024
    print '%40s : %4ims\t%4ikb' % (f, seconds * 1000, kb)
