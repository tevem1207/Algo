import sys
sys.stdin = open('input.txt')


import sys
sys.setrecursionlimit(10 ** 6)


def get_pre(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return
    center = index_order[int(postorder[post_e])]
    print(postorder[post_e], end=' ')

    # left node
    if center > in_s:
        get_pre(in_s, center-1, post_s, post_s-in_s+center-1)

    # right node
    if center < in_e:
        get_pre(center+1, in_e, post_s-in_s+center, post_e-1)


n = int(input())
inorder = input().split()
index_order = ['' for _ in range(n+1)]
for i in range(n):
    index_order[int(inorder[i])] = i

postorder = input().split()

get_pre(0, n-1, 0, n-1)
