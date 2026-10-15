from helpers import fastq

def filter_fastq(input_fastq, 
                 output_fastq, 
                 gc_bounds = (0,100), 
                 length_bounds = (0, 2**32), 
                 quality_threshold = 0):
    output_path = fastq.prepare_output_path(output_fastq)
    output_file = open(output_path, "w")
    input_file = open(input_fastq)
    all_lines = input_file.readlines()
    for i in range(len(all_lines)):
        reads = []
        if all_lines[i].startswith("@"):
            reads = all_lines[i:i+4]
            if fastq.check_gc_bounds(reads[1], gc_bounds):
                if fastq.check_length(reads[1], length_bounds):
                    if fastq.check_quality_threshold(reads[3], quality_threshold):
                        fastq.write_read(output_file, reads)
    output_file.close()
    input_file.close()