import os
from configuration import configuration
from face import show_the_face


def main():
    """TODO:
        42!!!!
        https://www.geeksforgeeks.org/multithreading-python-set-1/
    """
    filename = 'configuration.mem'
    # Example usage
    if os.path.exists(filename) and os.stat(filename).st_size != 0:
        print('File exist or is not empty')
        show_the_face()
    else:
        print('File is empty')
        configuration()

main()