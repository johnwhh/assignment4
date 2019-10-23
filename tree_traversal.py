class BinaryTree:
    """Binary tree to hold all tree nodes in"""
    class TreeNode:
        """Node class to represent nodes in binary tree"""
        __slots__ = '_value', '_left', '_right'

        def __init__(self, value):
            self._value = value
            self._left = None
            self._right = None

    def complete(self, incomplete):
        """Converts list of an incomplete tree to list of a complete tree"""
        i = 0
        while i < len(incomplete):
            if incomplete[i] is None:
                # for each None, insert left and right
                # None children if it will fit
                if i * 2 + 1 < len(incomplete):
                    incomplete.insert(i * 2 + 1, None)
                if i * 2 + 2 < len(incomplete):
                    incomplete.insert(i * 2 + 2, None)
            i += 1
        return incomplete

    def __init__(self, l):
        z = self.complete(l)  # Convert list to complete list
        self.root = self.create_nodes(z, 0, len(z) - 1)  # Build tree based on complete tree list

    def create_nodes(self, array, i, n):
        """Recursive method to fill tree with nodes"""
        if i > n or array[i] is None:
            return None
        node = self.TreeNode(array[i])  # create current node
        node._left = self.create_nodes(array, 2 * i + 1, n)  # create left node
        node._right = self.create_nodes(array, 2 * i + 2, n)  # create right node
        return node

    def preorder(self):
        """Traverses the tree using preorder traversal"""
        if self.root is None:
            print('Preorder:', None)
        else:
            print('Preorder:', self.traverse_preorder(self.root, '[')[:-2] + ']')

    def traverse_preorder(self, node, line):
        """Recursive helper method for preorder traversal"""
        if node is not None:
            line += str(node._value) + ', '
            if node._left is not None:
                line = self.traverse_preorder(node._left, line)
            if node._right is not None:
                line = self.traverse_preorder(node._right, line)
            return line

    def inorder(self):
        """Traverses the tree using inorder traversal"""
        if self.root is None:
            print('Inorder:', None)
        else:
            print('Inorder:', self.traverse_inorder(self.root, '[')[:-2] + ']')

    def traverse_inorder(self, node, line):
        """Recursive helper method for inorder traversal"""
        if node is not None:
            if node._left is not None:
                line = self.traverse_inorder(node._left, line)
            line += str(node._value) + ', '
            if node._right is not None:
                line = self.traverse_inorder(node._right, line)
            return line


def main():
    print('Example of a binary tree represented by list [1, None, 2, 3] traversed using preorder traversal:')
    example = [1, None, 2, 3]
    example_tree = BinaryTree(example)
    example_tree.preorder()
    print('Example of a binary tree represented by list [1, None, 2, 3] traversed using inorder traversal:')
    example_tree.inorder()
    while True:
        print()
        print('P. Preorder Traversal')
        print('I. Inorder Traversal')
        print('Q. Quit')
        choice = str(input())
        if choice.lower() == 'p' or choice.lower() == 'i':
            array = []  # empty array for user to fill up
            while True:
                num = input('Please input the next value of the list (S to stop): ')
                if str(num) == 's':
                    break  # break if q is entered
                if str(num) == 'None':
                    array.append(None)  # append None if None is entered
                    continue
                try:
                    array.append(int(num))  # append num if it's an int
                except ValueError:
                    print('Invalid input')
            tree = BinaryTree(array)
            if choice.lower() == 'p':
                tree.preorder()
            else:
                tree.inorder()
        elif choice.lower() == 'q':
            # break the loop and quit the program
            break
        else:
            # the provided input was not valid
            print("Invalid input")


if __name__ == '__main__':
    main()
