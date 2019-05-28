import json
import os
from pprint import pprint # "pretty print"
filename = os.path.join('./Lab 5/', 'KuroseRoss5-15.json') # modify as required
netjson = json.load(open(filename))



import networkx as nx # saves typing later on
graph = nx.Graph()
graph.add_nodes_from((
        (node['id'], node['properties']) # node-attributes
            for node in netjson['nodes']))
graph.add_edges_from((
        (link['source'], link['target'], {'cost': link['cost']}) # source-target-attributes
            for link in netjson['links']))
#for node, data in graph.nodes(data=True):
#    pprint((node, data))
#for source, target, data in graph.edges(data=True):
#    pprint((source, target, data)) # edges & attributes
#for node in graph:
#    pprint((node, dict(graph[node]))) # neighbours
    
    
node_positions = nx.get_node_attributes(graph, name='pos')
edge_label_positions = nx.draw_networkx_edge_labels(
    graph,
    pos=node_positions,
    node_labels=nx.get_node_attributes(graph, name='name'),
    edge_labels=nx.get_edge_attributes(graph, name='cost'))
nx.draw_networkx(graph, pos=node_positions)

node_positions2 = nx.spring_layout(graph)

sp = nx.shortest_path_length(graph, source='u', target=None, weight='cost', method='dijkstra')

pred = nx.dijkstra_predecessor_and_distance(graph, source='u', cutoff=None, weight='cost')

pprint(pred)

sp_tree = nx.convert.from_dict_of_lists(pred[0]).edges()
print(sp_tree)

nx.draw_networkx_edges(
    graph,
    pos=node_positions,
    edgelist=sp_tree,
    edge_color='r',
    width=3)


############# part 2 ###############







