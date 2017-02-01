#!python
from linkedlist import LinkedList

class Stack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any"""
        self.linked_list = LinkedList()
        if iterable:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack"""
        return 'Stack({})'.format(self.length())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise"""
        return self.linked_list.length() == 0

    def length(self):
        """Return the number of items in this stack"""
        return self.linked_list.length()

    def peek(self):
        """Return the top item on this stack without removing it,
        or None if this stack is empty"""
        if self.is_empty():
            return None
            
        return self.linked_list.head.data

    def push(self, item):
        """Push the given item onto this stack"""
        self.linked_list.prepend(item)
        pass

    def pop(self):
        """Return the top item and remove it from this stack,
        or raise ValueError if this stack is empty"""
        if self.is_empty():
            raise ValueError

        item = self.linked_list.head
        self.linked_list.head = item.next

        if item.next:
            item.next = None

        self.linked_list.node_count -= 1

        return item.data
