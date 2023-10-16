# -*- coding: utf-8 -*-

'''
' Example
'
' Note: PyMulSim only reports node similarities greater than 0, other are omitted.
'''

from pymulsim import PyMulSim # pip install pymulsim

## Parameters (example)
#
workspace = './' # Replace with current folder's path
#
source_path = workspace + 'dataset/synt50_1.txt'
target_path = workspace + 'dataset/synt50_1.txt'
#
layer_ids = [1,2]
interlayer_ids = [3]
#
model_type = 'GNN' # GNN or GIN
channels = 64
epochs = 0
verbose = True # True: verbose; False: does not show information during computation.
#

## PyMulSim
pymulsim = PyMulSim()

## Computing similarities from file (networkx is also supported, see the official repository for help).
sims = pymulsim.compute_similarities_from_file(source_path, target_path, layer_ids, interlayer_ids, model_type, channels, epochs, verbose)

# Print result
print(sims)