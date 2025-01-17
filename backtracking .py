class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = {}

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.getWords(board, word, i, j, visited):
                    return True
        
        return False

    def getWords(self, board, word, i, j, visited, pos = 0):
        if pos == len(word):
            return True

        if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited.get((i, j)) or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res

#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#Output: true

ob1 = Solution()
print("Leetcode's first case: ", ob1.exist(board
 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))

#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#Output: true

ob1 = Solution()
print("Leetcode's second case: ", ob1.exist(board
 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"))

#Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#Output: false

ob1 = Solution()
print("Leetcode's third case: ", ob1.exist(board
 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))