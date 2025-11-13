"""
converter.py

DNA to RNA/mRNA Converter

This module provides functionality to convert DNA sequences into RNA or mRNA sequences.

DNA transcription can produce:
- RNA: Direct transcription where thymine (T) is replaced with uracil (U).
- mRNA: Complementary mRNA strand using base pairing rules (A↔U, T↔A, C↔G, G↔C).

The module handles case-insensitive inputs and filters out invalid bases automatically.

Functions:
    dna_rna_or_mrna(dna: str, conversion: Literal["rna", "mrna"], valid_bases: str = "atcg") -> str
        Converts a DNA sequence to either RNA or mRNA format.

Examples:
    >>> from converter import dna_rna_or_mrna
    >>> dna_rna_or_mrna("atcg", "rna")
    'aucg'
    >>> dna_rna_or_mrna("AtCg", "mrna")
    'uagc'
    >>> dna_rna_or_mrna("ATXCG", "rna")  # Invalid base 'X' filtered out.
    'aucg'

Notes:
    - All input DNA sequences and bases are converted to lowercase before processing.
    - Inputs are all case-insensitive.
    - Invalid bases (not in valid_bases parameter) are silently filtered out.
    - Returns an error message string if no valid bases remain after filtering.
    - Output sequences are always in lowercase.

Author: Kevin K. Le
Version: 1.0.0
License: Apache 2.0
"""

from typing import Literal


MRNA_TRANSCRIPTION = {
    "a": "u",
    "t": "a",
    "c": "g",
    "g": "c"
}

def dna_rna_or_mrna(dna: str, conversion: Literal["rna", "mrna"], valid_bases: str = "atcg") -> str:
    """
    Convert a DNA sequence to RNA or mRNA.
    
    Args:
        dna: DNA sequence string to convert (case-insensitive).
        conversion: Type of conversion - "rna" for direct transcription
                        or "mrna" for complementary mRNA strand.
        valid_bases: String of valid base characters (default: "atcg").
    
    Returns:
        str: Converted sequence (RNA or mRNA), or an error message if no valid bases were found.
        
    Examples:
        >>> dna_rna_or_mrna("ATCG", "rna")
        'aucg'
        >>> dna_rna_or_mrna("aTcG", "mrna")
        'uagc'
    """
    dna = dna.strip().lower()
    valid_bases = valid_bases.strip().lower()

    filtered_dna = "".join(char for char in dna if char in valid_bases)

    if not filtered_dna:
        return f"'{dna}' has no valid bases. Please try again."

    if conversion == "mrna":
        mrna = "".join(MRNA_TRANSCRIPTION[strand] for strand in filtered_dna)

        return mrna

    rna = filtered_dna.replace("t", "u")

    return rna
