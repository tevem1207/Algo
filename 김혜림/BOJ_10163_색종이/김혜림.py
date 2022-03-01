import sys
sys.stdin = open('input1.txt')


def get_surface_area(points):
    ans = [0]*T
    
    for idx, point in enumerate(points):
        for i in range(point[0], point[0]+point[2]):
            for j in range(point[1], point[1]+point[3]):
                matrix[i][j] = idx+1
    
    for m in range(1001):
        for n in range(1001):
            if matrix[m][n]:
                x = matrix[m][n]
                ans[x-1] += 1
    return ans
    
    
T = int(input())
points = [list(map(int, input().split())) for _ in range(T)]
matrix = [[0]*1001 for _ in range(1001)]

results = get_surface_area(points)
for result in results:
    print(result)