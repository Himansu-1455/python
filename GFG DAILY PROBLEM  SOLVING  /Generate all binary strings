class Solution:
    # recursive function to generate all binary strings
    def binstrRec(self, s, i, res):
        n = len(s)

        # if string is complete, add to result
        if i == n:
            res.append("".join(s))
            return

     # assign '0' at current position
        s[i] = '0'
        self.binstrRec(s, i + 1, res)

        # assign '1' at current position
        s[i] = '1'
        self.binstrRec(s, i + 1, res)

    def binstr(self, n):
        s = ['0'] * n
        res = []
        self.binstrRec(s, 0, res)
        return res
