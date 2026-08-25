class Solution:
    def trap(self, height: List[int]) -> int:
        tot_fill = 0
        i = 0
        while i < len(height) - 1:          # fix 1
            left = height[i]
            if left == 0:
                i += 1
                continue

            j = i + 1
            wall = i + 1                    # tallest bar seen so far on the right
            found = False
            while j < len(height):
                if height[j] >= left:
                    found = True
                    break
                if height[j] > height[wall]:
                    wall = j
                j += 1

            if not found:
                j = wall                    # fix 2

            top = min(left, height[j])      # fix 3
            for k in range(i + 1, j):
                tot_fill += top - height[k]

            i = j
        return tot_fill