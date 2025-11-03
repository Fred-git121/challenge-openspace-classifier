from utils.file_utils import read_names_from_csv
from utils.openspace import Openspace
from utils.table import Table

def main():
    input_filepath = "new_colleagues.csv"
    output_filename = "output.csv"

    # Creates a list that contains all the colleagues names
    names = read_names_from_csv(input_filepath)

    # create an OpenSpace()
    open_space = Openspace(names)

    # assign a colleague randomly to a table
    open_space.organize_tables(names)

    # save the seat assigments to a new file
    open_space.store(output_filename)

    # display assignments in the terminal
    open_space.display_tables()

if __name__ == "__main__":
    main()