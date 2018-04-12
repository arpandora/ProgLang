from graph_util import *

def main():
	queryBot()



def queryBot():
	print "Welcome to Legal solutions !!\n"
	graph = Graph()
	graph.make_graph("knowledgebase.txt")
	node = graph.root
	while (!node.is_leaf){
		print(node.question)
		res = raw_input()
		if (res == "yes"){
			
		}
		else {
			print "Sorry we can't help you with that."
		}
	}




if __name__ == "__main__":
	main()