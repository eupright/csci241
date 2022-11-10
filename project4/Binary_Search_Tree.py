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

  def __init__(self):
    self.__root = None
    # TODO complete initialization

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
    
    if subroot.right_child is None:
      subroot.height = 1 + subroot.left_child.height
    elif subroot.left_child is None:
      subroot.height = 1 + subroot.right_child.height
    elif subroot.left_child.height > subroot.right_child.height:
      subroot.height = 1 + subroot.left_child.height
    else:
      subroot.height = 1 + subroot.right_child.height
    
    return subroot

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
      elif subroot.left_child is None:
        subroot = subroot.right_child
      else:
        subroot = subroot.left_child
      return subroot
    
    if subroot.right_child is None and subroot.left_child is None:
      subroot.height = 1
    elif subroot.right_child is None:
      subroot.height = 1 + subroot.left_child.height
    elif subroot.left_child is None:
      subroot.height = 1 + subroot.right_child.height
    elif subroot.left_child.height > subroot.right_child.height:
      subroot.height = 1 + subroot.left_child.height
    else:
      subroot.height = 1 + subroot.right_child.height
    
    return subroot

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
  #print(tree)
  #print(tree.get_height())
  #tree.insert_element(9)
  #print(tree)
  #print(tree.pre_order())
  #print(tree.get_height())
  
  #tree.insert_element(3)
  #print(tree)
  #print(tree.get_height())
  #tree.insert_element(24)
  #print(tree)
  #print(tree.get_height())
  #tree.insert_element(-2)
  #print(tree)
  #print(tree.get_height())
  #tree.insert_element(15)
  #print(tree)
  #print(tree.get_height())
  #tree.insert_element(123)
  #print(tree)
  #print(tree.pre_order())
  #print(tree.post_order())
  #print(tree.get_height())

  #tree.remove_element(9)
  #print(tree)
  #print(tree.pre_order())
  #print(tree.post_order())
  #print(tree.get_height())

  #tree.remove_element(-2)
  #print(tree)
  #print(tree.pre_order())
  #print(tree.post_order())
  #print(tree.get_height())
