#import libary
import heapq
import math
from itertools import permutations
import networkx as nx
import matplotlib.pyplot as plt

#Adjacency List Graph antar kota
graph = { 'surabaya':{'sidoarjo':26, 'gresik':24, 'mojokerto':50},
        'sidoarjo':{'gresik':42,'mojokerto':37, 'nganjuk':110},
        'gresik':{'mojokerto':53,'nganjuk':125, "kediri":130},
        'mojokerto':{'nganjuk':70,"kediri":75,'lamongan':50},
        'nganjuk':{'kediri':38,"lamongan":105, 'bojonegoro':65},
        'kediri':{'lamongan':110,"bojonegoro":100, 'tuban':130},
        'lamongan':{'bojonegoro':70,'tuban':60,'batu':110},
        'bojonegoro':{'tuban':42,'batu':150, 'surabaya':120},
        'tuban':{'batu':150,'surabaya':105, 'sidoarjo':120},
        'batu':{'surabaya':100,'sidoarjo':75, 'gresik':100}}

# Konversi Adjacency List ke Matriks Jarak
cities = list(graph.keys())
n = len(cities)
city_index = {city: i for i, city in enumerate(cities)}
dist = [[math.inf for _ in range(n)] for _ in range(n)]

# Isi matriks berdasarkan jarak di adjacency list
for city in graph:
    for neighbor in graph[city]:
        i = city_index[city]
        j = city_index[neighbor]
        dist[i][j] = graph[city][neighbor]
        dist[j][i] = graph[city][neighbor]  

#Fungsi dijkstra
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == end:
            return cost, path
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))

    return float('inf'), []

#Fungsi TSP Brute Force 
def tsp_brute_force(dist):
    n = len(dist)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    for perm in permutations(cities[1:]):  
        path = [0] + list(perm)
        cost = sum(dist[path[i]][path[i+1]] for i in range(n - 1)) + dist[path[-1]][0]
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path + [0], min_cost

# ===========================Main program==============================

#input pengguna dan mencetak hasil rute tercepat 2 kota
kota_asal= input("kota asal: ")
kota_tujuan= input('kota tujuan : ')
total_cost, route = dijkstra(graph, kota_asal, kota_tujuan)
print("Rute tercepat dari",kota_asal,'ke', kota_tujuan, 'adalah'," → ".join(route), '\nTotal jarak rute:', total_cost,'KM\n\n')

#Memangil fungsi dan mencetak hasil rute tercepat melewati semua kota
route, cost = tsp_brute_force(dist)
print("Rute tercepat melewati semua kota:\n", " → ".join(cities[i] for i in route), "\nTotal jarak:", cost,'KM')

# ======================== Visualisasi Graph ========================
# Buat graph NetworkX dari adjacency list
G = nx.Graph()

for city in graph:
    for neighbor in graph[city]:
        G.add_edge(city, neighbor, weight=graph[city][neighbor])
pos = nx.spring_layout(G, seed=42)

nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

# # Visualisasi Rute TSP 
# rute_tsp_nama = [cities[i] for i in route]
# rute_tsp_edges = [(rute_tsp_nama[i], rute_tsp_nama[i+1]) for i in range(len(rute_tsp_nama) - 1)]
# nx.draw_networkx_edges(G, pos, edgelist=rute_tsp_edges, edge_color='red', width=3)

# Tampilkan hasil visualisasi
plt.title("Graf Antar Kota dan Rute TSP (Merah)")
plt.tight_layout()
plt.show()