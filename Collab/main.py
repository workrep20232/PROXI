import numpy as np
import random
import networkx as nx
from collections import defaultdict
from ogb.linkproppred import LinkPropPredDataset
from neg_edges import *
from bag_of_fn import *
from database import *
import math

dataset_collab = LinkPropPredDataset(name='ogbl-collab')

split_edge = dataset_collab.get_edge_split()
train_edge, valid_edge, test_edge = split_edge["train"], split_edge["valid"], split_edge["test"]
G = dataset_collab[0]

pos_train = train_edge['edge']
pos_val = valid_edge['edge']
neg_val = valid_edge['edge_neg']
pos_test = test_edge['edge']
neg_test = test_edge['edge_neg']
node_feat = G['node_feat']
tr_years = train_edge['year']
years = np.unique(tr_years)

valp = nx.from_edgelist(pos_val)
valn = nx.from_edgelist(neg_val)
testp = nx.from_edgelist(pos_test)
testn = nx.from_edgelist(neg_test)

graph_p = nx.from_edgelist(pos_train)
N = graph_p.number_of_nodes()
M = graph_p.number_of_edges()

# collect the authors publication years
distr = {}
for J in range(N):
    distr[J] = []

for I in range(len(pos_train)):
    distr[pos_train[I][0]].append(tr_years[I])
    distr[pos_train[I][1]].append(tr_years[I])

for K in range(N):
    distr[K] = np.unique(distr[K])

auth_oldest = []
auth_newest = []
for auth in range(N):
    auth_oldest.append(auth_oldest_paper(distr, auth))
    auth_newest.append(auth_newest_paper(distr, auth))

year_index = {}
# collect the index of each link into its year
for year in years:
    year_index[year] = [index for index, value in enumerate(tr_years) if value == year]

w = train_edge['weight']

# assign to each edge the total number of collaboration up to 2017
sums = {}

for j in range(len(pos_train)):
    key = tuple(pos_train[j, :])
    if key in sums:
        sums[key] += w[j]
    else:
        sums[key] = w[j]

print('done2')

# assign to each edge the total number of collaboration from 2012 to 2017
sums_5 = {}
for y in range(2012, 2018):
    for i in year_index[y]:
        key = tuple(pos_train[i, :])
        if key in sums_5:
            sums_5[key] += w[i]
        else:
            sums_5[key] = w[i]

# assign to each edge the total number of collaboration from 2007 to 2017
sums_10 = {}
for y in range(2007, 2018):
    for i in year_index[y]:
        key = tuple(pos_train[i, :])
        if key in sums_10:
            sums_10[key] += w[i]
        else:
            sums_10[key] = w[i]
print('done3')

# assign to each node the total number of collaboration from 2007 to 2017
weights = np.zeros(N)
for edge, weight in sums_10.items():
    weights[edge[0]] += weight
    weights[edge[1]] += weight

print('done4')

gr_2007 = nx.from_edgelist(pos_train[year_index[2007], :])
gr_2008 = nx.from_edgelist(pos_train[year_index[2008], :])
gr_2009 = nx.from_edgelist(pos_train[year_index[2009], :])
gr_2010 = nx.from_edgelist(pos_train[year_index[2010], :])
gr_2011 = nx.from_edgelist(pos_train[year_index[2011], :])
gr_2012 = nx.from_edgelist(pos_train[year_index[2012], :])
gr_2013 = nx.from_edgelist(pos_train[year_index[2013], :])
gr_2014 = nx.from_edgelist(pos_train[year_index[2014], :])
gr_2015 = nx.from_edgelist(pos_train[year_index[2015], :])
gr_2016 = nx.from_edgelist(pos_train[year_index[2016], :])
gr_2017 = nx.from_edgelist(pos_train[year_index[2017], :])

# the graph obtained by combining the years from 2007 to 2017
concatenated_list = []
for year in range(2007, 2018):
    if year in year_index:
        concatenated_list.extend(year_index[year])
ngraph2007_2017 = nx.from_edgelist(pos_train[concatenated_list, :])

# the graph obtained by combining the years from 2012 to 2017
concatenated_list2 = []
for year in range(2012, 2018):
    if year in year_index:
        concatenated_list2.extend(year_index[year])
ngraph2012_2017 = nx.from_edgelist(pos_train[concatenated_list2, :])

# # the graph obtained by combining all the years up to 2017
ngraph_tr = nx.from_edgelist(pos_train)

# We assign index -1 to positive training set, index -2 to positive validation set, index -3 to negative validation set,
# index -4 to positive test set, index -5 to negative test set and indices 0-9 to negative training set


database(-1, gr_2017, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
         gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
         node_feat)

database(-2, valp, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
         gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
         node_feat)

database(-3, valn, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
         gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
         node_feat)

database(-4, testp, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
         gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
         node_feat)

database(-5, testn, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
         gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
         node_feat)

for i in range(10):
    ntraing = neg_train(pos_train, pos_val, neg_val, pos_test, neg_test, gr_2017)
    database(i, ntraing, sums, sums_5, sums_10, weights, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011,
             gr_2012, gr_2013, gr_2014, gr_2015, gr_2016, ngraph2007_2017, ngraph2012_2017, ngraph_tr, ngraph2007_2017,
             node_feat)

