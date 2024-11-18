class Solution:
    # Function to rotate an array by d elements in counter-clockwise direction.
    def rotateArr(self, arr, d):
        n = len(arr)
        d = d % n  # Normalize d to handle cases where d > n
        
        # Split and concatenate
        arr[:] = arr[d:] + arr[:d]  # Modify the array in place
        
        return arr
