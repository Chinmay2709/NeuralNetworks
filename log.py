#Discription:
#    Log.py the Neural Code for file third_neural.
#Author:
#    Chinmay Mishra
#Date:
#    Some time unknown: I started recording my coding progress late.

import numpy as np

class NeuralNetwork:
        def __init__(self):
                self.weights=np.random.randn(4,4)
                self.weights_2=np.random.randn(4,4)
        def forward(self,X,Target):
                self.INPUT=X
                print("Input: \n",X)
                print("Weights: \n",self.weights)
                self.z=np.dot(X,self.weights)
                self.a1=self.Activation_ReLU(self.z)
                print("Next Neuron:\n",self.a1)
                print("Next Weights:\n",self.weights_2)
                self.z2=np.dot(self.a1,self.weights_2)
                self.a2=self.Activation_ReLU(self.z2)
                self.o=self.sigmoid(self.a2)
                print('Target:\n',Target)
                self.OG_ERROR=self.ERROR(self.INPUT,Target)
                print('ERROR\n',self.OG_ERROR)
                return self.o
        def Activation_ReLU(self,z):
                return np.maximum(0,z)
        def sigmoid(self,s):
                return 1/(1+(np.exp(-s)))
        def ERROR(self,pred,Target):
                self.error_cal=lambda pred,Target: (pred-Target)
                self.error=self.error_cal(pred,Target)
                self.delta=pred-Target
                self.delta_weight=self.INPUT*self.delta
                self.delta_weight_2=self.INPUT*self.delta
                self.LEARN(self.delta_weight)
                return self.error_cal
        def LEARN(self,DELTA):
                self.alpha=0.
                self.weights-=(DELTA*self.alpha)
                self.weights_2-=(DELTA*self.alpha)
