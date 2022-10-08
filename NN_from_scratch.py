#Discription:
#    Continuing my journey to learn neural networks. First attempt to build a network from scratch.
#Author:
#    Chinmay Mishra
#Date:
#    9/10/2022
from numpy import *
from sklearn.datasets import load_iris
data = load_iris()

print(f"""
    Detailed Data listing:

    Input Layer Shape:  {data['data'].shape},
    Shape Target:       {data['target'].shape},
    Target Names:       {data['target_names']}

""")

#Defining Neural Network Class:

class Iris_Neural_Network():
    def __init__(self):
        
        #Actual Target:
        self.Target = data['target']


        #Defining Hidden Layers:
        self.hiddenLayer = 16
        self.hiddenLayer_2 = 2
        self.Error = 0

        #Defining Weights:
        self.weights_0_1 = array(4,self.hiddenLayer)
        self.weights_1_2 = array(self.hiddenLayer,self.hiddenLayer_2)
        self.weights_2_3 = array(self.hiddenLayer_2,1)

    def Forward(self,Layer_0):

        #Forward Pass:
        self.layer_1 = self.ActivationRelu(dot(Layer_0,self.weights_0_1))
        self.layer_2 = self.ActivationRelu(dot(self.Layer_1,self.weights_1_2))
        self.Layer_Output = dot(self.layer_2,self.weights_2_3)

        #Passing Values to Loss Function:
        self.Loss_and_error(self.Layer_Output,self.Target)

    def ActivationRelu(self, a):
        return (a > 0) * a
    def ActivationRivRelu_2(self, a):
        return (a > 0)
    def ActivationSoftMax(self, s):
        return (exp(s)/sum(exp(s)))
    def Loss_and_error(self, Layer_Output,Target):
        
        #Calculating Loss and Error
        self.Error += (Layer_Output - Target) ** 2

    def Delta(self):
        pass
    def BackPropogation(self):
        pass
    def Learning(self):
        pass


#Initializing the variables X (Input) and Target (Output): 


