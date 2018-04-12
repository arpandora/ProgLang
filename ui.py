from graph_util import *

def main():
	# graph = Graph()
	# graph.make_graph("knowledgebase.txt")
	graph = testGraph()
	queryBot(graph)

def testGraph():
	p1 = Node(_question = "The accused can be sentenced to 2 months in prison.",_is_leaf =True)
	p2 = Node(_question = "The accused can be sentenced to 5 months in prison.",_is_leaf =True)
	nc1 = Node ("Is your case related to literature copyright infringment?", ["book","paper","copied", "infringment"],[p1])
	nc2 = Node ("Is your case related to music copyright infringment?",["music", "copied", "track","record"],[p2])
	n1  = Node("Does your case fall into copyright cases?",["a","b"], [nc1,nc2])
	return Graph([n1,nc1,nc2,p1,p2])

def queryBot(graph):
	print "Welcome to Legal solutions !!\n"
	node = graph.nodes[graph.root_index]
	while (node.is_leaf == False):
		print(node.question)
		res = raw_input()
		if (res == "yes"):
			if (node.children[0].is_leaf == True):
				node = node.children[0]
				break
			print "Describe your problem further in the above category."
			description = raw_input()
			child_node,status = node.find_child(description)
			if (status):
				node = child_node
		
		elif (res == "no"):	
			print "Couldn't find a match."
		else :
			print "enter yes or no."
	
	if (node.is_leaf):
		print node.question




if __name__ == "__main__":
	main()