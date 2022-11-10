class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachable from the the methods.

    def __init__(self, value):
      self.value = value
      # TODO complete Node initialization
      self.left_child = None
      self.right_child = None
      self.height = 1
      self.left_height = 0
      self.right_height = 0

  def __init__(self):
    self.__root = None
    # TODO complete initialization

  def __set_height(self, subroot):
    if subroot.right_child is None and subroot.left_child is None:
      subroot.height = 1
      subroot.right_height = 0
      subroot.left_height = 0
    elif subroot.right_child is None:
      subroot.height = 1 + subroot.left_child.height
      subroot.right_height = 0
      subroot.left_height = subroot.left_child.height
    elif subroot.left_child is None:
      subroot.height = 1 + subroot.right_child.height
      subroot.right_height = subroot.right_child.height
      subroot.left_height = 0
    elif subroot.left_child.height > subroot.right_child.height:
      subroot.height = 1 + subroot.left_child.height
      subroot.right_height = subroot.right_child.height
      subroot.left_height = subroot.left_child.height
    else:
      subroot.height = 1 + subroot.right_child.height
      subroot.right_height = subroot.right_child.height
      subroot.left_height = subroot.left_child.height

  def __rotate(self, oldroot, imbalance):
    if imbalance == 'right':
      newroot = oldroot.right_child
      oldroot.right_child = newroot.left_child
      newroot.left_child = oldroot
    elif imbalance == 'left':
      newroot = oldroot.left_child
      oldroot.left_child = newroot.right_child
      newroot.right_child = oldroot
    self.__set_height(oldroot)
    self.__set_height(newroot)
    return newroot


  def __balance(self, subroot):
    if subroot.right_child is None and subroot.left_child is None:
      # a leaf node is inherently balanced
      self.__set_height(subroot)

    elif subroot.left_child is None:
      if abs(subroot.right_height - 0) > 1:
        # right imbalance
        if (subroot.right_child.right_height - subroot.right_child.left_height) < 0:
          # double rotation - first solve the kink to the left
          subroot.right_child = self.__rotate(subroot.right_child, 'left')
        # the single rotation and second-half of the double rotation
        subroot = self.__rotate(subroot, 'right')
      # if balanced - set height
      self.__set_height(subroot)
    elif subroot.right_child is None:
      if abs(0 - subroot.left_height) > 1:
        # left imbalance 
        if (subroot.left_child.right_height - subroot.left_child.left_height) > 0:
          # double rotation - first solve the kink to the right
          subroot.left_child = self.__rotate(subroot.left_child, 'right')
        # the single rotation and second-half of the double rotation
        subroot = self.__rotate(subroot, 'left')
      # if balanced - set height
      self.__set_height(subroot)

    elif abs(subroot.right_height - subroot.left_height) > 1:
      if (subroot.right_height - subroot.left_height) > 0:
        # right imbalance
        if (subroot.right_child.right_height - subroot.right_child.left_height) < 0:
          # double rotation - first solve the kink to the left
          subroot.right_child = self.__rotate(subroot.right_child, 'left')
        # the single rotation and second-half of the double rotation
        subroot = self.__rotate(subroot, 'right')
      elif (subroot.right_height - subroot.left_height) < 0:
        # left imbalance
        if (subroot.left_child.right_height - subroot.left_child.left_height) > 0:
          # double rotation - first solve the kink to the right
          subroot.left_child = self.__rotate(subroot.left_child, 'right')
        # the single rotation and second-half of the double rotation
        subroot = self.__rotate(subroot, 'left')
    else:
      # if balanced - set height
      self.__set_height(subroot)
    return subroot

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recur_insert(value, self.__root)

  def __recur_insert(self, value, subroot):
    # the private recursive method
    if subroot is None:
      return Binary_Search_Tree.__BST_Node(value)
    elif value < subroot.value:
      subroot.left_child = self.__recur_insert(value, subroot.left_child)
    elif value > subroot.value:
      subroot.right_child = self.__recur_insert(value, subroot.right_child)
    else:
      raise ValueError
    
    self.__set_height(subroot)

    return self.__balance(subroot)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recur_remove(value, self.__root)

  def __recur_remove(self, value, subroot):
    # the private recursive method
    if subroot is None:
      raise ValueError
    elif value < subroot.value:
      subroot.left_child = self.__recur_remove(value, subroot.left_child)
    elif value > subroot.value:
      subroot.right_child = self.__recur_remove(value, subroot.right_child)
    else:
      if subroot.left_child is not None and subroot.right_child is not None:
        current = subroot.right_child
        while current.left_child is not None:
          current = current.left_child
        subroot.value = current.value
        subroot.right_child = self.__recur_remove(current.value, subroot.right_child)
      elif subroot.left_child is None and subroot.right_child is None:
        return
      elif subroot.left_child is None:
        subroot = subroot.right_child
      else:
        subroot = subroot.left_child
  
    self.__set_height(subroot)
    return self.__balance(subroot)

  def __recur_to_list(self, subroot, bst_list):
    # private recursive method to create the in-order list
    if subroot is None:
      return ''
    else:
      self.__recur_to_list(subroot.left_child, bst_list)
      bst_list.append(subroot.value)
      self.__recur_to_list(subroot.right_child, bst_list)
      return bst_list

  def to_list(self):
    # create a python list of the tree's values
    # should be in in-order order
    if self.__root is None:
      return []
    else:
      bst_list = []
      bst_list = self.__recur_to_list(self.__root, bst_list)
    return bst_list

  def __recur_in_order(self, subroot):
    # the private recursive method for an in-order traversal
    # an in-order traversal is L-P-R
    if subroot is None:
      return ''
    else:
      bst_string = self.__recur_in_order(subroot.left_child)
      bst_string += str(subroot.value) + ', '
      bst_string += self.__recur_in_order(subroot.right_child)
      return bst_string

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    bst_string = self.__recur_in_order(self.__root)
    bst_string = bst_string[:-2]
    return '[ ' + bst_string + ' ]'

  def __recur_pre_order(self, subroot):
    # the private recursive method for a pre-order traversal
    # a pre-order traversal is P-L-R
    if subroot is None:
      return ''
    else:
      bst_string = str(subroot.value) + ', '
      bst_string += self.__recur_pre_order(subroot.left_child)
      bst_string += self.__recur_pre_order(subroot.right_child)
      return bst_string

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    bst_string = self.__recur_pre_order(self.__root)
    bst_string = bst_string[:-2]
    return '[ ' + bst_string + ' ]'

  def __recur_post_order(self, subroot):
    # the private recursive method for a post-order traversal
    # a post-order traversal is L-R-P
    if subroot is None:
      return ''
    else:
      bst_string = self.__recur_post_order(subroot.left_child)
      bst_string += self.__recur_post_order(subroot.right_child)
      bst_string += str(subroot.value) + ', '
      return bst_string

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    bst_string = self.__recur_post_order(self.__root)
    bst_string = bst_string[:-2]
    return '[ ' + bst_string + ' ]'

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
      return 0
    else:
      return self.__root.height

  def __str__(self):
    return self.in_order()

if __name__ == '__main__':
  pass #unit tests make the main section unnecessary.
  #tree = Binary_Search_Tree()
  #tree.insert_element(85)
  #tree.insert_element(126)
  #tree.insert_element(31)
  #tree.insert_element(22)
  #tree.insert_element(46)
  #tree.insert_element(92)
  #tree.insert_element(286)
  #print(tree)
  #tree.insert_element(28)
  #tree.insert_element(35)
  #tree.insert_element(50)
  #tree.insert_element(87)
  #tree.insert_element(107)
  #tree.insert_element(212)
  #tree.insert_element(307)
  #tree.insert_element(51)
  #print(tree)
  #tree.insert_element(89)
  #tree.insert_element(98)
  #tree.insert_element(112)
  #tree.insert_element(309)
  #tree.insert_element(115)
  #tree.remove_element(35)
  #print(tree)
