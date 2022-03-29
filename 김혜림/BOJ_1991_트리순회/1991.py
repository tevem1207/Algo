# 아스키 코드로 반환하기!
import sys
sys.stdin = open('input.txt')

def preorder(v):
    global preans, tree, ch1, ch2
    if v:
        preans += chr(tree[v]+64)
        preorder(ch1[tree[v]])
        preorder(ch2[tree[v]])



def inorder(v):
    global inans, tree, ch1, ch2
    if v:
        inorder(ch1[tree[v]])
        inans += chr(tree[v]+64)
        inorder(ch2[tree[v]])


def postorder(v):
    global postans, tree, ch1, ch2
    if v:
        postorder(ch1[tree[v]])
        postorder(ch2[tree[v]])
        postans += chr(tree[v] + 64)


N = int(input())
tree = [n for n in range(0, N+1)]
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)

lst = [list(input().split()) for _ in range(N)]
for l in lst:
    for idx in range(3):
        if l[idx] == '.':
            l[idx] = 0
            continue
        l[idx] = ord(l[idx]) - 64
    ch1[l[0]] = l[1]
    ch2[l[0]] = l[2]

preans = inans = postans = ''
preorder(1)
inorder(1)
postorder(1)
print(preans, inans, postans, sep="\n")