

import pandas as pd
import re
from nlp_util import *

class Node:
	def __init__(self, _question, _keywords, _children, _parent, _is_leaf=False):
		self.question = _question
		self.keywords = _keywords
		self.parent = _parent
		self.children = _children
		self.is_leaf = _is_leaf

	def find_child(self, text):

		# text = re.sub('[^0-9a-zA-Z]+', ' ', s)
		# words = text.split()
		# for child in self.children:
		# 	keywords.append(child.keywords)
		# for word in words:

		max_child = 0
		max_match = 0
		status = True
		similarities = []
		for child in self.children :
			similarity = get_similarity(child.keywords,text)
			similarities.append([child, similarity])
			if similarity != 0:
				max_match = 1

		if max_match==0:
			status = False

		sorted_similarity = sorted(similarities, key = lambda x : x[1])
		sorted_children = [i[0] for i in similarities]
		# print(sorted_children)
		return sorted_children, status



class Graph:
	def __init__(self,_nodes = []):
		self.nodes = _nodes
		self.root_index = 0

	#Reads file with _ separated values and creates graph
	def make_graph(self, questions_filename, content_filename):

		# knowledge_base = pd.read_csv(questions_filename,sep = "_", names = ["ID", "NOKeys", "Question", "Keywords"])
		knowledge_base = pd.read_csv(questions_filename,sep = "_", names = ["ID", "Isleaf", "Question"])
		keywords = pd.read_csv(content_filename,sep = "_", names = ["ID", "Keywords"])
		knowledge_base["Keywords"] = keywords["Keywords"]
		knowledge_base = knowledge_base.fillna(0)
		# print(knowledge_base)
		parent_index = None
		node = None
		rows = {}

		for row in knowledge_base.iterrows():
			# print(row[1]["ID"])
			if row[1]["ID"] == "0":
				node = Node(row[1]["Question"],[],[], None)
				rows["0"] = node
				self.nodes.append(node)
				continue

			split_index = row[1]["ID"].split(".")[0:-1]

			if split_index == []:
				parent_index = "0"
			else:
				parent_index = ".".join(split_index)

			# print(parent_index)



			if row[1]["Isleaf"] == 0:

				keywords = generate_key(row[1]["Keywords"])
				# node = Node(row[1]["Question"], row[1]["Keywords"].split(","), [])
				node = Node(row[1]["Question"], keywords, [], rows[parent_index])

			else:

				node = Node(row[1]["Question"], [], [], rows[parent_index], _is_leaf = True)

			rows[row[1]["ID"]] = node
			rows[parent_index].children.append(node)

			self.nodes.append(node)


if __name__ == "__main__":

	graph = Graph()
	graph.make_graph("../data/questions.txt", "../data/passage.txt")
	for node in graph.nodes:
		for child in node.children:
			print(child.question)
			if child.is_leaf:
				print ("The node is a leaf")
			else:
				print ("The node is not a leaf")
