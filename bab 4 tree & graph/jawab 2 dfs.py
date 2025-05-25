from collections import defaultdict

#Membuat class graph list
class GraphList:
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)

    def dfs(self, node, visited=None):
        if visited is None:
            visited = set()
        visited.add(node)
        print(node, end=' ')
        for nei in self.adj[node]:
            if nei not in visited:
                self.dfs(nei, visited)

#Membuat class graph matrix
class GraphMatrix:
    def __init__(self, nodes):
        self.nodes = nodes
        self.index = {node: i for i, node in enumerate(nodes)}
        n = len(nodes)
        self.mat = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        i, j = self.index[u], self.index[v]
        self.mat[i][j] = 1

    def dfs(self, start):
        visited = [False] * len(self.nodes)
        self._dfs_util(start, visited)

    def _dfs_util(self, node, visited):
        idx = self.index[node]
        visited[idx] = True
        print(node, end=' ')
        for i, has_edge in enumerate(self.mat[idx]):
            if has_edge and not visited[i]:
                self._dfs_util(self.nodes[i], visited)


#Main program dan menambahkan list
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
    print("DFS (Adjacency List) order:")
    g_list.dfs('A') 
    print()

    #Menambahkan matrix
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

    #Memanggil fungsi 
    print("DFS (Adjacency Matrix) order:")
    g_matrix.dfs('A')  
    print()
