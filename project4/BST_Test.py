import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

    def setUp(self):
        self.__bst = Binary_Search_Tree()

    def test_empty_bst(self):
        self.assertEqual('[ ]', str(self.__bst))
        self.assertEqual('[ ]', self.__bst.in_order())

    def test_empty_height(self):
        self.assertEqual(0, self.__bst.get_height())

    def test_insert_one(self):
        self.__bst.insert_element(34)
        self.assertEqual('[ 34 ]', str(self.__bst))
        self.assertEqual('[ 34 ]', self.__bst.in_order())
        self.assertEqual('[ 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 34 ]', self.__bst.post_order())

    def test_insert_one_height(self):
        self.__bst.insert_element(34)
        self.assertEqual(1, self.__bst.get_height())

    def test_insert_left_of_root(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(8)
        self.assertEqual('[ 8, 34 ]', str(self.__bst))
        self.assertEqual('[ 8, 34 ]', self.__bst.in_order())
        self.assertEqual('[ 34, 8 ]', self.__bst.pre_order())
        self.assertEqual('[ 8, 34 ]', self.__bst.post_order())

    def test_insert_left_of_root_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(8)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_right_of_root(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(47)
        self.assertEqual('[ 34, 47 ]', str(self.__bst))
        self.assertEqual('[ 34, 47 ]', self.__bst.in_order())
        self.assertEqual('[ 34, 47 ]', self.__bst.pre_order())
        self.assertEqual('[ 47, 34 ]', self.__bst.post_order())

    def test_insert_right_of_root_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(47)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_balanced(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        self.assertEqual('[ -2, 14, 29, 34, 36, 97, 157 ]', str(self.__bst))
        self.assertEqual('[ 34, 14, -2, 29, 97, 36, 157 ]', self.__bst.pre_order())
        self.assertEqual('[ -2, 29, 14, 36, 157, 97, 34 ]', self.__bst.post_order())

    def test_insert_balanced_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_all_less_than_root(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(0)
        self.__bst.insert_element(-27)
        self.assertEqual('[ -27, 0, 3, 5, 14, 34 ]', str(self.__bst))
        self.assertEqual('[ 34, 14, 3, 0, -27, 5 ]', self.__bst.pre_order())
        self.assertEqual('[ -27, 0, 5, 3, 14, 34 ]', self.__bst.post_order())

    def test_insert_all_less_than_root_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(0)
        self.__bst.insert_element(-27)
        self.assertEqual(5, self.__bst.get_height())

    def test_insert_all_greater_than_root(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.assertEqual('[ 34, 85, 92, 97, 102, 500 ]', str(self.__bst))
        self.assertEqual('[ 34, 97, 85, 92, 102, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ 92, 85, 500, 102, 97, 34 ]', self.__bst.post_order())


    def test_insert_all_greater_than_root_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.assertEqual(4, self.__bst.get_height())

    def test_insert_same_with_one(self):
        self.__bst.insert_element(34)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(34)
        self.assertEqual('[ 34 ]', str(self.__bst))
        self.assertEqual('[ 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 34 ]', self.__bst.post_order())
    
    def test_insert_same_with_one_height(self):
        self.__bst.insert_element(34)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(34)
        self.assertEqual(1, self.__bst.get_height())

    def test_insert_same_with_two(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(97)
        self.assertEqual('[ 34, 97 ]', str(self.__bst))
        self.assertEqual('[ 34, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 97, 34 ]', self.__bst.post_order())

    def test_insert_same_with_two_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(97)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_same_at_top(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(14)
        self.assertEqual('[ -2, 14, 29, 34, 36, 97, 157 ]', str(self.__bst))
        self.assertEqual('[ 34, 14, -2, 29, 97, 36, 157 ]', self.__bst.pre_order())
        self.assertEqual('[ -2, 29, 14, 36, 157, 97, 34 ]', self.__bst.post_order())

    def test_insert_same_at_top_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(14)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_same_at_bottom(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(-2)
        self.assertEqual('[ -2, 14, 29, 34, 36, 97, 157 ]', str(self.__bst))
        self.assertEqual('[ 34, 14, -2, 29, 97, 36, 157 ]', self.__bst.pre_order())
        self.assertEqual('[ -2, 29, 14, 36, 157, 97, 34 ]', self.__bst.post_order())

    def test_insert_same_at_bottom_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(-2)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_root_leaving_zero(self):
        self.__bst.insert_element(34)
        self.__bst.remove_element(34)
        self.assertEqual('[ ]', str(self.__bst))
        self.assertEqual('[ ]', self.__bst.pre_order())
        self.assertEqual('[ ]', self.__bst.post_order())

    def test_remove_root_leaving_zero_height(self):
        self.__bst.insert_element(34)
        self.__bst.remove_element(34)
        self.assertEqual(0, self.__bst.get_height())
    
    def test_remove_root_with_one_child(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.remove_element(34)
        self.assertEqual('[ 97 ]', str(self.__bst))
        self.assertEqual('[ 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 97 ]', self.__bst.post_order())

    def test_remove_root_with_one_child_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.remove_element(34)
        self.assertEqual(1, self.__bst.get_height())

    def test_remove_root_with_two_children(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.remove_element(34)
        self.assertEqual('[ 14, 97 ]', str(self.__bst))
        self.assertEqual('[ 97, 14 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 97 ]', self.__bst.post_order())

    def test_remove_root_with_two_children_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.remove_element(34)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_leaf(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.__bst.remove_element(500)
        self.assertEqual('[ 34, 85, 92, 97, 102 ]', str(self.__bst))
        self.assertEqual('[ 34, 97, 85, 92, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 92, 85, 102, 97, 34 ]', self.__bst.post_order())

    def test_remove_leaf_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.__bst.remove_element(500)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_middle_with_one_child(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.__bst.remove_element(85)
        self.assertEqual('[ 34, 92, 97, 102, 500 ]', str(self.__bst))
        self.assertEqual('[ 34, 97, 92, 102, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ 92, 500, 102, 97, 34 ]', self.__bst.post_order())

    def test_remove_middle_with_one_child_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(92)
        self.__bst.remove_element(85)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_middle_with_two_children(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(100)
        self.__bst.insert_element(92)
        self.__bst.remove_element(97)
        self.assertEqual('[ 34, 85, 92, 100, 102 ]', str(self.__bst))
        self.assertEqual('[ 34, 100, 85, 92, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 92, 85, 102, 100, 34 ]', self.__bst.post_order())

    def test_remove_middle_with_two_children_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(85)
        self.__bst.insert_element(102)
        self.__bst.insert_element(100)
        self.__bst.insert_element(92)
        self.__bst.remove_element(97)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_from_empty(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(34)
        self.assertEqual('[ ]', str(self.__bst))
        self.assertEqual('[ ]', self.__bst.pre_order())
        self.assertEqual('[ ]', self.__bst.post_order())

    def test_remove_from_empty_height(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(34)
        self.assertEqual(0, self.__bst.get_height())

    def test_remove_with_valueerror(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        with self.assertRaises(ValueError):
            self.__bst.remove_element(76)
        self.assertEqual('[ 14, 34, 97 ]', str(self.__bst))
        self.assertEqual('[ 34, 14, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 97, 34 ]', self.__bst.post_order())

    def test_remove_with_valueerror_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        with self.assertRaises(ValueError):
            self.__bst.remove_element(76)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_remove_insert(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(0)
        self.__bst.remove_element(34)
        self.__bst.remove_element(3)
        self.__bst.insert_element(34)
        self.__bst.insert_element(3)
        self.__bst.insert_element(28)
        self.assertEqual('[ 0, 3, 5, 14, 28, 34 ]', str(self.__bst))
        self.assertEqual('[ 14, 5, 0, 3, 34, 28 ]', self.__bst.pre_order())
        self.assertEqual('[ 3, 0, 5, 28, 34, 14 ]', self.__bst.post_order())

    def test_insert_remove_insert_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(3)
        self.__bst.insert_element(5)
        self.__bst.insert_element(0)
        self.__bst.remove_element(34)
        self.__bst.remove_element(3)
        self.__bst.insert_element(34)
        self.__bst.insert_element(3)
        self.__bst.insert_element(28)
        self.assertEqual(4, self.__bst.get_height())

# add test methods here
# each test should be in a method whose name begins with test_
# because of the different traversals there will be many cases
# where multiple assertions are appropriate for a single test

if __name__ == '__main__':
  unittest.main()