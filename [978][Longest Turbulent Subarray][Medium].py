class Solution:
    def maxTurbulenceSize(self, A) -> int:
        len_A = len(A)
        B = [1] * len_A
        # 1代表本次降序，2代表升序，3表示上次从头开始，这次都行
        tag = 3
        for i in range(1, len(A)):
            if tag == 3:
                if A[i] > A[i - 1]:
                    tag = 1
                    B[i] = B[i - 1] + 1
                elif A[i] < A[i - 1]:
                    tag = 2
                    B[i] = B[i - 1] + 1
                elif A[i] == A[i - 1]:
                    tag = 3
            elif tag == 1:
                if A[i] > A[i - 1]:
                    B[i] = 2
                    tag = 1
                elif A[i] < A[i - 1]:
                    tag = 2
                    B[i] = B[i - 1] + 1
                elif A[i] == A[i - 1]:
                    tag = 3
            elif tag == 2:
                if A[i] > A[i - 1]:
                    tag = 1
                    B[i] = B[i - 1] + 1
                elif A[i] < A[i - 1]:
                    B[i] = 2
                    tag = 2
                elif A[i] == A[i - 1]:
                    tag = 3
        return max(B)


