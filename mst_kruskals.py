#usr/bin/python

""" The Kruskals algorithm rather than depending on vertices and then exploring cheapest adjacent edges , goes directly to selecting cheapest edges from anywhere in the graph.


So, select the cheapest edges and avoid cycles.

The way I will try and avoid cycles is as follows:

lets say I have a possible fix on a and b as the cheap edge. I will check for neighbours of a and neoghbours of b and take an intersection. Lets say we have c as an intersection. Now I will check if both ac and bc are edges in the tree. If this is the case ab cannot be an edge.


"""
def main():
	graph = {'a' : {'b' : 2, 'd': 5, 'f' : 6 }, 'b': {'a' : 2, 'c': 8, 'd' : 6}, 'c' : {'b': 8, 'd' : 3, 'e' : 5}, 'd': {'a': 5, 'b': 6, 'c': 3, 'e': 6, 'f': 7}, 'e':{'c':5, 'd': 6, 'f': 2}, 'f':{'a': 6, 'd' : 7, 'e': 2}}
	
	temp  = graph.items()
	
	for i in  temp:
		for j in i[1].keys():
			if 'abcdef'.index(i[0]) < 'abcdef'.index(j):
				continue
			else:
				del i[1][j]
	edge_dict = {}
	print "This is temp"
	print temp
	print "-----------------------"
	for i in temp:
		for j in i[1].keys():
			edge_name, edge_weight = i[0] + j, i[1][j]
			edge_dict[edge_name] = edge_weight
	print edge_dict	
	

	class node:
		def __init__(self, name):
			self.name   = name
			#self.adjedges = adjedges  #THIS HAPPENS TO BE A DICTIONARY
			"""#EDIT: After some deliberation iv realized that there is no point declaring a new dict, I can make do with the available stuff from edge_dict"""
			self.mst = 0 #Zero indicating that the node is not yet a part of the minimum spanning tree
	node_dict = {}			
	for i in 'abcdef':
		node_dict[i]  = node(i)

	print node_dict
	print "------------------------FINAL ANSWER--------------------------"
	print kruskal(graph, edge_dict, node_dict)

def cycledet(v1, v2, intendedge, mst_edges):
	print "The spanning tree right now is "
	print mst_edges
	print "The edge is " + intendedge 
	adj_edges = []
	for i in mst_edges:
		if ((v1 in i) and (i != intendedge)):
			adj_edges.append(i)
	print adj_edges
	for j in adj_edges:
		if v2 in j:
			return 0
		else:
			value = cycledet(j.replace(v1, ''), v2, j, mst_edges)
			if value == 0:
				print "cycle detected" 
				return 0
				break
			
	return 1 #to ensure that if a node has no neighbours it says no cycle found
			
	
	
	
def kruskal(graph, edge_dict, node_dict):
	mst_edges = []
	mst_sum = 0
	#Define a list of all edges in the Minimum Spanning tree
	edges_sorted = sorted(edge_dict.items(), key = lambda x: x[1])
	print edges_sorted
	print edges_sorted[0][0]
	edges_sorted_names  = [i[0] for i in edges_sorted]
	#Create a sorted list of all edges
	while(len(edges_sorted) > 0):
	#while the list of sorted edges is not empty.
		#print edges_sorted
		select_edge = (edges_sorted[0])[0]
		select_edge_weight = (edges_sorted[0])[1]	
	#Select the minimum edge
		v1, v2 = list(select_edge)
		#print mst_edges
		value = cycledet(v1, v2, select_edge, mst_edges)
		if value == 1:
			mst_edges.append(select_edge)
			edges_sorted.remove((select_edge, select_edge_weight))
			mst_sum = mst_sum + select_edge_weight
		else:
			print "cycle detected"
			edges_sorted.remove((select_edge, select_edge_weight))
			
	#check if the two nodes of the selected edge form a cycle

	#if not, add it to mst_edges list and update the mst_sum

	#delete the 
	return mst_edges
if __name__ == "__main__":
	main()
