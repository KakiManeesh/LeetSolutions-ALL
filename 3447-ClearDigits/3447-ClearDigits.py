# Last updated: 7/3/2026, 12:49:30 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        '''

        stack = []
        for i in s :
            if i.isalpha():
                stack.append(i)
            else:
                stack.pop()
        return "".join(stack)

        '''

        stack = ""
        for i in s :
            if i.isalpha():
                stack += i
            else:
                stack = stack[:-1]
        return stack