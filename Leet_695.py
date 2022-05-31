class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count_dict = {}
        count = 1
        self.max_num = 1
        Output = 0
        
        def change(i,j,count):
            grid[i][j] = count
            if i > 0:
                if grid[i-1][j] != 0:
                    if grid[i-1][j] != grid[i][j]:
                        grid[i-1][j] = count
                        self.max_num += 1
                        change(i-1,j,count)
            if j > 0:
                if grid[i][j-1] != 0:
                    if grid[i][j-1] != grid[i][j]:
                        grid[i][j-1] = count
                        self.max_num += 1
                        change(i,j-1,count)
            if i < h - 1:
                if grid[i+1][j] != 0:
                    if grid[i+1][j] != grid[i][j]:
                        grid[i+1][j] = count
                        self.max_num += 1
                        change(i+1,j,count)
            if j < w - 1:
                if grid[i][j+1] != 0:
                    if grid[i][j+1] != grid[i][j]:
                        grid[i][j+1] = count
                        self.max_num += 1
                        change(i,j+1,count)
                    
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    change(i,j,count)
                    count += 1
                    Output = max(self.max_num,Output)
                    self.max_num = 1
            
        return Output


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        count_dict = {}
        count = 1
        
        def change(i,j,count):
            grid[i][j] = count
            if i > 0:
                if grid[i-1][j] != 0:
                    if grid[i-1][j] != grid[i][j]:
                        grid[i-1][j] = count
                        change(i-1,j,count)
            if j > 0:
                if grid[i][j-1] != 0:
                    if grid[i][j-1] != grid[i][j]:
                        grid[i][j-1] = count
                        change(i,j-1,count)
            if i < h - 1:
                if grid[i+1][j] != 0:
                    if grid[i+1][j] != grid[i][j]:
                        grid[i+1][j] = count
                        change(i+1,j,count)
            if j < w - 1:
                if grid[i][j+1] != 0:
                    if grid[i][j+1] != grid[i][j]:
                        grid[i][j+1] = count
                        change(i,j+1,count)
                    
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    change(i,j,count)
                    count += 1

        for i in range(h):
            for j in range(w):
                if grid[i][j] != 0:            
                    if grid[i][j] in count_dict.keys():
                        count_dict[grid[i][j]] += 1
                    else:
                        count_dict[grid[i][j]] = 1
        
        if count_dict:
            return max(count_dict.values())
        else:
            return 0
                    count += 1
                    Output = max(self.max_num,Output)
                    self.max_num = 1
            
        return Output
