import math
'''
This code contains some of the functions we considered for our datasets Cora, Citeseer and Pubmed.

The functions are:
1. author oldest paper year, returns the author's earliest paper year
2. author newest paper year, returns the author's latest paper year
3. author oldest paper index, returns 0 if year<1985, 1 otherwise
4. author newest paper index, returns 0 if year<1985, 1 otherwise
5. co-authored papers
6. common collaboration, counts the authors that authors u and v have collaborated
7. w-Jaccard
8. w-Salton
9. Preferential Attachment (PA)
10. w-Adamic Andar
11. cosine similarity

'''


def auth_oldest_paper(distr, auth):
    if len(distr[auth]) > 0:
        return min(distr[auth])
    else:
        return 0


def auth_newest_paper(distr, auth):
    if len(distr[auth]) > 0:
        return max(distr[auth])
    else:
        return 0


def oldest_paper_index(auth_oldest, auth):
    if auth_oldest[auth] < 1985:
        return 0
    else:
        return 1


def newest_paper_index(auth_newest, auth):
    if auth_newest[auth] < 1985:
        return 0
    else:
        return 1


def coauth(edge, sums):
    if edge in sums:
        return sums[edge]
    elif (edge[1], edge[0]) in sums:
        return sums[(edge[1], edge[0])]
    else:
        return 0


def common_collab(u, v, graph):
    try:

        neighbors_u = set(graph.neighbors(u))
        neighbors_v = set(graph.neighbors(v))
        inters = list(neighbors_u.intersection(neighbors_v))
    except:
        inters = []

    return len(inters)


def jaccard_weight(graph, u, v, sums):
    try:
        neighbors_u = set(graph.neighbors(u))
        neighbors_v = set(graph.neighbors(v))
        inters = list(neighbors_u.intersection(neighbors_v))
        un = list(neighbors_u.union(neighbors_v))

        if len(un) == 0:
            return 0
        if len(inters) == 0:
            return 0

        inters_edges = []
        un_edges = []
        U = 0
        I = 0

        for item in inters:
            inters_edges.append((u, item))
            inters_edges.append((v, item))

        for item1 in un:
            un_edges.append((u, item1))
            un_edges.append((v, item1))

        for edge in inters_edges:
            if edge in sums:
                I += sums[edge]
            elif (edge[1], edge[0]) in sums:
                I += sums[(edge[1], edge[0])]
            else:
                I += 0

        for edge1 in un_edges:
            if edge1 in sums:
                U += sums[edge1]
            elif (edge1[1], edge1[0]) in sums:
                U += sums[(edge1[1], edge1[0])]
            else:
                U += 0

        res = I / U

    except:
        res = 0

    return res


def salton_weight(graph, u, v, num):
    try:
        common_neighbors = list(nx.common_neighbors(graph, u, v))
        if len(common_neighbors) == 0:  # To prevent division by 0 errors
            return 0

        w = 0
        for node in common_neighbors:
            w += num[node]

        degree_u = num[u]
        degree_v = num[v]

        res = w / ((degree_u * degree_v) ** 0.5)

    except:
        res = 0

    return res


def PA(u, v, num):
    try:
        du = num[u]
        dv = num[v]
        result = du * dv
    except:
        result = 0

    return result


def w_adamic_adar(u, v, num, graph):
    try:
        common_neighbors = list(nx.common_neighbors(graph, u, v))
        aa_index = sum(1 / log(num[neighbor]) for neighbor in common_neighbors if num[neighbor] > 1)
    except:
        aa_index = 0

    return aa_index


def cosine_similarity(vector1, vector2):
    dot_product = sum(x * y for x, y in zip(vector1, vector2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in vector1))
    magnitude2 = math.sqrt(sum(y ** 2 for y in vector2))

    similarity = dot_product / (magnitude1 * magnitude2)
    return similarity
