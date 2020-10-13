import unittest
import array as r
import fun_with_collections.sort_and_search_array as basic_list_exception


class MyTestCase(unittest.TestCase):
    def test_search_array(self):
        self.assertFalse(basic_list_exception.search_array([5, -1, 3, 6, 8, 9, 4, 10], -1))


def test_sort_array(self):
    n = r.array([9, 3, 1, 5, 8, 6, 4, 7])
    to_list = n.tolist()
    _list = to_list.sort()
    to_list = r.array(to_list)

    self.assertTrue(basic_list_exception.sort_array(([9.0, 3.0, 1.0, 5.0, 8.0, 6.0, 4.0, 7.0])))
    """" I tried my bet, but I could not figure out the sort test"""


if __name__ == '__main__':
    unittest.main()
