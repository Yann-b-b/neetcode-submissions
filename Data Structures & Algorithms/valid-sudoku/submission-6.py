from math import isqrt
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        return all(self._no_dupes(g) for g in self._groups(board))

    @staticmethod
    def _no_dupes(group) -> bool:
        vals = [v for v in group if v != "."]
        return len(vals) == len(set(vals))

    @staticmethod
    def _groups(board):
        length = len(board)
        k = isqrt(length)
        if k * k != length:
            raise ValueError(f"board size {n} is not a perfect square")
        yield from board                              # rows
        yield from zip(*board)                        # columns
        for br in range(0, length, k):                     # boxes
            for bc in range(0, length, k):
                yield [board[br + dr][bc + dc]
                       for dr in range(3)
                       for dc in range(3)]