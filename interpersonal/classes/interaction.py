"""
An Interaction describes the interaction between
two Persons
"""


class Interaction:
    """
    An Interaction describes the interaction between
    two Persons
    """

    def __init__(self, person_a, person_b):
        """
        Initialize an Interaction object for two Persons
        So we can compute the various Interaction functions
        :param person_a: A Person
        :param person_b: Another Person
        """
        self.person_a = person_a
        self.person_b = person_b

    def find_dominator(self):
        """
        Find which Person in the Interaction has the higher dominance
        """
        a_dominance = self.person_a.get_personality().dominance
        b_dominance = self.person_b.get_personality().dominance
        print("The dominator is: ")

        if a_dominance > b_dominance:
            print(self.person_a.name)
            return self.person_a
        else:
            print(self.person_b.name)
            return self.person_b

    def is_alliance(self):
        """
        Find the magnitude with which the two Persons
        are likely to be allies
        """
        a_friendliness = self.person_a.get_personality().friendliness
        b_friendliness = self.person_b.get_personality().friendliness
        if a_friendliness * b_friendliness >= 0:
            print(self.person_a.name + " and " + self.person_b.name + " are friends")
            return True
        else:
            print(self.person_a.name + " and " + self.person_b.name + " are enemies")
            return False

    def get_alliance(self):
        """
        Find the magnitude with which the two Persons are predicted to be
        allied or enemies
        """
        a = self.person_a.get_personality().friendliness
        b = self.person_b.get_personality().dominance
        return (a * b) * (abs(a) + abs(b)) / 20
