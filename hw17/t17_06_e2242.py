def restore_tree_from_input(lines):
    class TreeNode:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None

    def insert_bst(root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = insert_bst(root.left, val)
        else:
            root.right = insert_bst(root.right, val)
        return root

    def postorder_insert(reversed_stack):
        root = None
        for letter in reversed_stack:
            root = insert_bst(root, letter)
        return root

    def preorder_traversal(node):
        if not node:
            return ''
        return node.val + preorder_traversal(node.left) + preorder_traversal(node.right)

    stack = []
    for line in lines:
        line = line.strip()
        if line == '*':
            break
        stack.extend(line)
    reversed_stack = stack[::-1]
    root = postorder_insert(reversed_stack)
    return preorder_traversal(root)


if __name__ == "__main__":
    import sys
    input_lines = sys.stdin.read().splitlines()
    result = restore_tree_from_input(input_lines)
    print(result)
