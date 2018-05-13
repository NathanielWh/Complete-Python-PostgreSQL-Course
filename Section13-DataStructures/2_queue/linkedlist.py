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

    def remove_end_from_list(self):

        if self.__root is None:
            return "No one in cue"

        marker = self.__root

        if marker.get_next() is None:
            self.__root = None
            return marker

        while marker:
            if marker.get_next().get_next() is None:
                to_drop = marker.get_next()
                marker.set_next(None)
            marker = marker.get_next()

        return to_drop

        """
        Implement this method! It should:
        - Iterate over each node
        - Find both the second-to-last node and the last node
        - Set the second-to-last node's next to be None
        - Return the last node
        :return: the removed Node.
        """
        raise NotImplementedError()

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        """
        You can reuse the method written for the previous assignment here.

        :param name: the name of the Node to find.
        :return: the found Node, or raises a LookupError if not found.
        """
        raise NotImplementedError()

    def size(self):

        count = 0

        if self.__root is None:
            return count

        marker = self.__root
        while marker:
            count += 1
            marker = marker.get_next()

        return count




