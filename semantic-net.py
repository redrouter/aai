import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add nodes for concepts and subconcepts
G.add_node('Chemical bonds', description='Connections between atoms in a molecule')
G.add_node('Strong intramolecular interactions', examples=['Covalent bonds', 'Ionic bonds'])
G.add_node('Weaker intermolecular forces', examples=['Dipole-dipole interactions', 'London dispersion forces', 'Hydrogen bonding'])
G.add_node('Intermolecular forces', description='Weaker forces compared to intramolecular interactions')

# Add edges to connect concepts
G.add_edge('Chemical bonds', 'Strong intramolecular interactions')
G.add_edge('Chemical bonds', 'Weaker intermolecular forces')
G.add_edge('Weaker intermolecular forces', 'Intermolecular forces')

# Draw the semantic network
pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray', arrowsize=20)
plt.show()
