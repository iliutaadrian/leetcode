class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        cols = {}
        rows = {}
        boxes = {}
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != ".":
                    if (
                        element in rows.get(i, set())
                        or element in cols.get(j, set())
                        or element in boxes.get((i // 3, j // 3), set())
                    ):
                        return False

                    if i not in rows:
                        rows[i] = set()
                    if j not in cols:
                        cols[j] = set()
                    if (i // 3, j // 3) not in boxes:
                        boxes[(i // 3, j // 3)] = set()
                    rows[i].add(element)
                    cols[j].add(element)
                    boxes[(i // 3, j // 3)].add(element)

        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(Solution().isValidSudoku(board))

