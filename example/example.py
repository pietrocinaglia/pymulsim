# -*- coding: utf-8 -*-

###
# @author: Pietro Cinaglia
# @mail: cinaglia (at) unicz (dot) it
# @github: https://github.com/pietrocinaglia
###

'''
' Example
'
' Note: PyMulSim only reports node similarities greater than 0, other are omitted.
'''

from pymulsim import PyMulSim # pip install pymulsim

## Parameters (example)
#
workspace = '{{current_folder}}' # Replace this with current folder's path
#
source_path = workspace + 'dataset/synt50_noise10.txt'
target_path = workspace + 'dataset/synt50_original.txt'
#
layer_ids = [1,2]
interlayer_ids = [3]
#
model_type = 'GIN' # GNN or GIN
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