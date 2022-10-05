#Discription:
#    Another attempt to make a neural network. It is an incomplete neural network.
#Author:
#    Chinmay Mishra
#Date:
#    Some time unknown: I started recording my coding progress late.

from bokeh.plotting import *
import numpy as np   
goal=[10,2,3]
i=0
j=0
weight_delta_plot=[]
weight_plot=[]
error_plot=[]
input=[2.35,3.45,1.45]
class SimpleNeural:
    def __init__(self):
        self.weight=[[0.1,0.2,0.1],
                     [0.45,0.21,0.31],
                     [0.33,0.12,0.1]]
        self.Alpha=0.00000001
        self.pred=[0,0,0]
        self.error=[0,0,0]
        self.DELTA=[0,0,0]
    def forward(self,input):
        assert(len(input)==len(self.weight))
        for i in range(len(input)):
            for j in range(len(self.weight[0])):
                self.pred[i] += input[i]*self.weight[i][j]
        self.Compare_learn(input)
        return self.pred
    def Compare_learn(self,input):
        self.weight_delta=[[0,0,0],
                           [0,0,0],
                           [0,0,0]]
        for e in range(len(self.error)):
            self.error[e] = (self.pred[e]-goal[e]) ** 2
            self.DELTA[e] = (self.pred[e]-goal[e])
        for i in range(len(input)):
            for j in range(len(input)):
                self.weight_delta[i][j] = input[i]*self.DELTA[j]
        for i in range(len(input)):
            error_plot.append(self.error[i])
            for learn in range(len(input)):
                self.weight[i][learn] -= self.Alpha*self.weight_delta[i][learn]
        weight_delta_plot.append(self.weight_delta[0][0])
        weight_plot.append(self.weight[0][0])
        error_plot.append(self.error[0])
        print(f"""
Error:      {self.error}
Prediction: {self.pred}
DELTA:      {self.DELTA}
Weight DELTA:{self.weight_delta}
Weight:{self.weight}
        """)
        # Hot & Cold Learning
        # self.p_up=input*(self.weight+self.learn)
        # self.p_down=input*(self.weight-self.learn)
        # self.e_up=(self.p_up-self.goal) ** 2
        # self.e_down=(self.p_down-self.goal) ** 2
        # if self.error>self.e_up or self.error>self.e_down:
        #     if self.e_up>self.e_down:
        #         self.weight-=self.learn
        #     if self.e_down>self.e_up:
        #         self.weight+=self.learn
SN = SimpleNeural()
while True:
    i+=1
    pred=SN.forward(input)
    if pred==goal:
        j+=1
    if i==10000:
        break
graph=figure(title="Brain"+' '+str(SN.Alpha)+' '+str(j))
graph.line(weight_delta_plot,error_plot,color='black')
graph.line(weight_plot,error_plot,color='lightgreen')
show(graph)
#     pred=SN.forward(input)
#     print('Prediction: ',pred)