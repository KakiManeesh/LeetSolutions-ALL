# Last updated: 7/3/2026, 12:55:06 PM
class Solution:
    def mirrorFrequency(self, s: str) -> int:
        def mirror_char(c):
            if c.isdigit():
                return chr(ord('0') + (9 - (ord(c) - ord('0'))))
            else:  # letters
                return chr(ord('a') + (25 - (ord(c) - ord('a'))))

        freq = {}

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        total = 0
        checked = set()

        for c in freq:
            if c in checked:
                continue

            mirror = mirror_char(c)

            total += abs(freq[c] - freq.get(mirror, 0))

            checked.add(c)
            checked.add(mirror)

        return total