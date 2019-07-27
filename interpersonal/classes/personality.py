"""
A Personality is a pair of friendliness and dominance values
"""


class Personality(object):
    """
    A Personality is a pair of friendliness and dominance values
    """

    def __init__(self, friendliness, dominance):
        """
        Initialize a Personality object
        """
        self.friendliness = friendliness
        self.dominance = dominance
