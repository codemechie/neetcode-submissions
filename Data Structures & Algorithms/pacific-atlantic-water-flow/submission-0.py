class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        rows, cols = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()

        def dfs(r, c, visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,visited)

        for r in range(rows):
            dfs(r, 0, pacific_visited)
        for c in range(cols):
            dfs(0, c, pacific_visited)

        for r in range(rows):
            dfs(r, cols-1, atlantic_visited)
        for c in range(cols):
            dfs(rows-1, c, atlantic_visited)
        return [[r,c] for r, c in pacific_visited & atlantic_visited] 





