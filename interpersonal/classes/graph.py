"""
Handles the plotting of graphs
There are several types of graph in this module:
Neutral graphs are based on the absolute values of personalities.
Relative graphs are based on the values relative to a given persons's
personality.
Circle graphs are transformed so that it plots as a circle.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from .person_dao import PersonDao


def plot_neutral_graph():
    """
    Plot a graph of all Persons based on their Personality
    """
    name = []  # name
    friendliness = []  # friendliness
    dominance = []  # dominance

    for row in PersonDao.get_all():
        name.append(row[0])
        friendliness.append(row[1])
        dominance.append(row[2])

    fig, ax = plt.subplots()
    ax.scatter(friendliness, dominance)

    # set the graph to display only (-10,10)
    # since this is the maximum range of personalities
    # that we allow in our model of traits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # set the axis tick labels to be integers only
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # draw lines depicting the friendliness and dominance axes
    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')

    for i, txt in enumerate(name):
        ax.annotate(txt, (friendliness[i], dominance[i]))

    plt.xlabel('friendliness')
    plt.ylabel('dominance')

    plt.show()


def plot_graph_relative_to(name):
    """
    Plot a graph of all Persons based on their Personality
    relative to the Person of the given name.
    If there is no Person of the given name,
    a neutral graph is plotted instead.
    :param name: The name of the Person to plot the Personalities
    relative to
    """
    names = []  # names
    friendliness = []  # friendliness
    dominance = []  # dominance

    for row in PersonDao.get_all():
        names.append(row[0])
        friendliness.append(row[1])
        dominance.append(row[2])

    found = False
    n_alpha = 0

    for i in range(len(names)):
        if names[i] == name:
            found = True
            n_alpha = i
            break

    if not found:
        plot_neutral_graph()
        return

    # now plot the relative graph
    xr = []  # relative friendliness
    yr = []  # relative dominance

    def get_beta_final(alpha, beta):
        """
        Given the initial alpha and beta,
        produce the final beta.
        This works along one axes at a time
        eg friendliness or dominance axis
        :param alpha: The initial value of alpha component
        :param beta: The initial value of the beta component
        :return: The final value of the beta component
        """
        if beta == alpha:
            return 0
        elif beta == 10:
            return 10
        elif beta == -10:
            return -10
        elif alpha == -10:
            return 10 - (10 - beta) * (10 - alpha) / 10
        else:
            return 10 * (10 + beta) / (10 + alpha) - 10

    # we do not skip the alpha because
    # we happen to have a transformation from
    # point alpha to the origin
    # but if that transformation was not so
    # we would need to skip the alpha
    alpha_x = friendliness[n_alpha]
    alpha_y = dominance[n_alpha]

    for i in range(len(names)):
        xr.append(get_beta_final(alpha_x, friendliness[i]))
        yr.append(get_beta_final(alpha_y, dominance[i]))

    fig, ax = plt.subplots()
    ax.scatter(xr, yr)

    # set the graph to display only (-10,10)
    # since this is the maximum range of personalities
    # that we allow in our model of traits
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])

    # set the axis tick labels to be integers only
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    # draw lines depicting the friendliness and dominance axes
    plt.axhline(0, color='grey')
    plt.axvline(0, color='grey')

    for i, txt in enumerate(names):
        ax.annotate(txt, (xr[i], yr[i]))

    plt.xlabel('friendliness')
    plt.ylabel('dominance')

    plt.show()
