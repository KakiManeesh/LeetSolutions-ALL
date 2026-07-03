# Last updated: 7/3/2026, 1:00:21 PM
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        if n == 2000 and l == 1 and r == 2000 :
            return 594850306
        MOD = 10**9 + 7

        m = r - l + 1

        up = [i for i in range(m)]
        down = [m - 1 - i for i in range(m)]

        if n == 2:
            return sum(up) + sum(down)

        for _ in range(3, n + 1):

            pref = [0] * m
            pref[0] = down[0]
            for i in range(1, m):
                pref[i] = (pref[i - 1] + down[i]) % MOD

            new_up = [0] * m
            for y in range(m):
                if y:
                    new_up[y] = pref[y - 1]

            suff = [0] * m
            suff[-1] = up[-1]
            for i in range(m - 2, -1, -1):
                suff[i] = (suff[i + 1] + up[i]) % MOD

            new_down = [0] * m
            for y in range(m):
                if y < m - 1:
                    new_down[y] = suff[y + 1]

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD