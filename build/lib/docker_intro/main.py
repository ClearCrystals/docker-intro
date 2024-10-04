import networkx as nx
import matplotlib.pyplot as plt
def dikstra():
    # Create a graph with nodes and weighted edges
    graph = nx.Graph()
    nodes = range(1, 7)
    graph.add_nodes_from(nodes)

    edges_with_weights = [
        (1, 2, 7), (1, 3, 9), (1, 6, 14),
        (2, 3, 10), (2, 4, 15), (3, 4, 11),
        (3, 6, 2), (4, 5, 6), (5, 6, 9)
    ]
    graph.add_weighted_edges_from(edges_with_weights)

    start_node, end_node = 1, 5
    shortest_path = nx.dijkstra_path(graph, source=start_node, target=end_node)
    shortest_path_length = nx.dijkstra_path_length(graph, source=start_node, target=end_node)

    positions = nx.spring_layout(graph)
    plt.figure(figsize=(10, 6))

    nx.draw(graph, positions, with_labels=True, node_color='lightblue', font_weight='bold')
    edge_weights = {(u, v): d['weight'] for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, positions, edge_labels=edge_weights)

    path_edges = list(zip(shortest_path, shortest_path[1:]))
    nx.draw_networkx_edges(graph, positions, edgelist=path_edges, edge_color='red', width=2)

    plt.title("Dijkstra's Algorithm Visualization")
    plt.savefig('dijkstra_graph_output.png')
    plt.close()

def main():
    print("Hello WOrld")
    # dikstra()

if __name__ == "__main__":
    main()
