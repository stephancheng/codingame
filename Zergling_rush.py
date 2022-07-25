#Zergling rush

import sys
import math
import numpy as np
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


w, h = [int(i) for i in input().split()]
MAP = []
for i in range(h):
    row = list(input())
    MAP.append(row)
    #row = input()

MAP = np.array(MAP)

class Starmap():
    def __init__(self, w, h, MAP):
        self.w = w
        self.h = h
        self.MAP = MAP
        self.search_matrix = np.zeros((h, w), dtype=int)
        self.open_matrix = np.zeros((h, w), dtype=int)

    def search(self, cor_x, cor_y):
        if self.search_matrix[cor_x, cor_y] == 1:
            return 0
        else:
            #print(cor_x, cor_y)
            self.search_matrix[cor_x, cor_y] = 1
            if self.MAP[cor_x, cor_y] == '.':
                self.open_matrix[cor_x, cor_y] = 1
                # left
                if (cor_y - 1) >= 0:
                    #print("left")
                    self.search(cor_x , cor_y - 1)
                # right
                if (cor_y + 1) <= (self.w - 1):
                    #print("right")
                    self.search(cor_x, cor_y +1)
                # up
                if (cor_x - 1) >= 0:
                    #print("up")
                    self.search(cor_x - 1, cor_y)
                # bottom
                if (cor_x + 1) <= (self.h -1):
                    #print("bo")
                    self.search(cor_x + 1, cor_y)
            return 0

starmap = Starmap(w, h, MAP)
for i in range(h):
    for j in range(w):
        if (i == 0) or (i == h-1) or (j == 0) or (j == w-1):
            starmap.search(i,j)

result = np.where(MAP == 'B')
List_cor_B= list(zip(result[0], result[1]))

for (x,y) in List_cor_B:
    low_x = max(0, x -1)
    up_x = min(x+1, h-1)
    low_y = max(0, y-1)
    up_y = min(y+1, w-1)
    for i in range(low_x, up_x+1):
        for j in range(low_y, up_y+1):
            if starmap.open_matrix[i,j] == 1:
                MAP[i, j] = 'z'
#print(starmap.open_matrix)
#print(MAP)
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
for row in MAP:
    rslt = "".join(row)
    print(rslt)
