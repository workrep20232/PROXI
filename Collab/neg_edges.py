def neg_train(pos_train, pos_val, neg_val, pos_test, neg_test, sub_graph):

    '''
    This code creates the negative edges set
    '''

    edges = list(pos_train) + list(pos_val) + list(pos_test)
    neg_edges = list(neg_val) + list(neg_test)
    all_edges = edges + neg_edges
    all_graph = nx.from_edgelist(all_edges)

    N = all_graph.number_of_nodes()
    M = sub_graph.number_of_edges()

    G = nx.Graph()

    k1 = 0
    while k1 < M:
        i = random.randint(0, N - 2)
        j = random.randint(0, N - 1)
        if i != j:
            if not all_graph.has_edge(i, j):
                if not G.has_edge(i, j):
                    G.add_edge(i, j)
                    k1 += 1

    return G