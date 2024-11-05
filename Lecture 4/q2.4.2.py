#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 19:12:30 2024
@author: andy
"""

import numpy as np
import matplotlib.pyplot as plt

P = [4, 5, 0, 2]
dPdx = []

for i, c in enumerate(P):
    dPdx.append(i*c)

print(dPdx)

#for i, c in enumerate(P[1:]):
#    dPdx.append(i*c)
#
#print(dPdx)