#!/bin/env python
import hashlib
import sys

# print(hashlib.algorithms_available)
arg = sys.argv[1]

h = hashlib.md5()
h.update(arg.encode("utf-8"))
wynik = h.digest()

print(h.hexdigest(), wynik)
