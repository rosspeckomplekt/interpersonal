"""
A Company is a commercial company that wants to look for
People of certain personalities
"""

from .person_dao import PersonDao
from .trait import Trait
from scipy.spatial import distance


class Company:
    """
    A Company is a commercial company that wants to look for
    People of certain personalities
    """

    def __init__(self, name):
        """
        Initialize a Company object
        """
        self.name = name
        self.person_dao = PersonDao()

    def find_description(self, paragraph):
        """
        Return a string of Persons fitting the
        paragraph of description
        sorted in descending order of relevance
        """
        friendliness = 0
        n_friendliness = 0
        dominance = 0
        n_dominance = 0

        words = paragraph.split()
        for word in words:
            trait = Trait(word)
            if trait.has_friendliness():
                friendliness += trait.get_friendliness()
                n_friendliness += 1
            if trait.has_dominance():
                dominance += trait.get_dominance()
                n_dominance += 1
        if n_friendliness > 0:
            friendliness = friendliness / n_friendliness
        if n_dominance > 0:
            dominance = dominance / n_dominance
        company_vector = (friendliness, dominance)
        persons = self.person_dao.get_all()
        if persons is None:
            print("No people in database")
        # distances has format [["mike", 0.9], ["misaki", 0.8],...]
        distances = []
        for person in persons:
            person_vector = (person[1], person[2])
            dst = distance.euclidean(person_vector, company_vector)
            distances.append([person[0], dst])
        distances.sort(key=lambda x: float(x[1]))
        result = []
        for answer in distances:
            result.append(answer[0])
            # print(answer[0])
        # returns the closest matches in
        # descending order of closeness of the match
        return result
