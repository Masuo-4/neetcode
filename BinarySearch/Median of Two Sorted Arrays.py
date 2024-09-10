class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # A < B にしたい。
        if len(A) > len(B):
            A, B = B, A
        
        total = len(nums1) + len(nums2)
        half = total // 2
        l, r = 0, len(A) - 1
        
        while True:
            A_m = l + (r - l) // 2
            B_m = half - A_m - 2
            A_left = A[A_m] if A_m >= 0 else float("-infinity")
            A_right = A[A_m + 1] if (A_m + 1) < len(A) else float("infinity")
            B_left = B[B_m] if B_m >= 0 else float("-infinity")
            B_right = B[B_m + 1] if (B_m + 1) < len(B) else float("infinity")
            if A_left > B_right:
                r = A_m - 1
            elif B_left > A_right:
                l = A_m + 1
            
            else:
                if total % 2:
                    return min(B_right, A_right) 
                else:
                    return float((max(A_left, B_left) + min(B_right, A_right))) / 2
                        