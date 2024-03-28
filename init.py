#######################################################
#
# Change the class code on LAS Datasets
#
#######################################################

# Dependencies
import pylas
import numpy as np
import numpy_indexed as npi
from collections import Counter

# Load data
las = pylas.read('5515_56060.las')
print("Occurring class codes:")
print(np.unique(las.classification))
print(las)

# Remap Dictionary
dict_remap = {2: 1, 8: 11, 9: 11, 10: 3, 11: 10, 20: 5, 30: 6, 31: 14, 13: 9}
for key, value in dict_remap.items():
    print(key, ' : ', value)
print("All other values will not be changed!\n")

#Remap function using numpy_indexed
las.classification = npi.remap(las.classification, list(dict_remap.keys()), list(dict_remap.values()))

# Point count per class
point_count = Counter(las.classification)
for key, value in sorted(point_count.items()):
    print(key, ' : ', value)

las.write('remap.las')