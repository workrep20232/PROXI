import torch
from torch_geometric.datasets import Planetoid
import scipy.sparse as sp
import networkx as nx
import random
import numpy as np
import pandas as pd
from pos_part import *
from neg_edges import *
from bag_of_fn import *
from gr_path import *
from database import *

# Download the Citeseer dataset
dataset = Planetoid(root='/tmp/citeseer', name='Citeseer')

# Extract the graph from the dataset
edge_index = dataset.data.edge_index.t().tolist()
graph = nx.from_edgelist(edge_index)
edges = np.array(list(graph.edges))

# Print the number of nodes and edges
print('Number of nodes:', graph.number_of_nodes())
print('Number of edges:', graph.number_of_edges())

n = graph.number_of_nodes()
m = graph.number_of_edges()
nodes = list(graph.nodes())

x = dataset[0].x
y = dataset[0].y
Y = y.numpy()
X = x.numpy()

keyword = {}
for i in range(max(nodes) + 1):
    keyword[i] = np.nonzero(X[i, :])
    keyword[i] = np.array(keyword[i])

for l in range(10):
    print(l)
    pos_partition(l, m)
    Edges = neg_set(l, nodes, m, edges)

    pos_train_ind = np.array(pd.read_csv('train_pos_index' + str(l) + '.csv'))[:, 1:]
    train_edges = np.squeeze(edges[sorted(pos_train_ind)])
    sub_graph = nx.from_edgelist(train_edges.tolist())

    gr_paths(l, sub_graph, Edges, graph)
    database(l, keyword, Y, sub_graph)


