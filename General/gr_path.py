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
        try:
            paths1 = len(list(nx.all_simple_paths(sub_graph, source=i, target=j, cutoff=1)))
        except:
            paths1 = 0

        try:
            paths2 = len(list(nx.all_simple_paths(sub_graph, source=i, target=j, cutoff=2))) - paths1
        except:
            paths2 = 0

        try:
            paths3 = len(list(nx.all_simple_paths(sub_graph, source=i, target=j, cutoff=3))) - paths1 - paths2
        except:
            paths3 = 0

        if G.has_edge(i, j) or G.has_edge(j, i):
            label = 1
        else:
            label = 0

        file.write(name + "\t" + str(i) + "\t" + str(j) + "\t" + str(len(path) - 1) + "\t" + str(paths2)
                   + "\t" + str(paths3) + "\t" + str(label) + "\n")

    file.close()
    print('done')
    return sub_graph
