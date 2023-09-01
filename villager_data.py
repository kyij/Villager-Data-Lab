"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    unique_species = set()
    file = open(filename)
    for line in file:
        species = line.rstrip().split("|")[1]
        unique_species.add(species)

    # TODO: replace this with your code

    return unique_species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """


    villagers = []
    file = open(filename)
    for line in file:
        name = line.rstrip().split("|")[0]
        species = line.rstrip().split("|")[1]
        if search_string in ("All", species):
            villagers.append(name)
   
    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    fitness = []
    nature = []
    education = []
    music = []
    fashion = []
    play = []

    file = open(filename)

    
    for line in file:

        name, _, _, hobby, _ = line.rstrip().split("|")

        if hobby == 'Fitness':
            fitness.append(name)
        elif hobby == 'Nature':
            nature.append(name)
        elif hobby == 'Education':
            education.append(name)
        elif hobby == 'Music':
            music.append(name)
        elif hobby == 'Fashion':
            fashion.append(name)
        elif hobby == 'play':
            play.append(name)



    return [sorted(fitness), 
            sorted(nature), sorted(education), 
            sorted(music), sorted(fashion), sorted(play)]


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []
    file = open(filename)
    for line in file:
        all_data.append(tuple(line.rstrip().split("|")))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    for name, _, _, _, motto in all_data(filename):
        if name == villager_name:
            return motto

def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    same_personality =set()
    wanted_personality = ' '
    for villager_data in all_data(filename):
        name,_,personality = villager_data[0:3]

        if name == villager_name:
            wanted_personality = personality
            break

    if wanted_personality:
        for villager_data in all_data(filename):
            name,_,personality = villager_data[0:3]
            if personality == wanted_personality:
                same_personality.add(name)
    return (same_personality)

            



print(all_species("villagers.csv"))
print(get_villagers_by_species("villagers.csv", search_string="All"))
print(all_names_by_hobby("villagers.csv"))
print(all_data("villagers.csv"))
print(find_motto("villagers.csv", villager_name))
print(find_likeminded_villagers("villagers.csv", villager_name))