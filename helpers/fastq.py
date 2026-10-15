import os 

def check_gc_bounds(seq: str, gc_bounds: tuple[float, float] | float) -> bool:
    if len(seq) == 0:
        return False
    gc_count = seq.count("G") + seq.count("C") 
    gc_percent = gc_count / len(seq) * 100
    if isinstance(gc_bounds, (int, float)):
        return gc_percent <= gc_bounds
    return gc_bounds[0] <= gc_percent <= gc_bounds[1] 

def check_length(seq: str, length_bounds: tuple[float, float] | float) -> bool:
    if len(seq) == 0:
        return False
    length = len(seq) 
    if isinstance(length_bounds, (int, float)):
        return length <= length_bounds
    return length_bounds[0] <= length <= length_bounds[1]

def ascii_to_numbers(str_quality: str):
    numbers = []
    for nucl in str_quality:
        numbers.append(ord(nucl)-33)
    return numbers

def check_quality_threshold(str_quality: str, quality_threshold: int | float) -> bool:
    if len(str_quality) == 0:
        return False
    numbers = ascii_to_numbers(str_quality)
    average_numbers = sum(numbers) / len(numbers)
    return average_numbers >= quality_threshold 

def make_output_path(output_fastq: str) -> str:
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)
    if os.path.isfile(output_path): 
        raise FileExistsError(f"Файл {output_path} уже существует")
    return output_path

def write_read(file, filtered_read: str):
    for line in filtered_read:
        file.write(line + "\n")









    

#мяу  