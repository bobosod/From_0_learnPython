import sys
print(sys.modules.keys())
print(sys.modules.values())

d = sys.modules.copy()
import copy, string
print(zip(set(sys.modules) - set(d)))
