"""
main.py

DNA Sequence Converter - Command Line Interface

Provides a program that can be executed in a command-line interface for converting DNA sequences
to RNA or mRNA using the converter module.

The program prompts the user for:
    1. A DNA sequence (any string, invalid bases will be filtered).
    2. A conversion type ("rna" or "mrna").

Then displays the converted sequence.

Usage:
    python main.py

Author: Kevin K. Le
Version: 1.0.0
License: Apache 2.0
"""

from converter import dna_rna_or_mrna


def main():
    """
    Main function to run the DNA to RNA/mRNA converter.
    
    Prompts the user for a DNA sequence and conversion type, validates the input,
    performs the conversion, and displays the result.
    
    The Function:
        1. Accepts a DNA sequence from user input.
        2. Accepts a conversion type (case-insensitive: "rna" or "mrna").
        3. Validates the conversion type.
        4. Calls dna_rna_or_mrna() to perform the conversion.
        5. Displays the converted sequence.
    
    Returns:
        None: Prints output directly to console and exits after displaying result.
        
    Examples:
        User Input: "ATCG" with the conversion being "rna".
        Output: Converted Strand: 'aucg'.
        
        User Input: "ATCG" with the conversion resulting as "mrna".
        Output: Converted Strand: 'uagc'.
    """
    dna = input("> Enter a strand of DNA: ")

    if not dna:
        print("A non-empty DNA argument is required for the conversion.")
        return

    conversion = input("> Pick a conversion type — RNA / mRNA (case-insensitive): ").strip().lower()

    if conversion not in ("rna", "mrna"):
        print(f"'{conversion}' is not a valid conversion type. Please use either RNA or mRNA.")
        return

    converted = dna_rna_or_mrna(dna, conversion)

    print(f"Converted Strand: '{converted}'.")
    return

# This ensures main() runs only when the script is executed directly.
if __name__ == "__main__":
    main()
