"""
Person Database Access Object
The class for accessing the Persons Database
"""

import sqlite3


class PersonDao(object):
    """
    Person Database Access Object
    The class for accessing the Persons Database
    """

    def __init__(self):
        """
        Initialize the Person Database Access Object
        """

    def print_persons_db(self):
        """
        Print all Persons in the persons database
        """
        print("Persons DB:")
        for row in self.get_all():
            print(row)

    @staticmethod
    def get_all():
        """
        Get all persons
        :return: All persons
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('SELECT * FROM persons')
        result = pc.fetchall()
        pc.close()
        pconn.close()
        return result

    @staticmethod
    def get(name):
        """
        Get the person with the given name
        :param name: The name of the person
        :return: The person with the given name
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('SELECT * FROM persons WHERE person=?', (name,))
        result = pc.fetchone()
        pc.close()
        pconn.close()
        return result

    @staticmethod
    def insert(name):
        """
        Add an entry to the persons database with the given name
        :param name: The name of the person to add to the database
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('INSERT INTO persons VALUES (?, ?, ?, ?, ?)',
                   (name, 0, 0, 0, 0))
        pc.close()
        pconn.commit()
        pconn.close()

    @staticmethod
    def set_friendliness(name, friendliness):
        """
        Set the value of friendliness for the person with the given name
        :param name: The name of the person
        :param friendliness: The value of friendliness to set for the person
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('UPDATE persons SET friendliness=? WHERE person=?',
                   (friendliness, name))
        pc.close()
        pconn.commit()
        pconn.close()

    @staticmethod
    def set_n_friendliness(name, n_friendliness):
        """
        Set the value of n_friendliness for the person with the given name
        :param name: The name of the person
        :param n_friendliness: The value of n_friendliness to set for the person
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('UPDATE persons SET n_friendliness=? WHERE person=?',
                   (n_friendliness, name))
        pc.close()
        pconn.commit()
        pconn.close()

    @staticmethod
    def set_dominance(name, dominance):
        """
        Set the value of dominance for the person with the given name
        :param name: The name of the person
        :param dominance: The value of dominance to set for the person
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('UPDATE persons SET dominance=? WHERE person=?',
                   (dominance, name))
        pc.close()
        pconn.commit()
        pconn.close()

    @staticmethod
    def set_n_dominance(name, n_dominance):
        """
        Set the value of n_dominance for the person with the given name
        :param name: The name of the person
        :param n_dominance: The value of n_dominance to set for the person
        """
        pconn = sqlite3.connect('persons.db', timeout=5)
        pc = pconn.cursor()
        pc.execute('UPDATE persons SET n_dominance=? WHERE person=?',
                   (n_dominance, name))
        pc.close()
        pconn.commit()
        pconn.close()
