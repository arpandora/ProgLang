import pandas as pd
class Node:
	def __init__(self,_question="",_keywords=[], _children=[], _is_leaf=False):
		self.question = _questions
		self.keywords = _keywords
		self.children = _children
		self.is_leaf = _is_leaf


class Graph:
	def __init__(self,_nodes):
		self.nodes = _nodes

	def make_graph(self,filename):
		#Reads file with _ separated values and creates graph
		df = pd.read_csv("knowledgebase.txt",sep = "_")
		
