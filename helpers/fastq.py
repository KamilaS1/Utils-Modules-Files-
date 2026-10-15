def check_gc_bounds(seq: str, gc_bounds: tuple[float, float] | float) -> bool:
    G_C_count = seq.count("G") + seq.count("C") 
    G_C_percent = G_C_count / len(seq) * 100
    if type(gc_bounds) is float:
        return G_C_percent <= gc_bounds
    return gc_bounds[0] <= G_C_percent <= gc_bounds[1]

seq = 'ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA'

print(check_gc_bounds(seq, (15.0, 50.0)))


#мы на вход хотим подавать последовательность нуклеотидов  