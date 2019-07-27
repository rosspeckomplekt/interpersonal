"""
A Trait is a type of behavior that a Person displays
"""

from .trait_dao import TraitDao


class Trait(object):
    """
    A Trait is a type of behavior that a Person displays
    """

    def __init__(self, name):
        """
        Initialize a Trait object
        """
        self.name = name
        self.traitDao = TraitDao()

    def has_friendliness(self):
        """
        Check whether the Trait has a friendliness value
        """
        trait = self.traitDao.get_friendliness(self.name)
        if trait is None:
            return False
        else:
            return True

    def has_dominance(self):
        """
        Check whether the Trait has a dominance value
        """
        trait = self.traitDao.get_dominance(self.name)
        if trait is None:
            return False
        else:
            return True

    def get_friendliness(self):
        """
        Get the friendliness value of the Trait
        """
        trait = self.traitDao.get_friendliness(self.name)
        friendliness = trait[1]
        return friendliness

    def get_dominance(self):
        """
        Get the dominance value of the Trait
        """
        trait = self.traitDao.get_dominance(self.name)
        dominance = trait[1]
        return dominance
