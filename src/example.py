# -*- coding: utf-8 -*-

from pymulsim import PyMulSim

##
# Parameters
##
#
workspace = '/Users/imorph/Library/Mobile Documents/com~apple~CloudDocs/Progetti/pyMulSim/'
#
source_path = workspace + 'dataset/synt50_1.txt'
target_path = workspace + 'dataset/synt50_1.txt'
#
layer_ids = [1,2]
interlayer_ids = [3]
#
model_type = 'GIN'
channels = 64
epochs = 0
verbose = False
#
##
# Testing
##
pymulsim = PyMulSim()
sims = pymulsim.compute_similarities_from_file(source_path, target_path, layer_ids, interlayer_ids, model_type, channels, epochs, verbose)
print(sims)