"""
Library for the functions used in populate_traits.py
"""


def is_adjective(word, adjectives):
    """
    Check whether the given word is an adjective or not
    :param word: the input word
    :param adjectives: list of all adjectives in the English language
    :return: True if the word is an adjective, False otherwise
    """
    if word in adjectives:
        return True
    else:
        return False


def filter_adjectives(a_list, adjectives):
    """
    Filter the list of words to find the adjectives in it
    :param a_list: A list of words
    :param adjectives: The list of adjectives
    :return: A list of all adjectives that were in the input list
    """
    found = []
    i = 0
    while i < len(a_list):
        if is_adjective(a_list[i][0], adjectives):
            found.append(a_list[i])
        i += 1
    return found


def scale_min_max(x, xmin, xmax, ymin, ymax):
    """
    scales input into integer output range
    :param x: the input value to transform
    :param xmin: the minimum input range
    :param xmax: the maximum input range
    :param ymin: the minimum output range
    :param ymax: the maximum output range
    :return: the scaled output value
    """
    y = (x - xmin) / (xmax - xmin)
    y *= (ymax - ymin)
    y += ymin
    y = int(y)
    return y


def scale_my_list(list, positivity):
    """
    Scale a list

    Example input :
        [('warm_hearted', 0.43241143226623535),
        ('playful', 0.3962867259979248),...
    Example output:
        [['warm_hearted', 11],
        ['playful', 7]

    :param list: the list to scale
    :param positivity: True if friendliness or dominance,
    False otherwise
    :return: the scaled list
    """
    if positivity:
        multiplier = 1
    else:
        multiplier = -1
    i = 0
    min = 1
    while i < len(list):
        if list[i][1] < min:
            min = list[i][1]
        i += 1
    i = 0
    max = 0
    while i < len(list):
        if list[i][1] > max:
            max = list[i][1]
        i += 1
    i = 0
    list2 = []
    while i < len(list):
        new = [list[i][0],
               multiplier * scale_min_max(list[i][1], min, max, 1, 10)]
        list2.append(new)
        i += 1
    return list2
