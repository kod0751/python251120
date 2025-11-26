import mod1

print(mod1.add(1,2))

from mod1 import add, sub

print(add(1,2))
print(sub(1,2))

import sys
print( sys.path )