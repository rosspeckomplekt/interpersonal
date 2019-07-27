from .person_dao import PersonDao
from .person_row import PersonRow
from .personality import Personality
from .trait import Trait


class Person(object):
    """
    A Person describes a person.
    A person can be a human  or an AI agent, such as
    a non-player character or a conversational interface
    """

    def __init__(self, name):
        """
        Initialize a Person object with a name
        """
        self.name = name
        if self.is_not_in_db():
            print(name + " is not in db")
            self.add_to_db()

    def is_not_in_db(self):
        """
        Check whether this Person is in the database or not
        """
        result = PersonDao.get(self.name)
        print(result)
        return result is None

    def add_to_db(self):
        """
        Add this Person to the database
        """
        print("adding " + self.name + " to persons.db")
        PersonDao.insert(self.name)

    def add_trait(self, trait_name):
        """
        Add a trait to this Person
        """
        trait = Trait(trait_name)
        person_row = PersonRow(self.name)
        if person_row is None:
            print("Could not find " + self.name +
                  " in the persons database.")
            return
        # print("Person Row is for " + self.name)
        f = person_row.friendliness
        d = person_row.dominance
        n_f = person_row.n_friendliness
        n_d = person_row.n_dominance
        if trait.has_friendliness():
            f = ((f * n_f) + trait.get_friendliness()) / (n_f + 1)
            PersonDao.set_friendliness(self.name, f)
            PersonDao.set_n_friendliness(self.name, n_f + 1)
        if trait.has_dominance():
            d = ((d * n_d) + trait.get_dominance()) / (n_d + 1)
            PersonDao.set_dominance(self.name, d)
            PersonDao.set_n_dominance(self.name, n_d + 1)

    def get_personality(self):
        """
        Get the Personality of this Person
        """
        person_row = PersonRow(self.name)
        friendliness = person_row.friendliness
        dominance = person_row.dominance
        personality = Personality(friendliness, dominance)
        return personality

    def add_description(self, paragraph):
        """
        Add a description to this Person
        A description is a paragraph of words describing the Person
        Ideally a description contains trait words (eg kind, mean)
        """
        words = paragraph.split()
        for word in words:
            self.add_trait(word)
