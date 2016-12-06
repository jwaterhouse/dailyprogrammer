"""
Solve the bomb diffusal problem.
"""

import sys

_STATE_MACHINE = {
    '0': {'w': '1', 'r': '2'},  # Start
    '1': {'w': '2', 'o': '3'},
    '2': {'r': '0', 'b': '3'},
    '3': {'g': '4', 'o': '5', 'b': '3'},
    '4': {'o': '6'},
    '5': {'g': '6'},
    '6': None   # Defused
}

def defuse(wires):
    state = '0'
    for wire in wires:
        if wire in list(_STATE_MACHINE[state].keys()):
            state = _STATE_MACHINE[state][wire]
        else:
            break
    return _STATE_MACHINE[state] is None

def defusable(state, wires):
    if _STATE_MACHINE[state] is None:
        return sum(wires.values()) == 0
    for wire in list(_STATE_MACHINE[state].keys()):
        if wire in wires and wires[wire] > 0:
            wires[wire] -= 1
            if defusable(_STATE_MACHINE[state][wire], wires):
                return True
            wires[wire] += 1
    return False

def handle(lines):
    if len(lines[0].split(' ')) == 2:
        wires = dict(zip([l[0] for l in lines], [int(l.split(' ')[1]) for l in lines]))
        print("defusable" if defusable('0', wires) else "not defusable")
    else:
        wires = [l[0] for l in lines]
        print("defused" if defuse(wires) else "Booom")

handle(sys.stdin.readlines())
