import queue

def can_reach_dest(grid, max_time):
    n = len(grid)
    m = len(grid[0])
    visited = [[False]*m for i in range(n)]
    drow = [-1, 0, 1, 0]
    dcol = [0, 1, 0, -1]
    q = queue.Queue()
    q.put([0, 0, 0])
    visited[0][0] = True

    while not q.empty():
        node = q.get()
        row = node[0][0]
        col = node[0][1]
        time = node[0][2]

        if row == n-1 and col == m-1:
            return time <= max_time

        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and grid[nrow][ncol] == '.' and visited[nrow][ncol] == False:
                visited[nrow][ncol] = True
                q.put([nrow, ncol, time+1])
    return False
    