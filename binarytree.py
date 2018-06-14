class Node:

    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

    def add(self, info):
        if self.info > info:
            if self.left is None:
                self.left = Node(info)
            else:
                self.left.add(info)
        elif self.info < info:
            if self.right is None:
                self.right = Node(info)
            else:
                self.right.add(info)
        else:
            raise ValueError('Cannot insert duplicate value: ' + str(info))