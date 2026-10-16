import os 

def check_gc_bounds(seq: str, gc_bounds: tuple[float, float] | float) -> bool:
    """
    Check whether GC content of a sequence is within the bounds.

    Arguments:
    seq: nucleotide sequence
    gc_bounds: GC content interval in percent, (lower, upper) or a single
        number as the upper bound (the lower bound is then 0)

    Returns True if GC content is within the bounds (inclusive), else False.
    Returns False for an empty sequence.
    """
    if len(seq) == 0:
        return False
    gc_count = seq.count("G") + seq.count("C") 
    gc_percent = gc_count / len(seq) * 100
    if isinstance(gc_bounds, (int, float)):
        return gc_percent <= gc_bounds
    return gc_bounds[0] <= gc_percent <= gc_bounds[1] 

def check_length(seq: str, length_bounds: tuple[float, float] | float) -> bool:
    """
    Check whether length of a sequence is within the bounds.

    Arguments:
    seq: nucleotide sequence
    length_bounds: length interval, (lower, upper) or a single number
        as the upper bound (the lower bound is then 0)

    Returns True if the length is within the bounds (inclusive), else False.
    Returns False for an empty sequence.
    """
    if len(seq) == 0:
        return False
    length = len(seq) 
    if isinstance(length_bounds, (int, float)):
        return length <= length_bounds
    return length_bounds[0] <= length <= length_bounds[1]

def ascii_to_numbers(str_quality: str):
    """
    Convert a quality string to numeric quality scores (phred33).

    Arguments:
    str_quality: quality string of a read, one symbol per nucleotide

    Returns a list of scores: ASCII code of each symbol minus 33.
    """
    numbers = []
    for nucl in str_quality:
        numbers.append(ord(nucl)-33)
    return numbers

def check_quality_threshold(str_quality: str, quality_threshold: int | float) -> bool:
    """
    Check whether mean quality of a read is not below the threshold.

    Arguments:
    str_quality: quality string of a read (phred33)
    quality_threshold: minimal allowed mean quality

    Returns True if mean quality >= quality_threshold, else False.
    Returns False for an empty quality string.
    """
    if len(str_quality) == 0:
        return False
    numbers = ascii_to_numbers(str_quality)
    average_numbers = sum(numbers) / len(numbers)
    return average_numbers >= quality_threshold 

def make_output_path(output_fastq: str) -> str:
    """
    Build the path to the output file inside the folder "filtered".

    Creates the folder "filtered" if it does not exist.

    Arguments:
    output_fastq: name of the output file

    Returns the path "filtered/<output_fastq>".
    Raises FileExistsError if this file already exists.
    """
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)
    if os.path.isfile(output_path): 
        raise FileExistsError(f"Файл {output_path} уже существует")
    return output_path

def write_read(file, filtered_read: list):
    """
    Write one read (4 lines) to an opened file.

    Arguments:
    file: file opened for writing
    filtered_read: [name, sequence, "+" line, quality]

    Returns None.
    """
    for line in filtered_read:
        file.write(line + "\n")

def get_next_read(input_file):
    """
    Read the next read (4 lines) from an opened FASTQ file.

    Arguments:
    input_file: FASTQ file opened for reading

    Returns [name, sequence, "+" line, quality] without newline symbols,
    or None if the end of the file is reached.
    """
    name = input_file.readline().strip()
    if not name:
        return 
    seq = input_file.readline().strip()
    plus = input_file.readline().strip()
    quality = input_file.readline().strip()
    return [name, seq, plus, quality]
