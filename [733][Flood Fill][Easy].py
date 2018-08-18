# https://leetcode.com/problems/flood-fill

class Solution:
    def dfs(self, i, j):
        if (0 <= i < self.row) and (0 <= j < self.row):
            if self.image[i][j] == self.old_color:
                self.image[i][j] = -1
                self.dfs(i - 1, j)
                self.dfs(i + 1, j)
                self.dfs(i, j - 1)
                self.dfs(i, j + 1)

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        self.row, self.col = len(image), len(image[0])
        self.old_color = image[sr][sc]
        self.dfs(sr, sc)
        for i in range(self.row):
            for j in range(self.col):
                if self.image[i][j]==-1:
                    self.image[i][j]=newColor
        return self.image
