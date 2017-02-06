from hashtable import HashTable

class Set(HashTable):

    def set(self, item):
        super(Set, self).set(item, True)
        return self

    def unset(self, item):
        super(Set, self).delete(item)
        return self

if __name__ == '__main__':
    new_set = Set()
    new_set.set('test')
    new_set.set('test')
    new_set.set('test1')
    print(new_set.length())
    new_set.unset('test')
    print(new_set.length())
