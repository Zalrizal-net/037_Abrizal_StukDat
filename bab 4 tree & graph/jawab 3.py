#Mengambil libary
import heapq

#Memasukan data graph
graph = {
    'jakarta': {'Bandung': 150, 'surabaya': 780},
    'Bandung': {'semarang': 430, 'surabaya': 800},
    'semarang': {'yogyakarta': 130},
    'surabaya': {'yogyakata': 7}
}

#Membuat Fungsi dijkstra
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

#Menghitung rute terpendek
total_cost, route = dijkstra(graph, 'jakarta', 'yogyakarta')

#Memangil fungsi
print("Rute terpendek dari jakarta ke yogyakarta:", " → ".join(route))
print("Total bobot rute:", total_cost) 