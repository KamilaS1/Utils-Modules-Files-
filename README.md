# Utils-Modules-Files

A Python package with bioinformatics utilities for working with FASTQ and FASTA files:

- **`filter_fastq`** — filters fastq reads by GC content, length and mean quality;
- **`convert_multiline_fasta_to_oneline`** — rewrites a fastа file so that every sequence takes one line.

Files are processed record by record, so only one read (or sequence) is kept in memory at a time, and large files are handled without loading them whole.

## Requirements

- Python **3.10** or newer
- No external dependencies: only the Python standard library is used

## Installation

```bash
git clone -b HW4 https://github.com/KamilaS1/Utils-Modules-Files-.git
cd Utils-Modules-Files-
```

Run your scripts from the repository root, so that `main.py` can import the `helpers` package.

## Project structure

```
Utils-Modules-Files-/
├── README.md
├── main.py               # utilities: filter_fastq, convert_multiline_fasta_to_oneline
└── helpers/
    ├── fastq.py          # helper functions for filter_fastq
    └── bio_files.py      # helper functions for the FASTA utilities
```

## Usage

### `filter_fastq`

Keeps only the reads that pass **all three** filters and saves them to the folder `filtered/` (it is created automatically).

| Argument | Default | Description |
|---|---|---|
| `input_fastq` | — | path to the input FASTQ file |
| `output_fastq` | — | name of the output file inside `filtered/` |
| `gc_bounds` | `(0, 100)` | GC content interval in percent |
| `length_bounds` | `(0, 2**32)` | read length interval |
| `quality_threshold` | `0` | minimal mean read quality (phred33) |

Bounds can be given as a tuple `(lower, upper)` or as a single number, which is treated as the upper bound (the lower bound is then 0). All bounds are inclusive. Reads with mean quality below `quality_threshold` are discarded.

### `convert_multiline_fasta_to_oneline`

| Argument | Default | Description |
|---|---|---|
| `input_fasta` | — | path to the input FASTA file |
| `output_fasta` | `None` | name of the output file; if not given, `_oneline` is added to the input name: `example.fasta` → `example_oneline.fasta` |

### Notes

- Existing files are never overwritten: if the output file already exists, the function raises `FileExistsError`. Delete the old file or choose another name.
- Every function has a docstring, so `help(filter_fastq)` shows the full description.

## Author

Kamila — [KamilaS1](https://github.com/KamilaS1)