class Solution {
    public int maxSubarrSum(int[] arr, int a, int b) {
        int n = arr.length;

        // compute prefix sum of the array
        for (int i = 1; i < n; i++) {
            arr[i] += arr[i - 1];
        }

        // to store the maximum sum found
        int maxi = arr[a - 1];

        // deque to maintain the minimum prefix in
        // the current window
        Deque<Integer> dq = new ArrayDeque<>();

        // insert initial prefix 0
        dq.addLast(0);

        // iterate from index 'a' to 'n - 1' (inclusive)
        for (int i = a; i < n; i++) {

            // remove prefix[i - b - 1] from deque if it's
            // outside the valid window
            if (i - b - 1 >= 0) {
                if (dq.peekFirst() == arr[i - b - 1]) {
                    dq.pollFirst();
                }
            }
            // special case: remove 0 if it falls outside the window
            else if (i - b == 0) {
                if (dq.peekFirst() == 0) {
                    dq.pollFirst();
                }
            }

            // maintain increasing order in deque (monotonic queue)
            while (!dq.isEmpty() && dq.peekLast() > arr[i - a]) {
                dq.pollLast();
            }

            // insert current prefix sum for future subarray starts
            dq.addLast(arr[i - a]);

            // compute maximum subarray sum ending at index i
            maxi = Math.max(maxi, arr[i] - dq.peekFirst());
        }

        return maxi;
    }
}
