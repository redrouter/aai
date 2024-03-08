import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('Chemical bonds', description='Connections between atoms in a molecule')
G.add_node('Strong intramolecular interactions', examples=['Covalent bonds', 'Ionic bonds'])
G.add_node('Weaker intermolecular forces', examples=['Dipole-dipole interactions', 'London dispersion forces', 'Hydrogen bonding'])
G.add_node('Intermolecular forces', description='Weaker forces compared to intramolecular interactions')

G.add_edge('Chemical bonds', 'Strong intramolecular interactions')
G.add_edge('Chemical bonds', 'Weaker intermolecular forces')
G.add_edge('Weaker intermolecular forces', 'Intermolecular forces')

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray', arrowsize=20)
plt.show()
