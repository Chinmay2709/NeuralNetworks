import numpy as np
from bokeh.plotting import *
import math

Hidden_neurons=4
weights_0 = np.random.rand(3,Hidden_neurons)
weights_1 = np.random.rand(Hidden_neurons,1)
alpha = 0.2

def ActivationReLu(layer):
    return (layer > 0) * layer
def ActivationReLu2RIV(out):
    return out>0
streetlights = np.array([
    [1,0,1],
    [0,1,1],
    [0,0,1],
    [1,1,1],
    [0,1,1],
    [1,0,1]
])
walk_vs_stop = np.array(
    [
        [0,1,0,1,1,0]
    ]
).T
pos=0
for iteration in range(60):
    pos+=1
    error_for_all_lights=0
    for row_index in range(len(walk_vs_stop)):
        input = streetlights[row_index:row_index + 1]
        layer_0 = ActivationReLu(np.dot(input,weights_0))
        layer_1 = np.dot(layer_0,weights_1)
        error = (walk_vs_stop[row_index:row_index + 1]-layer_1) ** 2
        delta_1 = layer_1 - walk_vs_stop[row_index:row_index+1]
        delta_0 = np.dot(delta_1,weights_1.T)*ActivationReLu2RIV(layer_0)
        weights_1 -= (alpha* np.dot(layer_1,delta_1))
        weights_0 -= (alpha* np.dot(input.T,delta_0))
        print(f"""
    Position:   {pos}
    Error:      {error}
    Delta_0:    {delta_0}
    Delta_1:    {delta_1}
    Prediction: {layer_1}
    Prediction: 
        """)
