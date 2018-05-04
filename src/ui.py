from graph_util import *

def main():
	graph = Graph()
	#Modify this line when running this program from inside the src file
	graph.make_graph("data/questions.txt","data/passages.txt")
	print("Hi, I am Sunvai, an artificially intelligent bot to guide you with your case.\nPlease tell me your name: ")
	user_name = input()

	repeat = "yes"
	while(repeat == "yes"):
		queryBot(graph, user_name)
		print("Do you want to look up other sections?")
		repeat = input()
	print("All the best for the resolution of your case.")

def queryBot(graph, user_name):
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
			print("Please enter further details related to your offence or enter options.")
			description = input()
			while (description == "options"):
				# temp_node_list,status = node.find_child(description)
				for n in node.children:
					print(n.question)
				print("Please enter further details related to your offence or enter options.")
				description = input()
			child_node_list,status = node.find_child(description)
			# if (status):
			node_list = child_node_list
			node = node_list[child_index]


		elif (res == "no"):
			if (len(node_list)>child_index+1):
				child_index += 1
				node = node_list[child_index]
			else :
				child_index = 0
				print("No match was found")
				if (node.parent != None):
					if (node.parent.parent != None):
						node_list = [n for n in node.parent.parent.sorted_children]
					else:
						node_list = [node.parent]
				node = node_list[child_index]
		else :
			print("please enter yes or no.")

	if (node.is_leaf):
		print("we have found a match for the case.")
		print(node.question)
		print("You can use the help of a lawyer to access the strength of your case.\nHope I helped.")



if __name__ == "__main__":
	main()
