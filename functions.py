FILEPATH = 'showlist.txt'

def get_shows(filepath=FILEPATH):
    """ Reads the content of a text file and
    returns in a list
    """
    with open(filepath, 'r') as file_local:
        shows_local = file_local.readlines()
        return shows_local


def write_shows(shows_arg, filepath=FILEPATH):
    """ Writes the content of a list
    to a text file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(shows_arg)
    return

if __name__ == "__main__":
    print("I am inside")