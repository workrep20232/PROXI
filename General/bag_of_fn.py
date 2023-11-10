'''
This code contains some of the functions we considered for our datasets Cora, Citeseer and Pubmed.

The functions are:
1. Jaccard Index
2. Salton Index
3. Sorensen Index
5. 3-Jaccard Index
6. 3-Salton Index
7. 3-Sorensen Index
8. Preferential Attachment (PA)

'''


def jaccard_index(graph, node_u, node_v):
    neighbors_u = set(nx.neighbors(graph, node_u))
    neighbors_v = set(nx.neighbors(graph, node_v))

    intersection_size = len(neighbors_u.intersection(neighbors_v))
    union_size = len(neighbors_u.union(neighbors_v))
    if union_size == 0:
        return 0

    return intersection_size / union_size


def salton_index(graph, node_u, node_v):
    common_neighbors = list(nx.common_neighbors(graph, node_u, node_v))
    if len(common_neighbors) == 0:  # To prevent division by 0 errors
        return 0

    degree_u = len(list(nx.neighbors(graph, node_u)))
    degree_v = len(list(nx.neighbors(graph, node_v)))

    return len(common_neighbors) / ((degree_u * degree_v) ** 0.5)


def sorensen_index(graph, node_u, node_v):
    common_neighbors = list(nx.common_neighbors(graph, node_u, node_v))
    if len(common_neighbors) == 0:  # To prevent division by 0 errors
        return 0

    degree_u = len(list(nx.neighbors(graph, node_u)))
    degree_v = len(list(nx.neighbors(graph, node_v)))

    return 2 * len(common_neighbors) / (degree_u + degree_v)


def jaccard_3_paths(graph, node_u, node_v, num):
    neighbors_u = set(nx.neighbors(graph, node_u))
    neighbors_v = set(nx.neighbors(graph, node_v))

    union_size = len(neighbors_u.union(neighbors_v))
    if union_size == 0:
        return 0

    return num / union_size


def salton_3_paths(graph, node_u, node_v, num):
    degree_u = len(list(nx.neighbors(graph, node_u)))
    degree_v = len(list(nx.neighbors(graph, node_v)))
    if degree_u * degree_v == 0:
        return 0

    return num / ((degree_u * degree_v) ** 0.5)


def sorensen_3_paths(graph, node_u, node_v, num):
    degree_u = len(list(nx.neighbors(graph, node_u)))
    degree_v = len(list(nx.neighbors(graph, node_v)))
    if degree_u + degree_v == 0:
        return 0

    return 2 * num / (degree_u + degree_v)


def PA(node_u, node_v, graph):
    try:
        degree_u = len(list(nx.neighbors(graph, node_u)))
        degree_v = len(list(nx.neighbors(graph, node_v)))
        result = degree_u * degree_v
    except:
        result = 0
    return result





