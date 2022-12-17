class Production:
    """
    Class to describe a production rule for a grammar
    """

    def __init__(self, left_term, right_term):
        """
        Constructor for Production class
        @param: left_term - left term of the production
        @param: right_term - right term of the production
        """
        self.__left_term = left_term
        self.__right_term = right_term

    """
    Getters
    """

    def get_left_term(self):
        return self.__left_term

    def get_right_term(self):
        return self.__right_term

    """
    Setters
    """

    def set_left_term(self, new_left):
        self.__left_term = new_left

    def set_right_term(self, new_right):
        self.__right_term = new_right

    """
    Str function
    """

    def __str__(self):
        right_str = "["
        for i in range(len(self.get_right_term())):
            if i != len(self.get_right_term()) - 1:
                right_str += self.get_right_term()[i] + ", "
            else:
                right_str += self.get_right_term()[i]
        right_str += "]"
        return self.__left_term + " -> " + right_str

    def __eq__(self, other):
        return self.__right_term == other.get_right_term() and self.__left_term == other.get_left_term()

