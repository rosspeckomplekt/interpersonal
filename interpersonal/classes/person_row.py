"""
A PersonRow object is a mediator
that executes repetitive code that retrieves
the row of information about a Person
from the database
"""

from .person_dao import PersonDao


class PersonRow(object):
    """
    A PersonRow object is a mediator
    that executes repetitive code that retrieves
    the row of information about a Person
    from the database
    """

    def __init__(self, name):
        """
        Initialize a PersonRow object
        """
        person_dao = PersonDao()
        person_row = person_dao.get(name)
        self.name = name
        if person_row is not None:
            self.friendliness = person_row[1]
            self.dominance = person_row[2]
            self.n_friendliness = person_row[3]
            self.n_dominance = person_row[4]
