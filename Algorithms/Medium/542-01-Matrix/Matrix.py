class Solution(object):
    def updateMatrix(self, matrix):
        if matrix == None or len(matrix) == 0:
            return matrix
        w = len(matrix[0])
        h = len(matrix)
        s = []
        for i in range(h):
            for j in range(w):
                if matrix[i][j] != 0:
                    s.append([i, j, 0])
                    while s:
                        a, b, dist = s.pop(0)
                        # if next element is 0, set the dist
                        if matrix[a][b] == 0:
                            matrix[i][j] = dist
                            s = []
                            break
                        # move to up, down, right, left
                        for x, y in [(0,1),(0,-1),(1,0),(-1,0)]:
                            xa = x+a
                            yb = y+b
                            # next element in correct area
                            if 0<=xa<h and 0<=yb<w:
                                s.append([xa, yb, dist+1])
        return matrix
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