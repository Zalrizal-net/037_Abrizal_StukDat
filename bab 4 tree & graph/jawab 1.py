# Mengambil libary
import matplotlib.pyplot as plt
import networkx as nx

#Membuat class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    #Fungsi untuk menghitung tinggi 
    def height(self, node):
        if node is None:
            return -1  
        return 1 + max(self.height(node.left), self.height(node.right))

    #Fungsi inoder, preorder, dan postorder
    def inorder(self, root):
        return self.inorder(root.left) + [root.value] + self.inorder(root.right) if root else []

    def preorder(self, root):
        return [root.value] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.value] if root else []
    
    

# Membuat tree
tree = TreeNode('A')
tree.left = TreeNode('B')
tree.right = TreeNode('C')
tree.left.left = TreeNode('D')
tree.left.right = TreeNode('E')
tree.right.left = TreeNode('F')

# memanggil fungsi height
print("Tinggi pohon:", tree.height(tree)) 

# memanggil inoder, preorder, dan postorder
print("Inorder Traversal:", tree.inorder(tree))
print("Preorder Traversal:", tree.preorder(tree))
print("Postorder Traversal:", tree.postorder(tree))

# Memvisualisasikan graph
G = nx.DiGraph()  

def add_edges(graph, node):
    if node:
        if node.left:
            graph.add_edge(node.value, node.left.value)
            add_edges(graph, node.left)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            add_edges(graph, node.right)
add_edges(G, tree)

def hierarchy_pos(G, root, width=1.0, vert_gap=0.2, vert_loc=0, xcenter=0.5):
    pos = {}
    def _hierarchy_pos(G, root, leftmost, width, vert_gap, vert_loc, xcenter, pos, parent=None):
        children = list(G.neighbors(root))
        if parent is not None and parent in children:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width / 2 - dx / 2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, leftmost, dx, vert_gap, vert_loc - vert_gap, nextx, pos, root)
        pos[root] = (xcenter, vert_loc)
        return pos

    return _hierarchy_pos(G, root, 0, width, vert_gap, vert_loc, xcenter, pos)
pos = hierarchy_pos(G, tree.value)

plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=14, arrows=True)
plt.title("Visualisasi Pohon Biner")
plt.show()