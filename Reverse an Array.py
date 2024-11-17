class Solution:
    def reverseArray(self, arr):
        # Initialize two pointers
        start = 0
        end = len(arr) - 1
        
        # Swap the elements until the pointers cross
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]  # Swap the elements
            start += 1  # Move the start pointer to the right
            end -= 1    # Move the end pointer to the left
        
        return arr

   
