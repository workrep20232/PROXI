import math
from bag_of_fn import *

def database(m, cons_graph, sums, sums_5, sums_10, num, gr_2007, gr_2008, gr_2009, gr_2010, gr_2011, gr_2012,
             gr_2013, gr_2014, gr_2015, gr_2016, ngraph, ngraph_5, ngraph_all, sub_graph, node_feat):
    '''
    In this code the feature vectors are computed and saved
    '''

    name = 'Collab'
    file = open( name + '_database' + str(m) + '.csv', 'w')
    file.write('dataset' + "\t" + 'u' + "\t" + 'v' + "\t"
               + 'i oldest paper' + "\t" + 'j oldest paper' + "\t" + 'i newest paper' + "\t"
               + 'j newest paper' + "\t" + 'all time coauthored' + "\t" + 'last 10 years coauthored'
               + "\t" + 'last 5 years coauthored' + "\t" + 'common collab all time'
               + "\t" + 'common collab last 10' + "\t" + 'common collab last 5'
               + "\t" + 'Preferential Attachment' + "\t" + 'w-adamic_adar' + "\t"
               + 'w-Jaccard' + "\t" + 'w-Salton' + "\t" + 'shortest path'
               + "\t" + 'cos' + "\t" + 'similar word emb' + "\t" + 'l1 dist'
               + "\t" + 'label 2007' + "\t"
               + "label 2008" + "\t" + "label 2009" + "\t" + 'label 2010' + "\t" + 'label 2011' + "\t" + 'label 2012'
               + "\t" + 'label 2013' + "\t" + 'label 2014' + "\t" + 'label 2015' + "\t" + 'label 2016'
               + "\t" + "label" + "\n")

    edges = list(cons_graph.edges())

    for k in edges:
        i, j = k

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

        old_i = oldest_paper_index(auth_oldest, i)
        old_j = oldest_paper_index(auth_oldest, j)
        new_i = newest_paper_index(auth_newest, i)
        new_j = newest_paper_index(auth_newest, j)

        coauth_all = coauth(k, sums)
        coauth_5 = coauth(k, sums_5)
        coauth_10 = coauth(k, sums_10)

        com_collab_5 = common_collab(i, j, ngraph_5)
        com_collab_10 = common_collab(i, j, ngraph)
        com_collab_all = common_collab(i, j, ngraph_all)

        pa = PA(i, j, num)
        M = w_adamic_adar(i, j, num, ngraph)
        w_jacc = jaccard_weight(ngraph, i, j, sums)
        w_salton = salton_weight(ngraph, i, j, num)

        label_2007 = label = 1 if gr_2007.has_edge(i, j) or gr_2007.has_edge(j, i) else 0
        label_2008 = label = 1 if gr_2008.has_edge(i, j) or gr_2008.has_edge(j, i) else 0
        label_2009 = label = 1 if gr_2009.has_edge(i, j) or gr_2009.has_edge(j, i) else 0
        label_2010 = label = 1 if gr_2010.has_edge(i, j) or gr_2010.has_edge(j, i) else 0
        label_2011 = label = 1 if gr_2011.has_edge(i, j) or gr_2011.has_edge(j, i) else 0
        label_2012 = label = 1 if gr_2012.has_edge(i, j) or gr_2012.has_edge(j, i) else 0
        label_2013 = label = 1 if gr_2013.has_edge(i, j) or gr_2013.has_edge(j, i) else 0
        label_2014 = label = 1 if gr_2014.has_edge(i, j) or gr_2014.has_edge(j, i) else 0
        label_2015 = label = 1 if gr_2015.has_edge(i, j) or gr_2015.has_edge(j, i) else 0
        label_2016 = label = 1 if gr_2016.has_edge(i, j) or gr_2016.has_edge(j, i) else 0

        U = node_feat[i]
        V = node_feat[j]

        matching_count = sum(x == y for x, y in zip(U, V))
        distance = sum(abs(x - y) for x, y in zip(U, V))
        C = cosine_similarity(U, V)

        if m in [-1, -2, -4]:
            label = 1
        else:
            label = 0

        file.write(name + "\t" + str(i) + "\t" + str(j) + "\t"
                   + str(old_i) + "\t" + str(old_j) + "\t" + str(new_i) + "\t"
                   + str(new_j) + "\t" + str(coauth_all) + "\t" + str(coauth_10) + "\t" + str(coauth_5)
                   + "\t" + str(com_collab_all) + "\t" + str(com_collab_10) + "\t" + str(com_collab_5)
                   + "\t" + str(pa) + "\t" + str(M) + "\t" + str(w_jacc) + "\t" + str(w_salton) + "\t"
                   + str(len(path) - 1)
                   + "\t" + str(C) + "\t" + str(matching_count) + "\t" + str(distance)
                   + "\t" + str(label_2007) + "\t" + str(label_2008) + "\t" + str(label_2009) +
                   "\t" + str(label_2010) + "\t" + str(label_2011) +
                   "\t" + str(label_2012) + "\t" + str(label_2013) +
                   "\t" + str(label_2014) + "\t" + str(label_2015) +
                   "\t" + str(label_2016) + "\t" + str(label) + "\n")

    return


