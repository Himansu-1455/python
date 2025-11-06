class Solution:

    def numberOfWays(self, n):
        # Base cases
        if n == 0 or n == 1:
            return 1

        prev2 = 1
        prev1 = 1

        # Iterate from 2 to n to build the result
        for i in range(2, n + 1):

            # Current state depends on the sum of previous two states
            curr = prev1 + prev2

            # Move the variables one step ahead
            prev2 = prev1
            prev1 = curr

        return prev1
