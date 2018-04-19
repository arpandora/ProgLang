

import pandas as pd
import re
from nlp_util import *

class Node:
	def __init__(self,_question,_keywords, _children,  _is_leaf=False):
		self.question = _question
		self.keywords = _keywords
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
		for child in self.children :
			similarity = get_similarity(child.keywords,text)
			if similarity > max_match:
				max_match = similarity
				max_child = child

		if max_match==0:
			status = False

		return max_child, status



class Graph:
	def __init__(self,_nodes = []):
		self.nodes = _nodes
		self.root_index = 0

	#Reads file with _ separated values and creates graph
	def make_graph(self,filename):

		knowledge_base = pd.read_csv(filename,sep = "_", names = ["ID", "NOKeys", "Question", "Keywords"])
		knowledge_base = knowledge_base.fillna(0)
		parent_index = None
		node = None
		rows = {}

		for row in knowledge_base.iterrows():
			# print(row[1]["ID"])
			if row[1]["ID"] == "0":
				node = Node(row[1]["Question"],[],[])
				rows["0"] = node
				self.nodes.append(node)
				continue

			parent_index = row[1]["ID"][0:-2]

			if parent_index == "":
				parent_index = "0"

			if row[1]["Keywords"] != 0:

				node = Node(row[1]["Question"], row[1]["Keywords"].split(","), [])

			else:

				node = Node(row[1]["Question"], [], [], _is_leaf = True)

			rows[row[1]["ID"]] = node
			rows[parent_index].children.append(node)

			self.nodes.append(node)


if __name__ == "__main__":

	graph = Graph()
	graph.make_graph("./knowledgebase.txt")
	for node in graph.nodes:
		for child in node.children:
			print(child.question)
