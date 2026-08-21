class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return all(self._no_dupes(g) for g in self._groups(board))

    @staticmethod
    def _no_dupes(group) -> bool:
        vals = [v for v in group if v != "."]
        return len(vals) == len(set(vals))

    @staticmethod
    def _groups(board):
        yield from board                              # rows
        yield from zip(*board)                        # columns
        for br in range(0, 9, 3):                     # boxes
            for bc in range(0, 9, 3):
                yield [board[br + dr][bc + dc]
                       for dr in range(3)
                       for dc in range(3)]