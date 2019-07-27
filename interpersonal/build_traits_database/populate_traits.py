"""
This script does all the heavy-lifting of setting up the
    initial databases...
topn ~ limit/5 seems a good number to ensure
    the combination of having enough traits
    yet avoiding matches that are completely irrelevant
"""

import nltk
import zipfile
from nltk.corpus import brown
from gensim.models import KeyedVectors

from tqdm import tqdm

from populate_traits_lib import *
from trait_dao import TraitDao

TraitDao.create_tables()
TraitDao.empty_tables()

# using the regular download can result in certificate problems
# which are hard to resolve without root access to computer
# but if you have root access to computers, this is the simplest way to
# download the brown corpora:
# nltk.download('brown')

print("Extracting brown corpora to directory")
zip_ref = zipfile.ZipFile('brown.zip', 'r')
# if nltk.data.path[0] fails, just try [1],[2],... and so on
# on our system we had about 10 alternative paths, eg. [0]~[9]
# you need write permissions to the path you choose
zip_ref.extractall(nltk.data.path[0])
zip_ref.close()

print("Loading GoogleNews-vectors into word2vec (~30 seconds)")
model = KeyedVectors.load_word2vec_format(
    'GoogleNews-vectors-negative300.bin.gz',
    binary=True,
    limit=500000
)

print("Extracting words from word2vec model")
friendliness = model.most_similar(
    positive=['friendly', 'affectionate', 'loving', 'kind'],
    negative=['hostile', 'hurtful', 'unfriendly', 'mean'],
    topn=100000
)
unfriendliness = model.most_similar(
    positive=['hostile', 'hurtful', 'unfriendly', 'mean'],
    negative=['friendly', 'affectionate', 'loving', 'kind'],
    topn=100000
)
dominance = model.most_similar(
    positive=['dominant', 'assertive', 'capable', 'important'],
    negative=['submissive', 'apologetic', 'meek', 'passive'],
    topn=100000
)
undominance = model.most_similar(
    positive=['submissive', 'apologetic', 'meek', 'passive'],
    negative=['dominant', 'assertive', 'capable', 'important'],
    topn=100000
)

# set of over 8000 adjectives
adjectives = {word for word, pos in brown.tagged_words()
              if pos.startswith('JJ')}

print("Filtering for adjectives from extracted words")
friendliness = filter_adjectives(friendliness, adjectives)
unfriendliness = filter_adjectives(unfriendliness, adjectives)
dominance = filter_adjectives(dominance, adjectives)
undominance = filter_adjectives(undominance, adjectives)

print("Scaling the list to fit the range (0,10) or (-10,0)")
friendliness = scale_my_list(friendliness, True)
unfriendliness = scale_my_list(unfriendliness, False)
dominance = scale_my_list(dominance, True)
undominance = scale_my_list(undominance, False)

print("Adding traits to database:")
print("- 1/4")
for trait in tqdm(friendliness):
    TraitDao.add_friendliness_trait(trait[0], trait[1])
print("- 2/4")
for trait in tqdm(unfriendliness):
    TraitDao.add_friendliness_trait(trait[0], trait[1])
print("- 3/4")
for trait in tqdm(dominance):
    TraitDao.add_dominance_trait(trait[0], trait[1])
print("- 4/4")
for trait in tqdm(undominance):
    TraitDao.add_dominance_trait(trait[0], trait[1])

print("traits.db is ready!")
