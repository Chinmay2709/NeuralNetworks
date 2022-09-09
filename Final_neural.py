#Discription:
#    This is my progress until today on Neural Networks, still a lot to learn.
#Author:
#    Chinmay Mishra
#Date:
#    9/9/2022

from numpy import *
import tensorflow as ts

print(ts.__version__)


hidden_size=4
directions = array([
    [1,1,0,0], # 0
    [0,0,1,1], # 1
    [1,0,0,1], # 2
    [0,1,1,0]  # 3
])

final = array([
    [1,0], # 0
    [0,1], # 1
    [1,1], # 2
    [0,0], # 3
    [0,1]  # 4
])

class NeuralNet:
    def __init__(self):
        self.Alpha_learning = 0.2
        self.weight_X_0 = (random.randn(4,hidden_size))
        self.weight_0_1 = (random.randn(hidden_size,2))
        self.error=0

    def ActivationRelU(self,a):
        return (a > 0) * a

    def ActivationRelU2RIV(self,a):
        return a > 0
    
    def forward(self,layer_X,Target):
        self.layer_0 = self.ActivationRelU(dot(layer_X,self.weight_X_0))
        self.layer_1 = dot(self.layer_0,self.weight_0_1)
        self.loss_and_error(self.layer_1,layer_X,Target)
        return self.layer_1

    def loss_and_error(self,layer_1,layer_X,Target):
        self.error += (layer_1-Target)**2
        self.Delta(self.layer_0,layer_1,layer_X,Target)

    def Delta(self,layer_0,layer_1,layer_X,Target):
        self.Delta_1_0 = layer_1-Target
        self.Delta_0_X = self.BackPropogation(self.Delta_1_0,layer_0,self.weight_0_1)
        self.learning(layer_X,layer_0,self.Delta_0_X,self.Delta_1_0)
        
    def BackPropogation(self,Delta_1_0,layer_0,weight_0_1):
        return (dot(Delta_1_0,weight_0_1.T) * self.ActivationRelU2RIV(layer_0))
        
    def learning(self,layer_X,layer_0,Delta_0_X,Delta_1_0):
        layer_0 = layer_0.reshape(1,4)
        Delta_1_0 = Delta_1_0.reshape(1,2)
        self.weight_0_1 -= self.Alpha_learning * dot(layer_0.T,Delta_1_0)
        self.weight_X_0 -= self.Alpha_learning * dot(layer_X.T,Delta_0_X)

L     =     0
R     =     0
D     =     0
U     =     0

Neural_run = 0
Total = 0
for ITI in range(100):
    Limit = 0
    NN = NeuralNet()
    Total+=1
    while True:
        Neural_run+=1
        Limit+=1
        Target = final[2]
        Output = NN.forward(directions[0],Target)
        
        if round(Output[0]) == 1 and round(Output[1]) == 0:
            L+=1
            break
        if round(Output[0]) == 1 and round(Output[1]) == 0:
            R+=1
            break
        if round(Output[0]) == 0 and round(Output[1]) == 0:
            D+=1
            break
        if round(Output[0]) == 1 and round(Output[1]) == 1:
            U+=1
            break
        if Limit == 60:
            break
    print("Times: ",ITI)

LEFT    = ((L/Total)*100)
RIGHT   = ((R/Total)*100)
DOWN    = ((D/Total)*100)
UP      = ((U/Total)*100)

print(f"""
        LEFT :{LEFT:>10}%
        RIGHT:{RIGHT:>10}%
        DOWN :{DOWN:>10}%
        UP   :{UP:>10}%


        Final Error: {NN.error}
        Final Output:{round(Output[0])} {round(Output[1])}
        
        NEURAL-RUN: {Neural_run} Times
        """)