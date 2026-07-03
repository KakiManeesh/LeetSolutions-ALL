# Last updated: 7/3/2026, 12:55:20 PM
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):

            digits = list(map(int, str(x)))
            n = len(digits)

            @cache
            def dfs(pos, tight, started, prev2, prev1):

                # reached end
                if pos == n:
                    return (1, 0)   # (cnt, wav)

                limit = digits[pos] if tight else 9

                total_cnt = 0
                total_wav = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    # leading zeros
                    if not started:

                        if d == 0:
                            cnt, wav = dfs(
                                pos + 1,
                                ntight,
                                False,
                                -1,
                                -1
                            )

                        else:
                            cnt, wav = dfs(
                                pos + 1,
                                ntight,
                                True,
                                -1,
                                d
                            )

                        total_cnt += cnt
                        total_wav += wav

                    else:

                        extra = 0

                        # we have 3 digits now
                        if prev2 != -1:

                            if prev2 < prev1 > d:
                                extra = 1

                            elif prev2 > prev1 < d:
                                extra = 1

                        # shift window
                        if prev2 == -1:
                            nprev2 = prev1
                            nprev1 = d
                        else:
                            nprev2 = prev1
                            nprev1 = d

                        cnt, wav = dfs(
                            pos + 1,
                            ntight,
                            True,
                            nprev2,
                            nprev1
                        )

                        total_cnt += cnt
                        total_wav += wav + extra * cnt

                return total_cnt, total_wav

            return dfs(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)