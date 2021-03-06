from sort import bubble_sort, selection_sort, insertion_sort, bucket_sort, counting_sort, merge_sort, tree_sort, quick_sort
import unittest


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        bubble_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        bubble_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        bubble_sort(numbers)
        assert numbers == []

        numbers = [-1]
        bubble_sort(numbers)
        assert numbers == [-1]

    def test_selection_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        selection_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        selection_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        selection_sort(numbers)
        assert numbers == []

        numbers = [-1]
        selection_sort(numbers)
        assert numbers == [-1]

    def test_insertion_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        insertion_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        insertion_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        insertion_sort(numbers)
        assert numbers == []

        numbers = [-1]
        insertion_sort(numbers)
        assert numbers == [-1]

    def test_bucket_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        numbers = bucket_sort(numbers, 5)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        numbers = bucket_sort(numbers, 5)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        numbers = bucket_sort(numbers, 5)
        assert numbers == []

        numbers = [-1]
        numbers = bucket_sort(numbers, 5)
        assert numbers == [-1]


    def test_counting_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        numbers = counting_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        numbers = counting_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        numbers = counting_sort(numbers)
        assert numbers == []

        numbers = [-1]
        numbers = counting_sort(numbers)
        assert numbers == [-1]

    def test_merge_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        numbers = merge_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        numbers = merge_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        numbers = merge_sort(numbers)
        assert numbers == []

        numbers = [-1]
        numbers = merge_sort(numbers)
        assert numbers == [-1]

    def test_tree_sort(self):
        numbers = [1, 20, 74, 35, 16, 100, 2]
        numbers = tree_sort(numbers)
        assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        numbers = tree_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        numbers = tree_sort(numbers)
        assert numbers == []

        numbers = [-1]
        numbers = tree_sort(numbers)
        assert numbers == [-1]

    def test_quick_sort(self):
        # numbers = [1, 20, 74, 35, 16, 100, 2]
        # quick_sort(numbers)
        # assert numbers == [1, 2, 16, 20, 35, 74, 100]

        numbers = [5, 4, 3, 2, 1, 0, -1]
        quick_sort(numbers)
        assert numbers == [-1, 0, 1, 2, 3, 4, 5]

        numbers = []
        quick_sort(numbers)
        assert numbers == []

        numbers = [-1]
        quick_sort(numbers)
        assert numbers == [-1]
