class LinkedList:
    """
    You should implement the methods of this class which are currently
    raising a NotImplementedError!
    Don't change the name of the class or any of the methods.
    """
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        if self.__root is None:
            raise RuntimeError("Tried to remove from the list but it was already empty!")
        marker = self.__root
        self.__root = marker.get_next()
        marker.set_next(None)
        return marker

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, text):
        marker = self.__root
        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        raise LookupError("Node with text {} was not found in the linked list!".format(text))

    def size(self):
        marker = self.__root
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count



