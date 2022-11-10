import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):

    def setUp(self):
        self.__bst = Binary_Search_Tree()

    #######################################################################
    ## basic tests from project 4
    #######################################################################

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
        self.assertEqual([34], self.__bst.to_list())

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
        self.assertEqual([8, 34], self.__bst.to_list())

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
        self.assertEqual([34, 47], self.__bst.to_list())

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
        self.assertEqual([-2, 14, 29, 34, 36, 97, 157] , self.__bst.to_list())

    def test_insert_balanced_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(36)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(29)
        self.__bst.insert_element(157)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_same_with_one(self):
        self.__bst.insert_element(34)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(34)
        self.assertEqual('[ 34 ]', str(self.__bst))
        self.assertEqual('[ 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 34 ]', self.__bst.post_order())
        self.assertEqual([34], self.__bst.to_list())
    
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
        self.assertEqual([34, 97], self.__bst.to_list())

    def test_insert_same_with_two_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        with self.assertRaises(ValueError):
            self.__bst.insert_element(97)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_root_leaving_zero(self):
        self.__bst.insert_element(34)
        self.__bst.remove_element(34)
        self.assertEqual('[ ]', str(self.__bst))
        self.assertEqual('[ ]', self.__bst.pre_order())
        self.assertEqual('[ ]', self.__bst.post_order())
        self.assertEqual([], self.__bst.to_list())

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
        self.assertEqual([97], self.__bst.to_list())

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
        self.assertEqual([14, 97], self.__bst.to_list())

    def test_remove_root_with_two_children_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.remove_element(34)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_from_empty(self):
        with self.assertRaises(ValueError):
            self.__bst.remove_element(34)
        self.assertEqual('[ ]', str(self.__bst))
        self.assertEqual('[ ]', self.__bst.pre_order())
        self.assertEqual('[ ]', self.__bst.post_order())
        self.assertEqual([], self.__bst.to_list())

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
        self.assertEqual([14, 34, 97], self.__bst.to_list())

    def test_remove_with_valueerror_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        with self.assertRaises(ValueError):
            self.__bst.remove_element(76)
        self.assertEqual(2, self.__bst.get_height())

    #######################################################################
    ## project 5 tests
    #######################################################################

    def test_to_list_with_strings(self):
        self.__bst.insert_element('c')
        self.__bst.insert_element('e')
        self.__bst.insert_element('a')
        self.assertEqual(['a', 'c', 'e'], self.__bst.to_list())

    def test_insert_single_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(4)
        self.assertEqual('[ 4, 14, 34 ]', self.__bst.in_order())
        self.assertEqual('[ 14, 4, 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 4, 34, 14 ]', self.__bst.post_order())
        self.assertEqual([4, 14, 34], self.__bst.to_list())
    
    def test_insert_single_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(4)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_single_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.assertEqual('[ 34, 97, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 97, 34, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 34, 102, 97 ]', self.__bst.post_order())
        self.assertEqual([34, 97, 102], self.__bst.to_list())

    def test_insert_single_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_double_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(24)
        self.assertEqual('[ 14, 24, 34 ]', self.__bst.in_order())
        self.assertEqual('[ 24, 14, 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 34, 24 ]', self.__bst.post_order())
        self.assertEqual([14, 24, 34], self.__bst.to_list())

    def test_insert_double_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(24)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_double_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.assertEqual('[ 34, 56, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 56, 34, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 34, 97, 56 ]', self.__bst.post_order())
        self.assertEqual([34, 56, 97], self.__bst.to_list())

    def test_insert_double_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.assertEqual(2, self.__bst.get_height())

    def test_insert_single_rotation_right_complex(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(2)
        self.__bst.insert_element(24)
        self.__bst.insert_element(0)
        self.assertEqual('[ 0, 2, 14, 24, 34, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 14, 2, 0, 34, 24, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 0, 2, 24, 97, 34, 14 ]', self.__bst.post_order())
        self.assertEqual([0, 2, 14, 24, 34, 97], self.__bst.to_list())

    def test_insert_single_rotation_right_complex_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(2)
        self.__bst.insert_element(24)
        self.__bst.insert_element(0)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_single_rotation_left_complex(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.assertEqual('[ 14, 34, 56, 97, 102, 500 ]', self.__bst.in_order())
        self.assertEqual('[ 97, 34, 14, 56, 102, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 56, 34, 500, 102, 97 ]', self.__bst.post_order())
        self.assertEqual([14, 34, 56, 97, 102, 500], self.__bst.to_list())

    def test_insert_single_rotation_left_complex_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(97)
        self.__bst.insert_element(14)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_double_rotation_right_complex(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(24)
        self.__bst.insert_element(2)
        self.__bst.insert_element(28)
        self.assertEqual('[ 2, 14, 24, 28, 34, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 24, 14, 2, 34, 28, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 2, 14, 28, 97, 34, 24 ]', self.__bst.post_order())
        self.assertEqual([2, 14, 24, 28, 34, 97], self.__bst.to_list())

    def test_insert_double_rotation_right_complex_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(24)
        self.__bst.insert_element(2)
        self.__bst.insert_element(28)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_double_rotation_left_complex(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(43)
        self.assertEqual('[ 14, 34, 43, 56, 97, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 56, 34, 14, 43, 97, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 43, 34, 102, 97, 56 ]', self.__bst.post_order())
        self.assertEqual([14, 34, 43, 56, 97, 102], self.__bst.to_list())

    def test_insert_double_rotation_left_complex_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(43)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_with_two_single_rotations(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(2)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.assertEqual('[ 2, 14, 34, 56, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 14, 2, 56, 34, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 2, 34, 97, 56, 14 ]', self.__bst.post_order())
        self.assertEqual([2, 14, 34, 56, 97], self.__bst.to_list())

    def test_insert_with_two_single_rotations_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(2)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_with_two_double_rotations(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(2)
        self.__bst.insert_element(14)
        self.__bst.insert_element(56)
        self.__bst.insert_element(24)
        self.__bst.insert_element(18)
        self.assertEqual('[ 2, 14, 18, 24, 34, 56 ]', self.__bst.in_order())
        self.assertEqual('[ 24, 14, 2, 18, 34, 56 ]', self.__bst.pre_order())
        self.assertEqual('[ 2, 18, 14, 56, 34, 24 ]', self.__bst.post_order())
        self.assertEqual([2, 14, 18, 24, 34, 56], self.__bst.to_list())

    def test_insert_with_two_double_rotations_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(2)
        self.__bst.insert_element(14)
        self.__bst.insert_element(56)
        self.__bst.insert_element(24)
        self.__bst.insert_element(18)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_double_single(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(17)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.assertEqual('[ 14, 17, 34, 56, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 17, 14, 56, 34, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 34, 97, 56, 17 ]', self.__bst.post_order())
        self.assertEqual([14, 17, 34, 56, 97], self.__bst.to_list())

    def test_insert_double_single_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(17)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.assertEqual(3, self.__bst.get_height())

    def test_insert_single_double(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.__bst.insert_element(44)
        self.__bst.insert_element(14)
        self.__bst.insert_element(49)
        self.assertEqual('[ 14, 34, 44, 49, 56, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 44, 34, 14, 56, 49, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 34, 49, 97, 56, 44 ]', self.__bst.post_order())
        self.assertEqual([14, 34, 44, 49, 56, 97], self.__bst.to_list())

    def test_insert_single_double_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.__bst.insert_element(44)
        self.__bst.insert_element(14)
        self.__bst.insert_element(49)
        self.assertEqual(3, self.__bst.get_height())
    
    def test_remove_leaf_single_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(2)
        self.__bst.remove_element(97)
        self.assertEqual('[ 2, 14, 34 ]', self.__bst.in_order())
        self.assertEqual('[ 14, 2, 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 2, 34, 14 ]', self.__bst.post_order())
        self.assertEqual([2, 14, 34], self.__bst.to_list())

    def test_remove_leaf_single_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(2)
        self.__bst.remove_element(97)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_leaf_single_roation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.remove_element(14)
        self.assertEqual('[ 34, 97, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 97, 34, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 34, 102, 97 ]', self.__bst.post_order())
        self.assertEqual([34, 97, 102], self.__bst.to_list())

    def test_remove_leaf_single_roation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.remove_element(14)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_leaf_double_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(22)
        self.__bst.remove_element(97)
        self.assertEqual('[ 14, 22, 34 ]', self.__bst.in_order())
        self.assertEqual('[ 22, 14, 34 ]', self.__bst.pre_order())
        self.assertEqual('[ 14, 34, 22 ]', self.__bst.post_order())
        self.assertEqual([14, 22, 34], self.__bst.to_list())

    def test_remove_leaf_double_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(22)
        self.__bst.remove_element(97)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_leaf_double_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(54)
        self.__bst.remove_element(14)
        self.assertEqual('[ 34, 54, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 54, 34, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ 34, 97, 54 ]', self.__bst.post_order())
        self.assertEqual([34, 54, 97], self.__bst.to_list())

    def test_remove_leaf_double_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(54)
        self.__bst.remove_element(14)
        self.assertEqual(2, self.__bst.get_height())

    def test_remove_with_one_child_single_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(97)
        self.assertEqual('[ -7, -2, 14, 20, 34, 56 ]', self.__bst.in_order())
        self.assertEqual('[ 14, -2, -7, 34, 20, 56 ]', self.__bst.pre_order())
        self.assertEqual('[ -7, -2, 20, 56, 34, 14 ]', self.__bst.post_order())
        self.assertEqual([-7, -2, 14, 20, 34, 56], self.__bst.to_list())

    def test_remove_with_one_child_single_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(97)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_one_child_single_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(20)
        self.__bst.insert_element(500)
        self.__bst.remove_element(14)
        self.assertEqual('[ 20, 34, 56, 97, 102, 500 ]', self.__bst.in_order())
        self.assertEqual('[ 97, 34, 20, 56, 102, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ 20, 56, 34, 500, 102, 97 ]', self.__bst.post_order())
        self.assertEqual([20, 34, 56, 97, 102, 500], self.__bst.to_list())

    def test_remove_with_one_child_single_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(20)
        self.__bst.insert_element(500)
        self.__bst.remove_element(14)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_one_child_double_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(0)
        self.__bst.insert_element(20)
        self.__bst.insert_element(24)
        self.__bst.remove_element(97)
        self.assertEqual('[ 0, 14, 20, 24, 34, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 20, 14, 0, 34, 24, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 0, 14, 24, 102, 34, 20 ]', self.__bst.post_order())
        self.assertEqual([0, 14, 20, 24, 34, 102], self.__bst.to_list())

    def test_remove_with_one_child_double_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(0)
        self.__bst.insert_element(20)
        self.__bst.insert_element(24)
        self.__bst.remove_element(97)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_one_child_double_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(20)
        self.__bst.insert_element(44)
        self.__bst.remove_element(14)
        self.assertEqual('[ 20, 34, 44, 56, 97, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 56, 34, 20, 44, 97, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 20, 44, 34, 102, 97, 56 ]', self.__bst.post_order())
        self.assertEqual([20, 34, 44, 56, 97, 102], self.__bst.to_list())

    def test_remove_with_one_child_double_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(102)
        self.__bst.insert_element(20)
        self.__bst.insert_element(44)
        self.__bst.remove_element(14)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_two_children_single_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(34)
        self.assertEqual('[ -7, -2, 14, 20, 56, 97 ]', self.__bst.in_order())
        self.assertEqual('[ 14, -2, -7, 56, 20, 97 ]', self.__bst.pre_order())
        self.assertEqual('[ -7, -2, 20, 97, 56, 14 ]', self.__bst.post_order())
        self.assertEqual([-7, -2, 14, 20, 56, 97], self.__bst.to_list())

    def test_remove_with_two_children_single_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(34)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_two_children_single_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(99)
        self.__bst.remove_element(34)
        self.assertEqual('[ -2, 14, 20, 56, 97, 99, 102, 500 ]', self.__bst.in_order())
        self.assertEqual('[ 56, 14, -2, 20, 102, 97, 99, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ -2, 20, 14, 99, 97, 500, 102, 56 ]', self.__bst.post_order())
        self.assertEqual([-2, 14, 20, 56, 97, 99, 102, 500], self.__bst.to_list())

    def test_remove_with_two_children_single_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(56)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(102)
        self.__bst.insert_element(500)
        self.__bst.insert_element(99)
        self.__bst.remove_element(34)
        self.assertEqual(4, self.__bst.get_height())

    def test_remove_with_two_children_double_rotation_right(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(24)
        self.__bst.remove_element(34)
        self.assertEqual('[ -2, 14, 20, 24, 97, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 20, 14, -2, 97, 24, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ -2, 14, 24, 102, 97, 20 ]', self.__bst.post_order())
        self.assertEqual([-2, 14, 20, 24, 97, 102], self.__bst.to_list())

    def test_remove_with_two_children_double_rotation_right_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(20)
        self.__bst.insert_element(24)
        self.__bst.remove_element(34)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_with_two_children_double_rotation_left(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(56)
        self.__bst.insert_element(20)
        self.__bst.insert_element(99)
        self.__bst.remove_element(34)
        self.assertEqual('[ 14, 20, 56, 97, 99, 102 ]', self.__bst.in_order())
        self.assertEqual('[ 56, 14, 20, 99, 97, 102 ]', self.__bst.pre_order())
        self.assertEqual('[ 20, 14, 97, 102, 99, 56 ]', self.__bst.post_order())
        self.assertEqual([14, 20, 56, 97, 99, 102], self.__bst.to_list())

    def test_remove_with_two_children_double_rotation_left_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(56)
        self.__bst.insert_element(20)
        self.__bst.insert_element(99)
        self.__bst.remove_element(34)
        self.assertEqual(3, self.__bst.get_height())

    def test_multiple_removals(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(56)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(97)
        self.__bst.remove_element(-2)
        self.__bst.remove_element(-7)
        self.assertEqual('[ 14, 20, 34, 56 ]', self.__bst.in_order())
        self.assertEqual('[ 34, 14, 20, 56 ]', self.__bst.pre_order())
        self.assertEqual('[ 20, 14, 56, 34 ]', self.__bst.post_order())
        self.assertEqual([14, 20, 34, 56], self.__bst.to_list())

    def test_multiple_removals_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(14)
        self.__bst.insert_element(97)
        self.__bst.insert_element(-2)
        self.__bst.insert_element(56)
        self.__bst.insert_element(20)
        self.__bst.insert_element(-7)
        self.__bst.remove_element(97)
        self.__bst.remove_element(-2)
        self.__bst.remove_element(-7)
        self.assertEqual(3, self.__bst.get_height())

    def test_remove_multiple_rotations(self):
        self.__bst.insert_element(85)
        self.__bst.insert_element(126)
        self.__bst.insert_element(31)
        self.__bst.insert_element(22)
        self.__bst.insert_element(46)
        self.__bst.insert_element(92)
        self.__bst.insert_element(286)
        self.__bst.insert_element(28)
        self.__bst.insert_element(35)
        self.__bst.insert_element(50)
        self.__bst.insert_element(87)
        self.__bst.insert_element(107)
        self.__bst.insert_element(212)
        self.__bst.insert_element(307)
        self.__bst.insert_element(51)
        self.__bst.insert_element(89)
        self.__bst.insert_element(98)
        self.__bst.insert_element(112)
        self.__bst.insert_element(309)
        self.__bst.insert_element(115)
        self.__bst.remove_element(31)
        self.assertEqual('[ 22, 28, 35, 46, 50, 51, 85, 87, 89, 92, 98, 107, 112, 115, 126, 212, 286, 307, 309 ]', self.__bst.in_order())
        self.assertEqual('[ 92, 85, 35, 22, 28, 50, 46, 51, 87, 89, 126, 107, 98, 112, 115, 286, 212, 307, 309 ]', self.__bst.pre_order())
        self.assertEqual('[ 28, 22, 46, 51, 50, 35, 89, 87, 85, 98, 115, 112, 107, 212, 309, 307, 286, 126, 92 ]', self.__bst.post_order())
        self.assertEqual([22, 28, 35, 46, 50, 51, 85, 87, 89, 92, 98, 107, 112, 115, 126, 212, 286, 307, 309], self.__bst.to_list())

    def test_remove_multiple_rotations_height(self):
        self.__bst.insert_element(85)
        self.__bst.insert_element(126)
        self.__bst.insert_element(31)
        self.__bst.insert_element(22)
        self.__bst.insert_element(46)
        self.__bst.insert_element(92)
        self.__bst.insert_element(286)
        self.__bst.insert_element(28)
        self.__bst.insert_element(35)
        self.__bst.insert_element(50)
        self.__bst.insert_element(87)
        self.__bst.insert_element(107)
        self.__bst.insert_element(212)
        self.__bst.insert_element(307)
        self.__bst.insert_element(51)
        self.__bst.insert_element(89)
        self.__bst.insert_element(98)
        self.__bst.insert_element(112)
        self.__bst.insert_element(309)
        self.__bst.insert_element(115)
        self.__bst.remove_element(31)
        self.assertEqual(5, self.__bst.get_height())

    def test_rotations_with_insertion_then_removal_then_insertion(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(101)
        self.__bst.insert_element(500)
        self.__bst.insert_element(98)
        self.__bst.remove_element(102)
        self.__bst.remove_element(56)
        self.__bst.remove_element(34)
        self.__bst.insert_element(100)
        self.__bst.insert_element(5)
        self.assertEqual('[ 5, 97, 98, 100, 101, 500 ]', self.__bst.in_order())
        self.assertEqual('[ 98, 97, 5, 101, 100, 500 ]', self.__bst.pre_order())
        self.assertEqual('[ 5, 97, 100, 500, 101, 98 ]', self.__bst.post_order())
        self.assertEqual([5, 97, 98, 100, 101, 500], self.__bst.to_list())

    def test_rotations_with_insertion_then_removal_then_insertion_height(self):
        self.__bst.insert_element(34)
        self.__bst.insert_element(56)
        self.__bst.insert_element(97)
        self.__bst.insert_element(102)
        self.__bst.insert_element(101)
        self.__bst.insert_element(500)
        self.__bst.insert_element(98)
        self.__bst.remove_element(102)
        self.__bst.remove_element(56)
        self.__bst.remove_element(34)
        self.__bst.insert_element(100)
        self.__bst.insert_element(5)
        self.assertEqual(3, self.__bst.get_height())

# add test methods here
# each test should be in a method whose name begins with test_
# because of the different traversals there will be many cases
# where multiple assertions are appropriate for a single test

if __name__ == '__main__':
  unittest.main()