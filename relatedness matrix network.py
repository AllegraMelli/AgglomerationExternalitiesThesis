import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the relatedness matrix
labels = ['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10']
relatedness = np.array([
    [0, 0.297297, 0.027778, 0.08, 0.090909, 0, 0.083333, 0, 0.052632, 0],
    [0.297297, 0, 0.027778, 0.038462, 0.028571, 0, 0.083333, 0, 0.052632, 0.137931],
    [0.027778, 0.027778, 0, 0.04878, 0.190476, 0.210526, 0.037037, 0, 0, 0],
    [0.08, 0.038462, 0.04878, 0, 0.076923, 0.025641, 0.046512, 0.322581, 0.15, 0],
    [0.090909, 0.028571, 0.190476, 0.076923, 0, 0.047619, 0, 0, 0, 0],
    [0, 0, 0.210526, 0.025641, 0.047619, 0, 0.041667, 0, 0, 0.1875],
    [0.083333, 0.083333, 0.037037, 0.046512, 0, 0.041667, 0, 0, 0.148148, 0.043478],
    [0, 0, 0, 0.322581, 0, 0, 0, 0, 0.038462, 0],
    [0.052632, 0.052632, 0, 0.15, 0, 0, 0.148148, 0.038462, 0, 0.041667],
    [0, 0.137931, 0, 0, 0, 0.1875, 0.043478, 0, 0.041667, 0]
])

# Industry mapping
industry_map = {
    'I1': 'Pharmaceutical Industry',
    'I2': 'Chemical industry',
    'I3': 'Automotive industry',
    'I4': 'ICT information and services',
    'I5': 'Aerospace construction and engineering',
    'I6': 'Specialistic Technical and scientific activities',
    'I7': 'Manufacturing of measurement instruments of navigation and Watchmaking',
    'I8': 'Editing audiovisual and diffusion',
    'I9': 'Manufacturing of communication equipment',
    'I10': 'Production and distribution of gas vapour and AC'
}

# Create graph
G = nx.Graph()

# Add edges with weights
for i in range(len(labels)):
    for j in range(i+1, len(labels)):
        if relatedness[i][j] > 0:
            G.add_edge(labels[i], labels[j], weight=relatedness[i][j])

# Node size based on degree (number of edges)
node_sizes = [300 + 300 * G.degree(n) for n in G.nodes()]

# Node color based on total relatedness
node_colors = [sum([d['weight'] for u, v, d in G.edges(n, data=True)]) for n in G.nodes()]

# Draw graph
pos = nx.spring_layout(G, seed=42)
fig, ax = plt.subplots(figsize=(12, 8))
nodes = nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.viridis, ax=ax)
edges = nx.draw_networkx_edges(G, pos, width=[d['weight']*10 for (u, v, d) in G.edges(data=True)], ax=ax)
nx.draw_networkx_labels(G, pos, ax=ax)

# # Add colorbar for node color
# sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(node_colors), vmax=max(node_colors)))
# sm.set_array([])
# cbar = fig.colorbar(sm, ax=ax)
# cbar.set_label('Total Relatedness')

# Add legend for industry mapping
legend_labels = [f"{k}: {v}" for k, v in industry_map.items()]
legend_handles = [plt.Line2D([0], [0], marker='o', color='w', label=label, markersize=5, markerfacecolor='gray') for label in legend_labels]
ax.legend(handles=legend_handles, loc='upper left', bbox_to_anchor=(1, 1), title="Industry Mapping")

ax.set_title("Industry Relatedness Network")
ax.axis('off')
plt.tight_layout()
plt.show()

