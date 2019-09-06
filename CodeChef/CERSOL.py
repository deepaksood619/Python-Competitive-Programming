import networkx as nx
from networkx.algorithms.dominating import dominating_set

"""
1
5 4 5
1 1 2 2 3
1 2
1 3
2 4
2 5
"""

G = nx.Graph()
CG = nx.Graph()
t = 1
for _ in range(t):
    n, m, k = 5,4,5
    classes_list = [1,1,2,2,3]
    print(n,m,k)
    print(classes_list)

    

    x = [(1,2),(1,3),(2,4),(2,5)]
    for _ in x:
        u, v = _
        print(u, v)
        G.add_edge(u, v)

    print("Nodes of graph: ")
    print(G.nodes())
    print("Edges of graph: ")
    print(G.edges())

    # Dominating set
    ds = dominating_set(G)
    print(ds)
    len_ds = len(ds)
    print(len_ds)

    if len_ds == 0:
        print(-1)
    elif len_ds >= k:
        print(len_ds)
    else:
        print(k)
