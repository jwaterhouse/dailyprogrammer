"""
Solve the bomb diffusal problem using a regex state machine.
"""

import sys
import re

_PATTERN = re.compile('(w[rogp]|r[g]|b[rbp]|o[rb]|g[ow]|p[rb])', flags=re.IGNORECASE)

_DEFUSED = True
if len(sys.argv) > 2:
    for l, n in zip([line[0] for line in sys.argv[1:-1]], [line[0] for line in sys.argv[2:]]):
        if _PATTERN.match(l+n) is None:
            _DEFUSED = False
            break

print("{}".format("Bomb defused" if _DEFUSED else "Boom"))
