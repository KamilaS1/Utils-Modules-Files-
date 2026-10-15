from helpers import fastq

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
    output_file.close()
    input_file.close()