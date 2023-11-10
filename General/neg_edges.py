def neg_set(m, N, M, edges):

    '''
    This code creates the negative edges set
    '''

    edges = edges.tolist()
    graph = nx.from_edgelist(edges)
    G = nx.Graph()

    k1 = 0
    while k1 < M:
        i = random.choice(N)
        j = random.choice(N)
        if i != j:
            if not graph.has_edge(i, j):
                if not G.has_edge(i, j):
                    G.add_edge(i, j)
                    k1 += 1

    neg_edges = G.edges()

    all_edges = edges + list(neg_edges)

    print(len(all_edges))

    return all_edges
