from helpers import fastq
from helpers import bio_files

def filter_fastq(input_fastq: str, 
                 output_fastq: str, 
                 gc_bounds = (0,100), 
                 length_bounds = (0, 2**32), 
                 quality_threshold = 0):
    """
    Filter reads of a fastq file by GC content, length and mean quality.
    Reads are processed one at a time: each read is checked and written
    right away, so only one read is kept in memory.

    Arguments:
    input_fastq: path to the input fastq file
    output_fastq: name of the output file; it is saved to the folder
        "filtered", which is created if it does not exist
    gc_bounds: GC content interval in percent, (lower, upper) or a single
        number as the upper bound, default (0, 100) keeps all reads
    length_bounds: read length interval, same rules as for gc_bounds,
        default (0, 2**32)
    quality_threshold: minimal mean read quality (phred33), default 0

    All bounds are inclusive.

    Returns None, writes the reads that passed all filters to the output file.
    Raises FileExistsError if the output file already exists.
    """
    output_path = fastq.make_output_path(output_fastq)
    with open(input_fastq) as input_file, open(output_path, "w") as output_file:
        while True:
            reads = fastq.get_next_read(input_file)
            if reads is None:
                break
            if fastq.check_gc_bounds(reads[1], gc_bounds):
                if fastq.check_length(reads[1], length_bounds):
                    if fastq.check_quality_threshold(reads[3], quality_threshold):
                        fastq.write_read(output_file, reads)

def convert_multiline_fasta_to_oneline(input_fasta: str, 
                                       output_fasta: str | None = None):
    """
    Rewrite a fasta file so that every sequence takes exactly one line.

    Records are processed one at a time, so only one sequence is kept
    in memory.

    Arguments:
    input_fasta: path to the input fasta file
    output_fasta: name of the output file; if None (default), the name is
        built from the input one: example.fasta -> example_oneline.fasta

    Returns None, writes the result to the output file.
    Raises FileExistsError if the output file already exists.
    """
    output_path = bio_files.make_output_path(input_fasta, output_fasta)
    with open(input_fasta) as input_file, open(output_path, "w") as output_file:
        header = input_file.readline().strip()
        while header:
            seq, next_header = bio_files.get_next_seq(input_file)
            bio_files.write_seq(output_file, [header, seq]) 
            header = next_header
