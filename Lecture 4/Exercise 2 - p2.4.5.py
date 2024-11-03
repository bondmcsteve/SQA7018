#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:57:42 2024

@author: andy
"""

# For example, for the sequence "AGTCTTATATCT":

# Frame 0 gives codons: AGT, CTT, ATA, TCT
# Frame 1 gives codons: GTC, TTA, TAT
# Frame 2 gives codons: TCT, TAT, ATC

# Given DNA sequence and frame
sequence = "AGTCTTATATCT"
frame = 0  # Can be 0, 1, or 2

# Extract codons starting from the given frame
codons = []
for i in range(frame, len(sequence) - 2, 3):
    codons.append(sequence[i:i+3])

# Output the extracted codons
print(codons)  # This will output the list of codons for the given frame
