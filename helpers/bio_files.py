import os

def make_output_path(input_fasta: str, output_fasta: str | None) -> str:
    if output_fasta is None:
        name, extension = os.path.splitext(input_fasta)
        output_fasta = name + "_oneline" + extension
    output_path = output_fasta 
    if os.path.isfile(output_path): 
        raise FileExistsError(f"Файл {output_path} уже существует")
    return output_path

def get_next_seq(input_file):
    line = input_file.readline()
    s = ""
    while line and not line.startswith(">"):
        s += line.strip()
        line = input_file.readline()
    return s, line.strip()

def write_seq(file, filtered_read: list):
    for line in filtered_read:
        file.write(line + "\n")