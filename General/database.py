from bag_of_fn import *

def database(m, keyword, Y, sub_graph):

    '''
    In this code the feature vectors are computed and saved
    '''

    with open('Citeseer_spath' + str(m) + '.csv', 'r') as f:
        data2 = f.readlines()[1:]

    s_data = np.array([list(map(int, edge.strip().split('\t')[1:])) for edge in data2])

    name = 'Citeseer'
    file = open(name + '_database' + str(m) + '.csv', 'w')
    file.write('dataset' + "\t" + 'u' + "\t" + 'v' + "\t" + 'common keywords' + "\t" + 'common field' + "\t"
               + 'short path length' + "\t" + 'nr of 2paths' + "\t" + 'nr of 3paths' + "\t"
               + 'Jaccard' + "\t" + 'Salton' + "\t" + 'Sorensen' + "\t" + '3-Jaccard' + "\t" + '3-Salton' + "\t"
               + '3-Sorensen' + "\t"
               + "field of u" + "\t" + "field of v"
               + "\t" + "K-norm" 
               + "class1" + "\t" + "class2" + "\t" + "class3" + "\t" + "class4" + "\t" + "class5" + "\t" + "class6"
               + "\t" + "Adamic Andar"
               + "\t" + "label" + "\n")

    path3 = s_data[:, 4]
    print(path3)
    N = len(s_data)

    for k in range(N):

        i = s_data[k, 0]
        j = s_data[k, 1]

        try:
            F1 = jaccard_index(sub_graph, i, j)
        except:
            F1 = 0

        try:
            F2 = salton_index(sub_graph, i, j)
        except:
            F2 = 0

        try:
            F3 = sorensen_index(sub_graph, i, j)
        except:
            F3 = 0

        try:
            F4 = float(jaccard_3_paths(sub_graph, i, j, path3[k]))
        except:
            F4 = 0

        try:
            F5 = float(salton_3_paths(sub_graph, i, j, path3[k]))
        except:
            F5 = 0

        try:
            F6 = float(sorensen_3_paths(sub_graph, i, j, path3[k]))
        except:
            F6 = 0

        K = len(np.intersect1d(keyword[i], keyword[j]))

        try:
            K_norm = K / (len(keyword[i][0]) + len(keyword[j][0]) - K)
        except:
            K_norm = 0

        C = 1 if Y[i] == Y[j] else 0

        try:
            A = list(nx.adamic_adar_index(sub_graph, [(i, j)]))[0][2]
        except:
            A = 0

        Cl = create_array(Y[i], Y[j])

        file.write(name + "\t" + str(i) + "\t" + str(j) + "\t" + str(K) + "\t" + str(C) + "\t"
                   + str(s_data[k, 2]) + "\t" + str(s_data[k, 3]) + "\t" + str(s_data[k, 4]) + "\t"
                   + str(F1) + "\t" + str(F2) + "\t" + str(F3) + "\t"
                   + str(F4) + "\t" + str(F5) + "\t" + str(F6) + "\t"
                   + str(Y[i]) + "\t" + str(Y[j])
                   + "\t" + str(K_norm) 
                   + str(Cl[0]) + "\t" + str(Cl[1]) + "\t" + str(Cl[2]) + "\t" + str(Cl[3]) + "\t" + str(Cl[4])+ "\t" + str(Cl[5])
                   + "\t" + str(A) + "\t" + str(s_data[k, 5]) + "\n")

    file.close()
    print('done')
    return


