class Node(object):
    def __init__(self, key, data):
        """Initialize this node with the given data"""
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node(data: {},left:{},right:{})'.format(repr(self.data), repr(self.left), repr(self.right))


class BinaryTree(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any"""
        self.root = None
        self.node_count = 0
        if iterable:
            for key, value in iterable:
                self.insert(key, value)

    def insert(self, key, value, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key, value)
        else:
            if key < node.key:
                #Go left
                if node.left:
                    self.insert(key, node.left)
                else:
                    node.left = Node(key, value)
                    self.node_count += 1
            elif key > node.key:
                #Go right
                if node.right:
                    self.insert(key, node.right)
                else:
                    node.right = Node(key, value)
                    self.node_count += 1
            else:
                raise KeyError

    def delete(self, key, node=None):
        if node is None:
            node = self.root
            if self.root is None:
                #Tree is empty
                raise KeyError

        if key < node.key:
            #Go left
            if node.left:
                if node.left.key is key:
                    #Remove node.left if it is the item
                    self.node_count -= 1
                    #Find the right most item in the left
                    if node.left.left:
                        temp_right = node.left.right
                        node.left, _ = self.rightMostNodeOf(node.left.left)
                        node.left.right = temp_right
                    else:
                        #If there is no item in the left use the right item
                        node.left = node.left.right
                else:
                    #Move to the lower node
                    self.delete(key, node.left)
            else:
                raise KeyError
        elif key > node.key:
            #If item is greater than the value of current item go right
            if node.right:
                if node.right.key is key:
                    #Remove node.right if it is the item
                    self.node_count -= 1
                    #Find the right most item in the left
                    if node.right.left:
                        temp_right = node.right.right
                        node.right, _ = self.rightMostNodeOf(node.right.left)
                        node.right.right = temp_right
                    else:
                        #If there is no item in the left use the right item
                        node.right = node.right.right
                else:
                    #Move to the higher node
                    self.delete(key, node.right)
            else:
                raise KeyError
        else:
            #This means the root is the item being deleted
            temp_left = self.root.left
            temp_right = self.root.right

            if self.root.left:
                self.root, parent = self.rightMostNodeOf(self.root.left)
                parent.right = None
            else:
                self.root, parent = self.leftMostNodeOf(self.root.right)
                parent.left = None

            self.root.left = temp_left
            self.root.right = temp_right
            self.node_count -= 1


    def rightMostNodeOf(self, node):
        parent = node
        replacement_node = node
        while replacement_node.right is not None:
            parent = replacement_node
            replacement_node = replacement_node.right

        return replacement_node, parent

    def leftMostNodeOf(self, node):
        parent = node
        replacement_node = node
        while replacement_node.left is not None:
            parent = replacement_node
            replacement_node = replacement_node.left

        return replacement_node, parent

    def search(self, key, node=None):
        if node is None:
            node = self.root

        if node.key is key:
            return node.value

        if key < node.key:
            if node.left:
                return self.search(key, node.left)
            else:
                raise KeyError
        else:
            if node.right:
                return self.search(key, node.right)
            else:
                raise KeyError

    def length(self):
        return self.node_count

    def in_order_traverse(self, node=None):
        if node is None:
            node = self.root

        items = []

        if node.left:
            items.extend(self.in_order_traverse(node.left))

        items.append(node.value)

        if node.right:
            items.extend(self.in_order_traverse(node.right))

        return items

    def post_order_traverse(self, node=None):
        if node is None:
            node = self.root

        items = []

        if node.left:
            items.extend(self.post_order_traverse(node.left))
        if node.right:
            items.extend(self.post_order_traverse(node.right))

        items.append(node.value)

        return items


    def pre_order_traverse(self, node=None):
        if node is None:
            node = self.root

        items = []

        items.append(node.value)

        if node.left:
            items.extend(self.pre_order_traverse(node.left))
        if node.right:
            items.extend(self.pre_order_traverse(node.right))

        return items

    def __iter__(self):
        



    def __repr__(self):
        """Return a string representation of this node"""
        return 'BinaryTree({})'.format(repr(self.root))

# if __name__ == '__main__':
