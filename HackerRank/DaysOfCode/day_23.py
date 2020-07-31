"""
Problem Statement Found at: https://www.hackerrank.com/challenges/30-binary-trees/problem
"""


# In the challenge, this is part of a class, so self makes sense there.
def levelOrder(self, root):
    queue = [root]
    visited = []
    data = []

    while queue:
        node = queue.pop(0)

        if node not in visited and node is not None:
            data.append(str(node.data))
            visited.append(node)

            if node.left:
                queue.append(node.left)

            if root.right:
                queue.append(node.right)

    print(' '.join(data))
