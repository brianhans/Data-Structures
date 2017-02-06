class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this node"""
        return '\nNode(data: {},left:{},right:{})'.format(repr(self.data), repr(self.left), repr(self.right))


class BinaryTree(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any"""
        self.root = None
        self.node_count = 0
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, item, node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(item)
        else:
            if item < node.data:
                #Go left
                if node.left:
                    self.insert(item, node.left)
                else:
                    node.left = Node(item)
            elif item > node.data:
                #Go right
                if node.right:
                    self.insert(item, node.right)
                else:
                    node.right = Node(item)
            else:
                raise KeyError

    def delete(self, item, node=None):
        if node is None:
            node = self.root
            if self.root is None:
                #Tree is empty
                raise KeyError

        if item < node.data:
            #Go left
            if node.left:
                if node.left.data is item:
                    #Remove node.left if it is the item

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
                    self.delete(item, node.left)
            else:
                raise KeyError
        elif item > node.data:
            #If item is greater than the value of current item go right
            if node.right:
                if node.right.data is item:
                    #Remove node.right if it is the item

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
                    self.delete(item, node.right)
            else:
                raise KeyError
        else:
            print('root delete')
            #This means the root is the item being deleted
            temp_left = self.root.left
            temp_right = self.root.right

            if self.root.left:
                self.root, parent = self.rightMostNodeOf(self.root.left)
                parent.right = None
            else:
                self.root = self.root.right

            self.root.left = temp_left
            self.root.right = temp_right


    def rightMostNodeOf(self, node):
        parent = node
        replacement_node = node
        while replacement_node.right is not None:
            parent = replacement_node
            replacement_node = replacement_node.right

        return replacement_node, parent

    def search(self, item, node=-1):
        if node is -1:
            node = self.root

        if node is None or node.data is item:
            return node

        if item < node.data:
            return self.search(item, node.left)
        else:
            return self.search(item, node.right)

    def __repr__(self):
        """Return a string representation of this node"""
        return 'BinaryTree({})'.format(repr(self.root))

# if __name__ == '__main__':
