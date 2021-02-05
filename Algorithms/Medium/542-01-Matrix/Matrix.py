import numpy as np
from collections import deque
matrix = [[0,0,0],[0,1,0],[0,0,0]]
w = len(matrix[0])
h = len(matrix)
s = deque()
limit = w*2
for i in range(h):
    for j in range(w):
        if matrix[i][j] != 0:
            dist = 0
            s.append((i, j))
            while s:
                (a, b) = s.popleft()
                if matrix[a][b] == 0:
                    matrix[i][j] = dist
                    
                for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    xa = x+a
                    yb = y+b
                    if 0<=xa<h and 0<=yb<w:
                        s.append((xa, yb))
                        dist += 1
print(matrix)
# w = len(matrix[0])
# h = len(matrix)
# limit = w*2
# m = np.matrix(matrix)
# m =  m.flatten()
# zero_queue = deque()
# for i in range(h):
#     for j in range(w):
#         if matrix[i][j] == 0:
#             zero_queue.append((i,j))
# for i in range(h):
#     for j in range(w):
#         dist = limit
#         if matrix[i][j] != 0:
#             for z in zero_queue:
#                 if (abs(z[0]-i) + abs(z[1]-j)) < dist:
#                     dist = abs(z[0]-i) + abs(z[1]-j)
#             matrix[i][j] = dist
# print(matrix)