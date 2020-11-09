#!/usr/bin/env python3
import sys
def func1(a, b):
    c=a+b
    return c
def test_answer():
    assert func1(3,3) == 4
test_answer()
print(func1(int(sys.argv[1]),int(sys.argv[2])))



