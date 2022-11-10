class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        new_node = Linked_List.__Node(val)
        self.__trailer.prev.next = new_node
        new_node.prev = self.__trailer.prev
        new_node.next = self.__trailer
        self.__trailer.prev = new_node
        self.__size += 1

    def __walk_to(self, index):
        # walks to the given index and returns the node
        # if the index is in the first half, start at the header
        if index <= (self.__size//2):
            cur = self.__header
            for _ in range(index + 1):
                cur = cur.next
        # otherwise start at the trailer
        else:
            cur = self.__trailer
            for _ in range(self.__size - index):
                cur = cur.prev
        return cur

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= self.__size or index < 0:
            raise IndexError
        new_node = Linked_List.__Node(val)
        cur = self.__walk_to(index - 1) # walks to the node before the insertion point
        new_node.next = cur.next
        new_node.prev = cur
        cur.next = new_node
        new_node.next.prev = new_node
        self.__size += 1
        

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= self.__size or index < 0:
            raise IndexError
        cur = self.__walk_to(index) # walks to the node that will be removed
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        self.__size -= 1
        return cur.val

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self.__size or index < 0:
            raise IndexError
        cur = self.__walk_to(index)
        return cur.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
        if self.__size != 0:
            cur = self.__header.next
            # establishing the new head node
            self.__header.next = self.__header.next.next
            cur.next.prev = self.__header
            # moving cur to the tail
            self.__trailer.prev.next = cur
            cur.prev = self.__trailer.prev
            self.__trailer.prev = cur
            cur.next = self.__trailer

        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__size == 0:
            return '[ ]'
        list_str = [None] * self.__size
        cur = self.__header.next
        i = 0
        while cur is not self.__trailer:
            list_str[i] = str(cur.val)
            cur = cur.next
            i += 1
        list_str = ', '.join(list_str)
        list_str = '[ ' + str(list_str) + ' ]'
        return list_str

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_item = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__iter_item is self.__trailer:
            raise StopIteration
        to_return = self.__iter_item.val
        self.__iter_item = self.__iter_item.next
        return to_return

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        new_list = Linked_List()
        cur = self.__trailer.prev
        while cur is not self.__header:
            new_list.append_element(cur.val)
            cur = cur.prev
        return new_list

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests

    a_list = Linked_List()
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should fail, you need to append to add to an empty list
        a_list.insert_element_at(2,0)
    except IndexError:
        print('Correctly caught error for using insert_element on an empty list')
    print(a_list)
    print('the linked list has a length of:', len(a_list))
    
    # testing the rotation
    # shouldn't be able to raise any errors
    a_list.rotate_left()
    print(a_list)
    print('empty list remains unchanged after rotate_left')

    # testing the reversed function
    # shouldn't be able to raise any errors
    print('the reversed list:', reversed(a_list))
    print('the original list:', a_list)
    print('the reversed list correctly looks the same as the original')
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without any errors
        a_list.append_element(2)
        a_list.append_element(4)
        a_list.append_element(7)
        a_list.append_element(-6)
        a_list.append_element(9)
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without any errors
        a_list.insert_element_at(2,2)
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should fail, would need to use append_element
        a_list.insert_element_at(3,6)
    except IndexError:
        print('Correctly caught error, would need to use append_element')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without any errors
        removed = a_list.remove_element_at(3)
        print('the item removed from index 3:', removed)
        print('checking that remove_element_at is returning the value of the node:', (removed + 10))
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should fail, index is too large
        removed = a_list.remove_element_at(5)
    except IndexError:
        print('Correctly caught index error, an index of 5 is too large')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # testing the rotation
    # shouldn't be able to raise any errors
    a_list.rotate_left()
    print(a_list)
    print('the list was correctly rotated')

    # testing the reversed function
    # shouldn't be able to raise any errors
    print('the list reversed:', reversed(a_list))
    print('the original list:', a_list)
    print('the original list remains unchanged')

    try:
        # should run without errors
        element = a_list.get_element_at(4)
        print('the element at index 4:', element)
        print('checking that get_element_at is returning the value of the node:', (element + 10))
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))
    print('the element at index 4 is still in the list')

    try:
        # should fail, negative indexes aren't valid
        a_list.insert_element_at(0,-2)
    except IndexError:
        print('Correctly caught index error, negative indexes are not valid')
    print(a_list)
    print('the linked list has a length of:', len(a_list))
    
    try:
        # should fail, negative indexes aren't valid
        a_list.remove_element_at(-1)
    except IndexError:
        print('Correctly caught index error, negative indexes are not valid')
    print(a_list)
    print('the linked list has a length of:', len(a_list))
    
    try:
        # should fail, negative indexes aren't valid
        a_list.get_element_at(-3)
    except IndexError:
        print('Correctly caught index error, negative indexes are not valid')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # testing the iterator
    # shouldn't be able to raise any errors
    print('testing the iterator:')
    for item in a_list:
        print(item)
    print()

    # testing the iterator on a reversed list
    # shouldn't be able to raise any errors
    print('testing the iterator with reversed():')
    for item in reversed(a_list):
        print(item)
    print()

    try:
        # should run without errors
        a_list.remove_element_at(4)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.remove_element_at(1)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.remove_element_at(2)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.remove_element_at(0)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.remove_element_at(0)
        print(a_list)
        print('the linked list has a length of:', len(a_list))
    except IndexError:
        print('Error: unexpected index error')
    
    try:
        # should fail, can't remove anything from an empty list
        a_list.remove_element_at(0)
    except IndexError:
        print('Correctly caught index error, nothing to remove from an empty list')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # iterating over an empty list
    print('testing iteration on an empty list')
    for item in a_list:
        print('unexpected print in the for loop')
    print('correctly does not print anything in the for loop')
    print()
    
    try:
        # should run without errors
        a_list.append_element(94)
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # testing the rotation
    # shouldn't be able to raise any errors
    a_list.rotate_left()
    print(a_list)
    print('the list correctly looks the same after being rotated')

    # testing the reversed function
    # shouldn't be able to raise any errors
    print('the reversed list:', reversed(a_list))
    print('the original list:', a_list)
    print('the list correctly looks the same when reversed')

    # testing the iterator
    # shouldn't be able to raise any errors
    print('testing the iterator:')
    for item in a_list:
        print(item)
    print()

    try:
        # should run without error
        a_list.insert_element_at(123, 0)
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without error
        print('the element at index 0:', a_list.get_element_at(0))
    except IndexError:
        print('Error: unexpected index error')
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # testing the rotation
    # shouldn't be able to raise any errors
    a_list.rotate_left()
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without error
        a_list.append_element(None)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.append_element('turtle')
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.append_element(2.34)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.append_element('hello')
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.append_element(7)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.append_element('ciao')
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.insert_element_at('cat', 0)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.insert_element_at(19, 7)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.insert_element_at(-92, 8)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        a_list.insert_element_at('car', 3)
        print(a_list)
        print('the linked list has a length of:', len(a_list))
    except IndexError:
        print('Error: unexpected index error')

    # testing the rotation
    # shouldn't be able to raise any errors
    a_list.rotate_left()
    print(a_list)
    print('the linked list has a length of:', len(a_list))

    # testing the iterator
    # shouldn't be able to raise any eroors
    print('testing the iterator:')
    for item in a_list:
        print(item)
    print()

    # testing the reversed function
    # shouldn't be able to raise any errors
    print('the list reversed:', reversed(a_list))
    print('the original list:', a_list)
    print('the linked list has a length of:', len(a_list))

    try:
        # should run without error
        element = a_list.get_element_at(11)
        print('the element at index 11:', element)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        element = a_list.get_element_at(4)
        print('the element at index 4:', element)
        print(a_list)
        print('the linked list has a length of:', len(a_list))
    except IndexError:
        print('Error: unexpected index error')
    
    try:
        # should run without error
        removed = a_list.remove_element_at(2)
        print('the element removed from index 2:', removed)
        print(a_list)
        print('the linked list has a length of:', len(a_list))

        removed = a_list.remove_element_at(10)
        print('the element removed from index 10:', removed)
        print(a_list)
        print('the linked list has a length of:', len(a_list))
    except IndexError:
        print('Error: unexpected index error')