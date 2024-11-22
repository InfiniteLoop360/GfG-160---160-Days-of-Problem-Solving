class Solution:
    def getMinDiff(self, arr, k):
        n = len(arr)
        if n == 1:
            return 0  # If there's only one element, the difference is 0

        # Sort the array
        arr.sort()

        # Initial difference between max and min elements
        ans = arr[-1] - arr[0]

        # Loop to evaluate each possible boundary
        for i in range(n - 1):
            # Current maximum element after modifications
            max_elem = max(arr[i] + k, arr[-1] - k)
            # Current minimum element after modifications
            min_elem = min(arr[0] + k, arr[i + 1] - k)
            
            # Update the answer
            if min_elem >= 0:  # Ensure no negative heights
                ans = min(ans, max_elem - min_elem)

        return ans
