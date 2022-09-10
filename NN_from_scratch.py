#Discription:
#    Continuing my journey to learn neural networks. First attempt to build a network from scratch.
#Author:
#    Chinmay Mishra
#Date:
#    9/10/2022
import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()

print(data['data'].shape)

print(data['target'].shape)

print(f"""
{data['feature_names']}
{data['target_names']}
""")

