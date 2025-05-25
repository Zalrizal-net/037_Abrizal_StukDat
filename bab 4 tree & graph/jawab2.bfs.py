#Mengambil libary
from collections import defaultdict, deque

#Membuat class graplist
class GraphList:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def bfs(self, start):
        visited = set([start])
        q = deque([start])
        while q:
            u = q.popleft()
            print(u, end=' ')
            for nei in self.adj[u]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

#Membuat class grap matrix
class GraphMatrix:
    def __init__(self, nodes):
        self.nodes = nodes
        self.index = {node: i for i, node in enumerate(nodes)}
        n = len(nodes)
        self.mat = [[0]*n for _ in range(n)]

    def add_edge(self, u, v):
        i, j = self.index[u], self.index[v]
        self.mat[i][j] = 1

    def bfs(self, start):
        visited = [False] * len(self.nodes)
        q = deque()
        visited[self.index[start]] = True
        q.append(start)

        while q:
            u = q.popleft()
            print(u, end=' ')
            u_idx = self.index[u]
            for v_idx, has_edge in enumerate(self.mat[u_idx]):
                if has_edge and not visited[v_idx]:
                    visited[v_idx] = True
                    q.append(self.nodes[v_idx])



#Main program dan menambahkan data list
if __name__ == "__main__":
    g_list = GraphList()
    adj_list = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E', 'F'],
        'C': ['A', 'G'],
        'D': ['A'],
        'E': ['B'],
        'F': ['B'],
        'G': ['C']
    }
    for u in adj_list:
        for v in adj_list[u]:
            g_list.add_edge(u, v)

    #Memanggil fungsi
    print("BFS (Adjacency List) order:")
    g_list.bfs('A')
    print()

    #menambahkan data matrix
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    g_matrix = GraphMatrix(nodes)
    adj_matrix = [
        # A  B  C  D  E  F  G
        [ 0, 1, 1, 1, 0, 0, 0],  # A
        [ 1, 0, 0, 0, 1, 1, 0],  # B
        [ 1, 0, 0, 0, 0, 0, 1],  # C
        [ 1, 0, 0, 0, 0, 0, 0],  # D
        [ 0, 1, 0, 0, 0, 0, 0],  # E
        [ 0, 1, 0, 0, 0, 0, 0],  # F
        [ 0, 0, 1, 0, 0, 0, 0],  # G
    ]
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            if adj_matrix[i][j]:
                g_matrix.add_edge(nodes[i], nodes[j])

    #memanggil fungsi
    print("BFS (Adjacency Matrix) order:")
    g_matrix.bfs('A')
    print()
