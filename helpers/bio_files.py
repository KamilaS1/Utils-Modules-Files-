import os

def make_output_path(output_fasta: str) -> str:  
    output_path = os.path(output_fasta) 
    if os.path.isfile(output_path): 
        raise FileExistsError(f"Файл {output_path} уже существует")
    return output_path

def get_next_seq(input_file):
    line = input_file.readline().strip()
    s = ""
    while line and not line.startswith(">"):
        s += line
        line = input_file.readline().strip()
    return s, line 

def write_seq(file, filtered_read: list):
    for line in filtered_read:
        file.write(line + "\n")