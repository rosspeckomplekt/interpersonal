"""
Trait Database Access Object
The class for accessing the Traits Database
"""

import sqlite3


class TraitDao(object):
    """
    Trait Database Access Object
    The class for accessing the Traits Database
    """

    def __init__(self):
        """
        Initialize the Trait Database Access Object
        """

    def print_traits_db(self):
        """
        Print all Traits in the traits database
        """
        print("Friendliness DB:")
        for row in self.get_all_friendliness():
            print(row)
        print("Dominance DB:")
        for row in self.get_all_dominance():
            print(row)

    @staticmethod
    def create_tables():
        """
        Create the tables for the Trait Database
        """
        tconn = sqlite3.connect('traits.db')
        tc = tconn.cursor()

        tc.execute('''
        CREATE TABLE IF NOT EXISTS friendliness(
        trait TEXT,
        friendliness INT
        )''')

        tc.execute('''
        CREATE TABLE IF NOT EXISTS dominance(
        trait TEXT,
        dominance INT
        )''')

        tc.close()
        tconn.commit()
        tconn.close()

    @staticmethod
    def empty_tables():
        """
        Empty the tables in the Trait Database
        """
        tconn = sqlite3.connect('traits.db')
        tc = tconn.cursor()

        tc.execute('DELETE FROM friendliness')
        tc.execute('DELETE FROM dominance')

        tc.close()
        tconn.commit()
        tconn.close()

    @staticmethod
    def add_friendliness_trait(trait_name, friendliness_value):
        tconn = sqlite3.connect('traits.db')
        tc = tconn.cursor()

        tc.execute('INSERT INTO friendliness VALUES (?, ?)',
                   (trait_name, friendliness_value))

        tc.close()
        tconn.commit()
        tconn.close()

    @staticmethod
    def add_dominance_trait(trait_name, dominance_value):
        tconn = sqlite3.connect('traits.db')
        tc = tconn.cursor()

        tc.execute('INSERT INTO dominance VALUES (?, ?)',
                   (trait_name, dominance_value))

        tc.close()
        tconn.commit()
        tconn.close()

    @staticmethod
    def get_all_friendliness():
        """
        Get all values of friendliness as a cursor
        :return: Iterable cursor to all values of friendliness
        """
        tconn = sqlite3.connect('traits.db', timeout=5)
        tc = tconn.cursor()
        tc.execute('SELECT * FROM friendliness')
        result = tc.fetchall()
        tc.close()
        tconn.close()
        return result

    @staticmethod
    def get_all_dominance():
        """
        Get all values of dominance as a cursor
        :return: Iterable cursor to all values of dominance
        """
        tconn = sqlite3.connect('traits.db', timeout=5)
        tc = tconn.cursor()
        tc.execute('SELECT * FROM dominance')
        result = tc.fetchall()
        tc.close()
        tconn.close()
        return result

    @staticmethod
    def get_friendliness(name):
        """
        Get the friendliness value for a given trait
        :param name: The name of a trait
        :return: The friendliness value for the given trait
        """
        tconn = sqlite3.connect('traits.db', timeout=5)
        tc = tconn.cursor()
        tc.execute('SELECT * FROM friendliness WHERE trait=?', (name,))
        result = tc.fetchone()
        tc.close()
        tconn.close()
        return result

    @staticmethod
    def get_dominance(name):
        """
        Get the dominance value for a given trait
        :param name: The name of a trait
        :return: The dominance value for the given trait
        """
        tconn = sqlite3.connect('traits.db', timeout=5)
        tc = tconn.cursor()
        tc.execute('SELECT * FROM dominance WHERE trait=?', (name,))
        result = tc.fetchone()
        tc.close()
        tconn.close()
        return result
