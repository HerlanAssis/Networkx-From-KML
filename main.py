from graph.gp import GraphFromKmlDoc
from graph.plot import PlotGraph
# import networkx as nx


if __name__ == '__main__':    
    m_ad = GraphFromKmlDoc().get_matriz_adjacencias()

    nt = PlotGraph(m_ad)

    all_connections = nt.get_G()

    # nt.plot(all_connections) # plot matriz de adjacencias

    mst = nt.get_mst(all_connections) # crie a árvore geradora mínima

    # # obtendo todas os vértices do grafo
    # edges = [e for e in mst.edges(data=True)]

    # for edge in edges:
    #     # se a conexão entre eles for menor
    #     # que 500 metros, pinte de 'blue'
    #     if edge[2]['weight'] <= 0.75:
    #         edge[2]['color'] = 'g'
    #     elif edge[2]['weight'] < 1.5:
    #         edge[2]['color'] = 'b'
    # # atualizando as cores das ligações que tem menos de 500 metros
    # mst.update(edges=edges, nodes=mst.nodes)

    nt.plot(mst)
