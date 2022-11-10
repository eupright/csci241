from Linked_List import Linked_List
import sys

class Run_Length:
    def __init__(self, pair):
        self.symbol = pair[0]
        self.repetitions = pair[1]

def load_encodings(filename):
    with open(filename) as f:
        lines = f.readlines()
    encodings = Linked_List()
    for line in lines:
        row = Linked_List()
        for run_length_pair in line.split():
            row.append_element(Run_Length(run_length_pair.split(',')))
        encodings.append_element(row)
    return encodings

def display(encodings):
    # TODO replace pass with your display implementation.
    for i in range(len(encodings)):
        print()
        for j in range(len(encodings.get_element_at(i))):
            print(encodings.get_element_at(i).get_element_at(j).symbol * int(encodings.get_element_at(i).get_element_at(j).repetitions), end='')

if __name__ == '__main__':
    # The list sys.argv contains everything the user typed on the command 
    # line after the word python. For example, if the user types
    # python RLE_ASCII_Art.py smile.txt
    # then printing the contents of sys.argv shows
    # ['RLE_ASCII_Art.py', 'smile.txt']
    if len(sys.argv) < 2:
        # This means the user did not provide the required arguments.
        # Show the correct usage.
        print('Usage: python RLE_ASCII_Art.py encoding_file.txt')
    else:
        encodings = load_encodings(sys.argv[1])
        display(encodings)
