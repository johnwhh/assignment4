class SortedPriorityQueue:
    """Priority queue using a sorted list implementation"""
    class _Item:
        """Structure to store priority queue items in"""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __le__(self, other):
            return self._key <= other._key

    def __init__(self):
        """Creates empty list to hold the items of the priority queue"""
        self._data = []

    def __len__(self):
        """Returns number of elements in the priority queue"""
        return len(self._data)

    def is_empty(self):
        """Checks if the priority queue is empty"""
        return len(self) == 0

    def show(self):
        """Provides visual representation of priority queue"""
        if self.is_empty():
            print('[]')
            return
        line = '['
        for item in self._data:
            line += '(' + str(item._key) + ', ' + str(item._value) + '), '
        line = line[:-2] + ']'
        print(line)

    def add(self, key, value):
        """Inserts key-value pair into the appropriate spot in priority queue"""
        new = self._Item(key, value)

        if self.is_empty():
            self._data.append(new)
        else:
            for i, item in enumerate(self._data):
                if new <= item:
                    self._data.insert(i, new)
                    break
                if i == len(self) - 1:
                    self._data.append(new)
                    break

    def min(self):
        """Returns minimum item in the form of a tuple"""
        if self.is_empty():
            return None
        t = (self._data[0]._key, self._data[0]._value)
        return t

    def remove_min(self):
        """Removes and returns minimum item in the form of a tuple"""
        if self.is_empty():
            return None
        t = (self._data[0]._key, self._data[0]._value)
        self._data = self._data[1:]
        return t


def main():
    spq = SortedPriorityQueue()
    spq.add(0, 'Pepper')
    spq.add(2, 'Salt')
    spq.add(1, 'Garlic')
    spq.add(5, 'Oregano')
    spq.add(3, 'Saffron')
    print('Example using this Sorted Priority Queue:')
    spq.show()
    print('Removing min:', spq.remove_min())
    spq.show()
    queue = SortedPriorityQueue()
    while True:
        print()
        print('Your Sorted Priority Queue:')
        queue.show()
        print('A. Add')
        print('G. Get minimum')
        print('R. Remove minimum')
        print('Q. Quit')
        choice = str(input())
        if choice.lower() == 'a':
            while True:
                key = input('Please enter the key: ')

                try:
                    int(key) == 0  # check if it's an int
                    break
                except ValueError:
                    print('Invalid input')

            value = input('Please enter the value: ')
            queue.add(key, value)
        elif choice.lower() == 'g':
            print('Minimum:', queue.min())
        elif choice.lower() == 'r':
            print('Removing min:', queue.remove_min())
        elif choice.lower() == 'q':
            # break the loop and quit the program
            break
        else:
            # the provided input was not valid
            print("Invalid input")

if __name__ == '__main__':
    main()
