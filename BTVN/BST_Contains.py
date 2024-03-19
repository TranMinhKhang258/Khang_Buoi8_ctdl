class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def contains(self, value):
        temp = self.root
        while temp:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False


