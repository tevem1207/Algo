import sys
sys.stdin = open('input.txt')


def preorder(n):
    print(n, end='')

    if tree[n][0] != '.':
        preorder(tree[n][0])

    if tree[n][1] != '.':
        preorder(tree[n][1])


def inorder(n):
    if tree[n][0] != '.':
        inorder(tree[n][0])

    print(n, end='')

    if tree[n][1] != '.':
        inorder(tree[n][1])


def postorder(n):
    if tree[n][0] != '.':
        postorder(tree[n][0])

    if tree[n][1] != '.':
        postorder(tree[n][1])

    print(n, end='')


N = int(input())
tree = {}

for i in range(N):
    m, l, r = input().split()
    tree[m] = [l, r]

root_node = 'A'

preorder(root_node)
print()
inorder(root_node)
print()
postorder(root_node)
