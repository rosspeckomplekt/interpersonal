"""
Library containing assorted functions that do not fit in regular classes
"""

from .company import Company


def get_our_present(their_past, their_future):
    """
    Predicts the present style of speech we should use
    to influence a other person who is currently in
    their_past to become their_future
    :param their_past: the past of the other person
    :param their_future: the desired future of the other person
    :return: the present style we should use
    """
    if their_past * their_future < 0:
        return -10
    else:
        return 10


def suggest_contact(description):
    """
    suggests a contact for a given situation
    :param description: the description of the situation
    :return: the suggested contact
    """
    company = Company("default")
    company.find_description(description)
