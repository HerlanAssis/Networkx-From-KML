import matplotlib.pyplot as plt
import networkx as nx


class PlotGraph:
    def __init__(self, distancias):
        self._distancias = distancias
        self._G = nx.Graph()

    def _add_edges(self):
        for praca, distancia_ate in self._distancias.items():
            for _praca, distancia_ate_ela in distancia_ate.items():
                self._G.add_edge(
                    praca, _praca, weight=distancia_ate_ela, color='r')

        return self._G

    def get_G(self):
        self._add_edges()
        return self._G

    def get_mst(self, G, data=True):
        mst = nx.tree.minimum_spanning_edges(G, algorithm='kruskal', data=data)
        edgelist = list(mst)

        mst_G = nx.Graph()

        for edge in sorted(edgelist):
            mst_G.add_edge(edge[0], edge[1], weight=edge[2]
                           ['weight'], color=edge[2]['color'])

        return mst_G

    def plot(self, G, legend=False):
        pos = nx.spring_layout(G)
        edges = G.edges()
        colors = [G[u][v]['color'] for u, v in edges]

        plt.figure(figsize=(40, 40))        

        nx.draw_networkx(G, pos, edge_color=colors, font_size=10, width=1, linewidths=1,
                         node_size=500, node_color='pink', alpha=0.5)

        if legend:
            labels = nx.get_edge_attributes(G, 'weight')

            for label, value in labels.items():
                labels[label] = str("{0:.2f}km".format(value))

            nx.draw_networkx_edge_labels(
                G, pos, font_size=6, alpha=0.5, edge_labels=labels)

        leg = []
        for idx, name in enumerate(G.nodes):
            leg.append("{} - {}".format(idx, name))
        
        plt.axis('equal')
        plt.show()
