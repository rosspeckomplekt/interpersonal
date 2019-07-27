"""
Initializes an empty persons database.
The persons database is used to store persons.
"""

import sqlite3

PCONN = sqlite3.connect('persons.db')
PC = PCONN.cursor()

# Here we store the mean and number (count) of each trait
#  so that we can update it over time by updating the mean
#  Example: "Bob is friendly" + "Bob is unfriendly" -> mean=0
# person            : the name of the person
# friendliness      : the mean value of friendliness traits
# dominance         : the mean value of dominance traits
# n_friendliness    : the number of friendliness traits
# n_dominance       : the number of dominance traits
PC.execute('''
CREATE TABLE IF NOT EXISTS persons(
person TEXT,
friendliness INT,
dominance INT,
n_friendliness INT,
n_dominance INT
)''')

PCONN.commit()
