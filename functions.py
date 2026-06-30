FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Read the to-do items from the text file
    and return them as a list.
    """
    with open(file_path, "r") as file:
        todos_local = file.readlines()

    return todos_local


def write_todos(todos_arg, file_path=FILEPATH):
    """
    Write the list of to-do items to the text file.
    """
    with open(file_path, "w") as file:
        file.writelines(todos_arg)
