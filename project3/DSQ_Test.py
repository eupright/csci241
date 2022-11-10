import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')
  
  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')
  
  def test_empty_queue_string(self):
    self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')

  def test_push_front_empty_deque(self):
    self.__deque.push_front('Victory')
    self.assertEqual('[ Victory ]', str(self.__deque))

  def test_push_back_empty_deque(self):
    self.__deque.push_back('Victory')
    self.assertEqual('[ Victory ]', str(self.__deque))

  def test_push_empty_stack(self):
    self.__stack.push('Victory')
    self.assertEqual('[ Victory ]', str(self.__stack))

  def test_enqueue_empty_queue(self):
    self.__queue.enqueue('Victory')
    self.assertEqual('[ Victory ]', str(self.__queue))

  def test_push_front_with_one_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    self.assertEqual('[ Mary, William ]', str(self.__deque))

  def test_push_back_with_one_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    self.assertEqual('[ William, Mary ]', str(self.__deque))

  def test_push_with_one_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.assertEqual('[ Mary, William ]', str(self.__stack))

  def test_enqueue_with_one_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.assertEqual('[ William, Mary ]', str(self.__queue))

  def test_push_front_with_two_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('&')
    self.__deque.push_front('Mary')
    self.assertEqual('[ Mary, &, William ]', str(self.__deque))

  def test_push_back_with_two_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('&')
    self.__deque.push_back('Mary')
    self.assertEqual('[ William, &, Mary ]', str(self.__deque))

  def test_push_with_two_stack(self):
    self.__stack.push('William')
    self.__stack.push('&')
    self.__stack.push('Mary')
    self.assertEqual('[ Mary, &, William ]', str(self.__stack))

  def test_enqueue_with_two_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('&')
    self.__queue.enqueue('Mary')
    self.assertEqual('[ William, &, Mary ]', str(self.__queue))
  
  def test_push_front_and_back_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_back('&')
    self.__deque.push_front('of')
    self.__deque.push_back('Mary')
    self.__deque.push_front('College')
    self.assertEqual('[ College, of, William, &, Mary ]', str(self.__deque))

  def test_push_front_with_many_deque(self):
    for n in range(9):
      self.__deque.push_front(n)
    self.assertEqual('[ 8, 7, 6, 5, 4, 3, 2, 1, 0 ]', str(self.__deque))

  def test_push_back_with_many_deque(self):
    for n in range(9):
      self.__deque.push_back(n)
    self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]', str(self.__deque))

  def test_push_with_many_stack(self):
    for n in range(9):
      self.__stack.push(n)
    self.assertEqual('[ 8, 7, 6, 5, 4, 3, 2, 1, 0 ]', str(self.__stack))

  def test_enqueue_with_many_queue(self):
    for n in range(9):
      self.__queue.enqueue(n)
    self.assertEqual('[ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]', str(self.__queue))

  def test_get_empty_length_deque(self):
    self.assertEqual(0, len(self.__deque))

  def test_get_empty_length_stack(self):
    self.assertEqual(0, len(self.__stack))

  def test_get_empty_length_queue(self):
    self.assertEqual(0, len(self.__queue))

  def test_get_one_length_front_deque(self):
    self.__deque.push_front('Victory')
    self.assertEqual(1, len(self.__deque))

  def test_get_one_length_back_deque(self):
    self.__deque.push_back('Victory')
    self.assertEqual(1, len(self.__deque))

  def test_get_one_length_stack(self):
    self.__stack.push('Victory')
    self.assertEqual(1, len(self.__stack))

  def test_get_one_length_queue(self):
    self.__queue.enqueue('Victory')
    self.assertEqual(1, len(self.__queue))

  def test_get_two_length_front_and_back_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_back('Mary')
    self.assertEqual(2, len(self.__deque))

  def test_get_two_length_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.assertEqual(2, len(self.__stack))

  def test_get_two_length_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.assertEqual(2, len(self.__queue))

  def test_pop_front_leaving_zero_returned_value_deque(self):
    self.__deque.push_front('Victory')
    returned = self.__deque.pop_front()
    self.assertEqual('Victory', returned)

  def test_pop_front_leaving_zero_remaining_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_leaving_zero_length_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_leaving_zero_returned_value_deque(self):
    self.__deque.push_back('Victory')
    returned = self.__deque.pop_back()
    self.assertEqual('Victory', returned)

  def test_pop_back_leaving_zero_remaining_deque(self):
    self.__deque.push_back('Victory')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_leaving_zero_length_deque(self):
    self.__deque.push_back('Victory')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))

  def test_pop_leaving_zero_returned_value_stack(self):
    self.__stack.push('Victory')
    returned = self.__stack.pop()
    self.assertEqual('Victory', returned)

  def test_pop_leaving_zero_remaining_stack(self):
    self.__stack.push('Victory')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_leaving_zero_length_stack(self):
    self.__stack.push('Victory')
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_dequeue_leaving_zero_returned_value_queue(self):
    self.__queue.enqueue('Victory')
    returned = self.__queue.dequeue()
    self.assertEqual('Victory', returned)

  def test_dequeue_leaving_zero_remaining_queue(self):
    self.__queue.enqueue('Victory')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_leaving_zero_length_queue(self):
    self.__queue.enqueue('Victory')
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))
  
  def test_pop_front_leaving_one_returned_value_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    returned = self.__deque.pop_front()
    self.assertEqual('Mary', returned)

  def test_pop_front_leaving_one_remaining_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    self.__deque.pop_front()
    self.assertEqual('[ William ]', str(self.__deque))

  def test_pop_front_leaving_one_length_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    self.__deque.pop_front()
    self.assertEqual(1, len(self.__deque))

  def test_pop_back_leaving_one_returned_value_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    returned = self.__deque.pop_back()
    self.assertEqual('Mary', returned)

  def test_pop_back_leaving_one_remaining_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    self.__deque.pop_back()
    self.assertEqual('[ William ]', str(self.__deque))

  def test_pop_back_leaving_one_length_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    self.__deque.pop_back()
    self.assertEqual(1, len(self.__deque))

  def test_pop_leaving_one_returned_value_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    returned = self.__stack.pop()
    self.assertEqual('Mary', returned)

  def test_pop_leaving_one_remaining_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.__stack.pop()
    self.assertEqual('[ William ]', str(self.__stack))

  def test_pop_leaving_one_length_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_dequeue_leaving_one_returned_value_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    returned = self.__queue.dequeue()
    self.assertEqual('William', returned)

  def test_dequeue_leaving_one_remaining_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.__queue.dequeue()
    self.assertEqual('[ Mary ]', str(self.__queue))

  def test_dequeue_leaving_one_length_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.__queue.dequeue()
    self.assertEqual(1, len(self.__queue))

  def test_peek_front_with_one_element_deque(self):
    self.__deque.push_front('Victory')
    returned = self.__deque.peek_front()
    self.assertEqual('Victory', returned)

  def test_peek_front_with_one_element_remaining_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.peek_front()
    self.assertEqual('[ Victory ]', str(self.__deque))

  def test_peek_front_with_one_element_length_deque(self):
    self.__deque.push_front('Victory')
    self.__deque.peek_front()
    self.assertEqual(1, len(self.__deque))

  def test_peek_back_with_one_element_deque(self):
    self.__deque.push_back('Victory')
    returned = self.__deque.peek_back()
    self.assertEqual('Victory', returned)

  def test_peek_back_with_one_element_remaining_deque(self):
    self.__deque.push_back('Victory')
    self.__deque.peek_back()
    self.assertEqual('[ Victory ]', str(self.__deque))

  def test_peek_back_with_one_element_length_deque(self):
    self.__deque.push_back('Victory')
    self.__deque.peek_back()
    self.assertEqual(1, len(self.__deque))

  def test_peek_with_one_element_stack(self):
    self.__stack.push('Victory')
    returned = self.__stack.peek()
    self.assertEqual('Victory', returned)

  def test_peek_with_one_element_remaining_stack(self):
    self.__stack.push('Victory')
    self.__stack.peek()
    self.assertEqual('[ Victory ]', str(self.__stack))

  def test_peek_with_one_element_length_stack(self):
    self.__stack.push('Victory')
    self.__stack.peek()
    self.assertEqual(1, len(self.__stack))

  def test_peek_with_one_element_queue(self):
    self.__queue.enqueue('Victory')
    returned = self.__queue.peek()
    self.assertEqual('Victory', returned)

  def test_peek_with_one_element_remaining_queue(self):
    self.__queue.enqueue('Victory')
    self.__queue.peek()
    self.assertEqual('[ Victory ]', str(self.__queue))

  def test_peek_with_one_element_length_queue(self):
    self.__queue.enqueue('Victory')
    self.__queue.peek()
    self.assertEqual(1, len(self.__queue))

  def test_peek_front_with_two_elements_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    returned = self.__deque.peek_front()
    self.assertEqual('Mary', returned)

  def test_peek_front_with_two_elements_remaining_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    self.__deque.peek_front()
    self.assertEqual('[ Mary, William ]', str(self.__deque))

  def test_peek_front_with_two_elements_length_deque(self):
    self.__deque.push_front('William')
    self.__deque.push_front('Mary')
    self.__deque.peek_front()
    self.assertEqual(2, len(self.__deque))

  def test_peek_back_with_two_elements_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    returned = self.__deque.peek_back()
    self.assertEqual('Mary', returned)

  def test_peek_back_with_two_elements_remaining_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    self.__deque.peek_back()
    self.assertEqual('[ William, Mary ]', str(self.__deque))

  def test_peek_back_with_two_elements_length_deque(self):
    self.__deque.push_back('William')
    self.__deque.push_back('Mary')
    self.__deque.peek_back()
    self.assertEqual(2, len(self.__deque))

  def test_peek_with_two_elements_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    returned = self.__stack.peek()
    self.assertEqual('Mary', returned)

  def test_peek_with_two_elements_remaining_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.__stack.peek()
    self.assertEqual('[ Mary, William ]', str(self.__stack))

  def test_peek_with_two_elements_length_stack(self):
    self.__stack.push('William')
    self.__stack.push('Mary')
    self.__stack.peek()
    self.assertEqual(2, len(self.__stack))

  def test_peek_with_two_elements_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    returned = self.__queue.peek()
    self.assertEqual('William', returned)

  def test_peek_with_two_elements_remaining_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.__queue.peek()
    self.assertEqual('[ William, Mary ]', str(self.__queue))

  def test_peek_with_two_elements_length_queue(self):
    self.__queue.enqueue('William')
    self.__queue.enqueue('Mary')
    self.__queue.peek()
    self.assertEqual(2, len(self.__queue))

  def test_pop_front_with_none_deque(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_with_none_return_deque(self):
    returned = self.__deque.pop_front()
    self.assertEqual(returned, None)

  def test_pop_front_with_none_length_deque(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_back_with_none_deque(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_with_none_return_deque(self):
    returned = self.__deque.pop_back()
    self.assertEqual(returned, None)

  def test_pop_back_with_none_length_deque(self):
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))

  def test_pop_with_none_stack(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_with_none_return_stack(self):
    returned = self.__stack.pop()
    self.assertEqual(returned, None)

  def test_pop_with_none_length_stack(self):
    self.__stack.pop()
    self.assertEqual(0, len(self.__stack))

  def test_dequeue_with_none_queue(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_with_none_return_queue(self):
    returned = self.__queue.dequeue()
    self.assertEqual(returned, None)

  def test_dequeue_with_none_length_queue(self):
    self.__queue.dequeue()
    self.assertEqual(0, len(self.__queue))

  def test_peek_front_with_none_deque(self):
    self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_front_with_none_return_deque(self):
    returned = self.__deque.peek_front()
    self.assertEqual(returned, None)

  def test_peek_front_with_none_length_deque(self):
    self.__deque.peek_front()
    self.assertEqual(0, len(self.__deque))

  def test_peek_back_with_none_deque(self):
    self.__deque.peek_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_back_with_none_return_deque(self):
    returned = self.__deque.peek_back()
    self.assertEqual(returned, None)

  def test_peek_back_with_none_length_deque(self):
    self.__deque.peek_front()
    self.assertEqual(0, len(self.__deque))

  def test_peek_with_none_stack(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))

  def test_peek_with_none_return_stack(self):
    returned = self.__stack.peek()
    self.assertEqual(returned, None)

  def test_peek_with_none_length_stack(self):
    self.__stack.peek()
    self.assertEqual(0, len(self.__stack))

  def test_peek_with_none_queue(self):
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))

  def test_peek_with_none_return_queue(self):
    returned = self.__queue.peek()
    self.assertEqual(returned, None)

  def test_peek_with_none_length_queue(self):
    self.__queue.peek()
    self.assertEqual(0, len(self.__queue))


  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should be in a method whose name begins with test_

if __name__ == '__main__':
  unittest.main()

