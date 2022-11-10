import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
  with open(filename, 'r') as my_file:
    text = my_file.read().splitlines()
    text = ''.join(text)
  stack = Stack()
  opening = '([{'
  closing = ')]}'
  for c in text:
    if c in opening:
      stack.push(c)
    elif c in closing:
      if len(stack) == 0:
        return False
      elif closing.index(c) != opening.index(stack.pop()):
        return False
  if len(stack) == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


