def count_simple_paths_for_edge(adj_matrix, u, v):
    n = len(adj_matrix)
    
    # Directly find neighbors of u and v
    neighbors_u = [x for x in range(n) if adj_matrix[u][x] == 1 and x != v]
    neighbors_v = [y for y in range(n) if adj_matrix[v][y] == 1 and y != u]
    
    # Count pairs (x, y) where A[x][y] == 1
    count_3paths = sum(1 for x in neighbors_u for y in neighbors_v if adj_matrix[x][y] == 1)
    count_2paths = sum(1 for x in neighbors_u if adj_matrix[x][v] == 1)
    
    return count_2paths, count_3paths





def gr_paths(m, sub_graph, all_edges, G):

    '''
    In this code short path length, number of 2-paths, number of 3-paths and label is found and saved in a file
    '''


    name = 'Citeseer'
    file = open(name + '_spath' + str(m) + '.csv', 'w')
    file.write(
        'dataset' + "\t" + 'u' + "\t" + 'v' + "\t" + 'short path length' + "\t" + 'nr of 2paths' + "\t" + 'nr of 3paths' + "\t" + "label" + "\n")

    for k in all_edges:
        i = k[0]
        j = k[1]
        if sub_graph.has_edge(i, j):
            sub_graph.remove_edge(i, j)
            try:
                path = nx.shortest_path(sub_graph, i, j)
            except:
                path = [0]
            sub_graph.add_edge(i, j)

        else:
            try:
                path = nx.shortest_path(sub_graph, i, j)
            except:
                path = [0]
        paths2, paths3 = count_simple_paths_for_edge(A, i, j)

        if G.has_edge(i, j) or G.has_edge(j, i):
            label = 1
        else:
            label = 0

        file.write(name + "\t" + str(i) + "\t" + str(j) + "\t" + str(len(path) - 1) + "\t" + str(paths2)
                   + "\t" + str(paths3) + "\t" + str(label) + "\n")

    file.close()
    print('done')
    return sub_graph
