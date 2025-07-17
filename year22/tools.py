import os


def read_strings_from_file(filepath: str):
    """
    Reads a text (.txt) file and returns a list of strings,
    with trailing newlines removed.
    :param filepath: Name of text file.
    :return: List[str]: list of lines as strings.
    """

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, 'inputs\\' + filepath)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding='utf-8') as file:
        lines = [line.strip() for line in file]

    return lines
