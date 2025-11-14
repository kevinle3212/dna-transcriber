# DNA to RNA/mRNA Converter

![DNA Icon](assets/img/dna-rna-mrna-transcriber.png)

## DNA to RNA/mRNA Converter (dna-transcriber)

A simple Python tool for converting DNA sequences into RNA or mRNA strands.

## Description

This project provides functionality to convert DNA sequences using two different methods:

- **RNA Conversion**: Direct transcription where thymine (T) is replaced with uracil (U).
- **mRNA Conversion**: Complementary mRNA strand using base pairing rules (A↔U, T↔A, C↔G, G↔C).

The converter handles case-insensitive input and automatically filters out invalid bases.

## Features

- ✅ Convert DNA to RNA (direct transcription).
- ✅ Convert DNA to mRNA (complementary strand).
- ✅ Case-insensitive input handling.
- ✅ Automatic filtering of invalid bases.
- ✅ Error handling for invalid input.
- ✅ Simple command-line interface.

## Core Project Structure

```md
dna-converter/
├── converter.py          # Core conversion logic.
├── main.py              # Executable Python file for a command-line interface.
├── LICENSE              # Apache 2.0 License.
└── README.md           # This file, information about the project.
```

## Requirements

- Requires Python 3.6 or newer (tested on 3.8+).
- No external dependencies required.

## Installation

a. Clone this repository:

```bash
git clone https://github.com/yourusername/dna-converter.git
cd dna-converter
```

b. No additional installation needed - it's ready to run!

## Usage

### Command-Line Interface

Run the interactive script:

```bash
python main.py
```

**Example:**

```py
> Enter a strand of DNA: ATCG
> Provide a conversion type (RNA/mRNA): rna
Converted Strand: 'aucg'.
```

### As a Python Module

You can also import and use the converter in your own Python scripts:

```python
from converter import dna_rna_or_mrna

# Convert to RNA.
rna = dna_rna_or_mrna("ATCG", "rna")
print(rna)  # Output: aucg

# Convert to mRNA.
mrna = dna_rna_or_mrna("ATCG", "mrna")
print(mrna)  # Output: uagc
```

## Examples

### DNA to RNA Conversion

```python
>>> dna_rna_or_mrna("ATCG", "rna")
'aucg'

>>> dna_rna_or_mrna("TTTTAAAA", "rna")
'uuuuaaaa'
```

### DNA to mRNA Conversion

```python
>>> dna_rna_or_mrna("ATCG", "mrna")
'uagc'

>>> dna_rna_or_mrna("AAAA", "mrna")
'uuuu'
```

### Handling Invalid Bases

```python
>>> dna_rna_or_mrna("ATXCG", "rna")  # 'X' is filtered out.
'aucg'

>>> dna_rna_or_mrna("XYZ", "rna")  # No valid bases.
"'xyz' has no valid bases. Please try again."
```

## How It Works

### RNA Conversion

RNA conversion performs direct transcription:

- Adenine (A) → Adenine (A)
- Thymine (T) → Uracil (U)
- Cytosine (C) → Cytosine (C)
- Guanine (G) → Guanine (G)

### mRNA Conversion

mRNA conversion creates the complementary strand:

- Adenine (A) → Uracil (U)
- Thymine (T) → Adenine (A)
- Cytosine (C) → Guanine (G)
- Guanine (G) → Cytosine (C)

## API Reference

### `dna_rna_or_mrna(dna, conversion, valid_bases="atcg")`

Convert a DNA sequence to RNA or mRNA.

**Parameters:**

- `dna` (str): DNA sequence string to convert (case-insensitive).
- `conversion` (Literal["rna", "mrna"]): Type of conversion.
  - `"rna"`: Direct transcription (T → U).
  - `"mrna"`: Complementary mRNA strand.
- `valid_bases` (str, optional): Valid DNA base characters (default: "atcg").

**Returns:**

- `str`: Converted sequence (lowercase), or error message if no valid bases found.

**Example:**

```python
dna_rna_or_mrna("ATCG", "rna")  # Returns: 'aucg'.
```

## Testing

You can manually test the converter using the CLI or import the module in Python and try example sequences. All invalid characters are automatically filtered.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Author

### Kevin K. Le

## Acknowledgments

- Based on basic fundamental molecular biology concepts of DNA transcription.
- Built as a learning project for Python development.

---
