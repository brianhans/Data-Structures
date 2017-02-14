class Node(object):
    __init__(data):
        self.items = []
        self.data = [data]
        self.depth = 0

    def get_left():
        if len(items) == 0:
            return None
        else:
            return item[0]

    def get_left_data():
        if len(items) == 0:
            return None
        else:
            return data[0]

    def get_middle():
        if len(items) < 2:
            return None
        else:
            return item[1]

    def get_right():
        if len(items) < 2:
            return None
        else:
            return items[len(items) - 1]

    def get_right_data():
        if len(items) < 2:
            return None
        else:
            return data[len(items) - 1]

    def insert(self, item):
        data.append(item)
        data.sort()

        if len(data) > 2:
            left_item = data[0]
            right_item = data[2]

            items = [left_item, right_item]



class twoThreeTree(object):

    __init__(iterable):
        self.root = None
        self.max_depth = 0

        for item in iterable:
            self.insert(item)

    def insert(self, item, node=None):
        if root is None:
            self.root = Node(item)
            return

        if node is None:
            node = self.root

        if node.depth == self.max_depth:
            node.insert(item)
        else:
            
            self.insert(item, )

    def findChildNode(self, node, item):
        if item < node.get_left_data():
            return node.get_left()
        elif item > node.get_right_data();
            return node.get_right()
        else:
            return node.get_middle()
