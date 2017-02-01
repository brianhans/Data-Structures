#!python
from linkedlist import LinkedList

class Queue(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any"""
        self.linked_list = LinkedList()
        if iterable:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue"""
        return 'Queue({})'.format(self.length())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise"""
        return self.linked_list.length() == 0

    def length(self):
        """Return the number of items in this queue"""
        return self.linked_list.length()

    def peek(self):
        """Return the next item in this queue without removing it,
        or None if this queue is empty"""
        if self.is_empty():
            return None

        return self.linked_list.head.data

    def enqueue(self, item):
        """Enqueue the given item into this queue

        Runtime: O(1)
        """
        self.linked_list.append(item)


    def dequeue(self):
        """Return the next item and remove it from this queue,
        or raise ValueError if this queue is empty"""
        if self.is_empty():
            raise ValueError

        item = self.linked_list.head
        self.linked_list.head = item.next

        item.next = None

        self.linked_list.node_count -= 1

        return item.data
