import sys
n = int(sys.stdin.readline().rstrip())
tree = {}
for _ in range(n):
    root, left, right = sys.stdin.readline().rstrip().split()
    tree[root] = [left, right]

def pre_traversal(root):
    if root != '.':
        print(root, end='')
        pre_traversal(tree[root][0])
        pre_traversal(tree[root][1])

def in_traversal(root):
    if root != '.':
        in_traversal(tree[root][0])
        print(root, end='')
        in_traversal(tree[root][1])

def post_traversal(root):
    if root != '.':
        post_traversal(tree[root][0])
        post_traversal(tree[root][1])
        print(root, end='')

pre_traversal('A')
print()
in_traversal('A')
print()
post_traversal('A')