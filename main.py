from helpers import fastq
from helpers import bio_files

def filter_fastq(input_fastq, 
                 output_fastq, 
                 gc_bounds = (0,100), 
                 length_bounds = (0, 2**32), 
                 quality_threshold = 0):
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
    output_path = bio_files.make_output_path(input_fasta, output_fasta)
    with open(input_fasta) as input_file, open(output_path, "w") as output_file:
        header = input_file.readline().strip()
        while header:
            seq, next_header = bio_files.get_next_seq(input_file)
            bio_files.write_seq(output_file, [header, seq]) 
            header = next_header
