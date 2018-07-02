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
    
    def in_order(self):
        infos = []
        Node._in_order(self, infos)
        return infos

    @staticmethod
    def _in_order(node, infos):
        if node.left is not None:
            Node._in_order(node.left, infos)
        infos.append(node.info)
        if node.right is not None:
            Node._in_order(node.right, infos)

    def max_height(self):
        if self.left is None and self.right is None:
            return 1
        l = 0
        r = 0
        if self.left is not None:
            l = self.left.max_height()
        if self.right is not None:
            r = self.right.max_height()
        
        if l > r:
            return l+1
        return r+1

    def min_height(self):
        if self.left is None and self.right is None:
            return 1
        l = 0
        r = 0
        if self.left is not None:
            l = self.left.min_height()
        if self.right is not None:
            r = self.right.min_height()
        
        if l < r:
            return l+1
        return r+1


        
