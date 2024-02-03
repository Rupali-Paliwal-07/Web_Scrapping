import numpy as np

def calculate_pagerank(adjacency_matrix, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    num_nodes = adjacency_matrix.shape[0]
    initial_pagerank = np.ones(num_nodes) / num_nodes
    pagerank = initial_pagerank.copy()

    for iteration in range(max_iterations):
        new_pagerank = np.zeros(num_nodes)
        for i in range(num_nodes):
            for j in range(num_nodes):
                if adjacency_matrix[j, i] == 1:
                    outgoing_links = np.sum(adjacency_matrix[j])
                    new_pagerank[i] += pagerank[j] / outgoing_links
        new_pagerank = (1 - damping_factor) / num_nodes + damping_factor * new_pagerank

        if np.linalg.norm(new_pagerank - pagerank) < tolerance:
            break

        pagerank = new_pagerank

    return pagerank

# Example usage:
# Create a sample adjacency matrix representing a directed graph
adjacency_matrix = np.array([
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
])

# Calculate PageRank scores for the graph
pagerank_scores = calculate_pagerank(adjacency_matrix)

# Print the PageRank scores for each node
for i, score in enumerate(pagerank_scores):
    print(f"Node {i + 1}: {score:.4f}")