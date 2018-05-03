from graph_util import *

def main():
	graph = Graph()
	graph.make_graph("knowledgebase.txt")
	# graph = testGraph()
	queryBot(graph)

# def testGraph():
# 	p1 = Node("The accused can be sentenced to 2 months in prison.",[],[],_is_leaf =True)
# 	p2 = Node("The accused can be sentenced to 5 months in prison.",[],[],_is_leaf =True)
# 	nc1 = Node ("Is your case related to literature copyright infringment?", ["book","paper","copied", "infringment"],[p1])
# 	nc2 = Node ("Is your case related to music copyright infringment?",["music", "copied", "track","record"],[p2])
# 	n1  = Node("Does your case fall into copyright cases?",["a","b"], [nc1,nc2])
# 	return Graph([n1,nc1,nc2,p1,p2])

def queryBot(graph):
	print("Hi, I am Sunvai, an artificially intelligent bot to guide you with your case.\n Please tell me your name: ")
	user_name = input()
	print("Hello "+user_name+", good to have you here.\n")
	node_list = [graph.nodes[graph.root_index]]
	node = node_list[0]
	child_index = 0
	while (node.is_leaf == False):
		print(node.question)
		res = input()
		if (res == "yes"):
			if (node.children[0].is_leaf == True):
				node = node.children[0]
				break
			print("Please enter further details related to your offence.\n")
			description = input()
			child_node_list,status = node.find_child(description)
			if (status):
				node_list = child_node_list
				node = node_list[child_index]


		elif (res == "no"):
			if (len(node_list)>child_index+1):
				child_index += 1
			else :
				child_index = 0
				print("No match was found")
				if (node.parent != None):
					if (node.parent.parent != None)
						node_list = [n for n in node.parent.parent.children]
					else:
						nodes_list = [node.parent]
				node = nodes_list[child_index]
		else :
			print("please enter yes or no.")

	if (node.is_leaf):
		print("we have found a match for the case.\n")
		print(node.question)
		print("\n")
		print("You can use the help of a lawyer to access the strength of your case.\n Hope I helped. All the best for resolution of your case.")



if __name__ == "__main__":
	main()
