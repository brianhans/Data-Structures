#!python

from linkedlist import LinkedList
from tree import BinaryTree

class KeyValuePair:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __eq__(self, other):
            return other == self.key

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.count = 0

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets

        Best case running time: Om(n) and
        Worst case running time: O(n) because we have to loop through all
        the elements."""
        total = 0

        for bucket in self.buckets:
            total += bucket.length()

        return total

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        try:
            self.get(key)
        except KeyError:
            return False

        return True


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError

        Best case running time: Om(1) if the bucket has only one or less elements
        Worst case running time: O(n) if all the elements are in one bucket."""

        index = self._bucket_index(key)
        item = self.buckets[index].find(lambda item: item == key)

        if(item):
            return item.value

        raise KeyError


    def set(self, key, value):
        """Insert or update the given key with its associated value

        Best case running time: Om(1) if the bucket is empty
        Worst case running time: O(n^2) if the bucket has many elements in it."""

        index = self._bucket_index(key)

        bucket_item = self.buckets[index].find(lambda item: item == key)

        if(bucket_item):
            bucket_item.value = value
        else:
            self.buckets[index].append(KeyValuePair(key, value))
            self.count += 1
            if self.count > len(self.buckets) * (2.0/3.0):
                self.expand()

    def update_value(self, key, function):
        index = self._bucket_index(key)

        bucket_item = self.buckets[index].find(lambda item: item == key)

        if(bucket_item):
            bucket_item.value = function(bucket_item.value)
        else:
            raise KeyError


    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError

        Best case running time: Om(1) if the bucket is empty
        Worst case running time: O(n) if the bucket has all the elements in it."""

        if not self.get(key):
            raise KeyError

        index = self._bucket_index(key)
        self.buckets[index].delete(key)
        self.count -= 1

    def keys(self):
        """Return a list of all keys in this hash table

        Best case running time: Om(n) and
        Worst case running time: O(b+n) because it has to got through all the elements."""
        keys = []

        for bucket in self.buckets:
            bucket_keys = map(lambda x: x.key, bucket.as_list())
            keys.extend(bucket_keys)

        return keys

    def values(self):
        """Return a list of all values in this hash table

        Best case running time: Om(n) and
        Worst case running time: O(b+n) bceause it has to got through all the elements."""
        values = []

        for bucket in self.buckets:
            bucket_values = map(lambda x: x.value, bucket.as_list())
            values.extend(bucket_values)

        return values

    def clear(self):
        """Remove all items from the dictionary.

        Best case running time: Om(n) and
        Worst case running time: O(n) because it has to got through all the buckets."""
        self.buckets = [LinkedList() for i in range(len(self.buckets))]

    def expand(self):
        old_buckets = self.buckets
        self.buckets = [LinkedList() for i in range(len(self.buckets) * 2)]

        for bucket in self.buckets:
            for item in bucket:
                self.set(item.key, item.value)


    def iteritems(self):
        for bucket in self.buckets:
            for item in bucket:
                yield (item.key, item.value)

    def __iter__(self):
        for bucket in self.buckets:
            for value in bucket.as_list():
                yield value.value


class BinaryHashTable(object):

    def __init__(self):
        self.tree = BinaryTree()

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def length(self):
        return self.tree.length()

    def contains(self, key):
        try:
            self.tree.search(hash(key))
            return True
        except KeyError:
            return False

    def get(self, key):
        return self.tree.search(hash(key))

    def set(self, key, value):
        self.tree.insert(hash(key), value)

    def delete(self, key):
        self.tree.delete(hash(key))

    def clear(self):
        self.tree.root = None

    def keys(self):
        return [x.key for x in self.tree]

    def values(self):
        return [x.value for x in self.tree]



def create_hashtable(amount):
    hash_table = HashTable()

    for i in range(0, amount):
        hash_table.set('test' + str(i), 'none')
    return hash_table


if __name__ == '__main__':
    create_hashtable(100)
