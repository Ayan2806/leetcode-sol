class Solution(object):
    def minInsertions(self, s):
        res = 0     # total insertions
        need = 0    # number of ')' needed
        i = 0
        while i < len(s):
            if s[i] == '(':
                need += 2
                if need % 2 == 1:
                    res += 1     
                    need -= 1
            else:  # it's a ')'
                need -= 1
                if need == -1:
                    res += 1     
                    need = 1
            i += 1
        return res + need