#!/usr/bin/python
"""Minimum spanning tree is to find a subtree which can connect all vertices in a given tree at the minimum cost

Select any random node and add it to the MST

Look at all edges emerging from vertices in MST to vertices not in MST
Add the edge with minimum weight to the tree. Add the other node to the tree too. 

Repeat step one till all tree vertices are covered. 


"""
def main():
	graph = {'a' : {'b' : 2, 'd': 5, 'f' : 6 }, 'b': {'a' : 2, 'c': 8, 'd' : 6}, 'c' : {'b': 8, 'd' : 3, 'e' : 5}, 'd': {'a': 5, 'b': 6, 'c': 3, 'e': 6, 'f': 7}, 'e':{'c':5, 'd': 6, 'f': 2}, 'f':{'a': 6, 'd' : 7, 'e': 2}}

	class node:
		def __init__(self, name, neighbours):
			self.name = name
			self.neighbours = neighbours
			self.mst = 0
		
	nodes = []
	for i in 'abcdef':
		neighbours = graph[i].items()
		i = node(i, neighbours)
		nodes.append(i)
	nodes_dict = dict(zip('abcdef', nodes))
	print prims(nodes_dict, graph)

def prims(nodes_dict, graph):
#create a list of all (mst edges, weight)
	mst_edges = []
	#Create a list of node names in the MST by assuming the convention that you always start from node A
	mst_nodes = ['a']
	nodes_dict['a'].mst = 1
	#Create a list of node names not in the MST (intially it has all the nodes except A)
	non_mst_nodes = list('bcdef')
	#while tree nodes are not empty:
	while len(non_mst_nodes) > 0:
		minimizer = []
		#print minimizer
		for i in mst_nodes:
			neighbours = nodes_dict[i].neighbours
			neighbours = sorted(neighbours, key = lambda x:x[1])
			print neighbours
			for j in neighbours:
				if j[0] in mst_nodes:
					continue
				else:
					minimizer.append([j[0], i + j[0], j[1]])
					#print minimizer
					break
		
#do this for all edges in MST:
#	select the edges whose other end is not in MST and return the minimum of it to a array called minimizer(node name, edge name, weight).
#select smallest from minimizer
		minimizer = sorted(minimizer, key = lambda x:x[2])
		print minimizer
		temp = minimizer[0]
		print temp
		print "--------------------------------------------"
		mst_nodes.append(temp[0])
#add node name to mst
		non_mst_nodes.remove(temp[0])
#remove name from non_mst_nodes
		nodes_dict[temp[0]].mst = 1
#flag node.mst to 1
		mst_edges.append((temp[1], temp[2]))
#add to mst_edge list
	print "MST is"
	return mst_edges
					
if __name__ == '__main__':
	main()		

	
	
