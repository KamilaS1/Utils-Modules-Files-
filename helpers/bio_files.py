import os

def make_output_path(input_fasta: str, output_fasta: str | None) -> str:
    """
    Choose the output file name and check that this file does not exist.

    Arguments:
    input_fasta: path to the input fasta file
    output_fasta: name of the output file or None

    Returns output_fasta, or, if it is None, the input path with "_oneline"
    added before the extension: example.fasta -> example_oneline.fasta.
    Raises FileExistsError if the output file already exists.
    """
    if output_fasta is None:
        name, extension = os.path.splitext(input_fasta)
        output_fasta = name + "_oneline" + extension
    output_path = output_fasta 
    if os.path.isfile(output_path): 
        raise FileExistsError(f"Файл {output_path} уже существует")
    return output_path

def get_next_seq(input_file):
    """
    Read one sequence from an opened fasta file and join it into one line.

    The header of the record must be already read. Lines are read until
    the next header (a line starting with ">") or the end of the file.

    Arguments:
    input_file: fasta file opened for reading

    Returns a tuple (sequence, next_header).
    next_header is an empty string at the end of the file.
    """
    line = input_file.readline()
    s = ""
    while line and not line.startswith(">"):
        s += line.strip()
        line = input_file.readline()
    return s, line.strip()

def write_seq(file, filtered_read: list):
    """
    Write a fasta record (header and sequence) to an opened file.

    Arguments:
    file: file opened for writing
    filtered_read: [header, sequence]

    Returns None.
    """
    for line in filtered_read:
        file.write(line + "\n")