def check_gc_bounds(seq: str, gc_bounds: tuple[float, float] | float) -> bool:
    if len(seq) == 0:
        return False
    gc_count = seq.count("G") + seq.count("C") 
    gc_percent = gc_count / len(seq) * 100
    if isinstance(gc_bounds, (int, float)):
        return gc_percent <= gc_bounds
    return gc_bounds[0] <= gc_percent <= gc_bounds[1] 

def check_length(seq: str, length_bounds: tuple[float, float] | float) -> bool:
    length = len(seq) 
    if isinstance(length_bounds, (int, float)):
        return length <= length_bounds
    return length_bounds[0] <= length <= length_bounds[1]

def ascii_to_numbers(seq: str):
    numbers = []
    for nucl in seq:
        numbers.append(ord(nucl)-33)
    return numbers

def check_quality_threshold(seq: str, quality_threshold: int | float):
    numbers = ascii_to_numbers(seq)
    average_numbers = sum(numbers) / len(numbers)
    return average_numbers >= quality_threshold 

    

#мяу  