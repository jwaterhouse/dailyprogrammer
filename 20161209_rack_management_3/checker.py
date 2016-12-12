import sys
from collections import Counter

N = 10  # number of tiles in the rack
words = set(line.strip() for line in open("enable1.txt"))
row = "sd?zeioao?mluvepesceinfxt?wyiru?ie?giator?t??nuefje?l?odndrotpewlgoobiinysagacaqski?aeh?rbhaervtnl?m"
rack = []
score = 0
for line in sys.stdin:
    if not line: continue
    leftdraws, play, word = line.split()
    # Draw from the left
    leftdraws = int(leftdraws)
    assert leftdraws <= len(row), "Not enough tiles to draw from"
    rack += list(row[:leftdraws])
    row = row[leftdraws:]
    assert len(rack) <= N, "Drew too many tiles"
    # Draw remaining from the right
    rightdraws = min(len(row), N - len(rack))
    if rightdraws:
        rack += list(row[-rightdraws:])
        row = row[:-rightdraws]
    # Check that play is legal
    print(play)
    print(rack)
    assert not Counter(play) - Counter(rack), "Cannot make given play"
    assert len(play) == len(word) and all(a in ("?", b) for a, b in zip(play, word))
    assert word in words
    # Remove letters from rack
    rack = list((Counter(rack) - Counter(play)).elements())
    # Add score
    tilescores = dict(zip("abcdefghijklmnopqrstuvwxyz?",
        [1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10,0]))
    print(sum(j * tilescores[char] for j, char in enumerate(play, 1)))
    score += sum(j * tilescores[char] for j, char in enumerate(play, 1))
print(score)