import pandas as pd
import re

class Node:
	def __init__(self,_question="",_keywords=[], _children=[], _is_leaf=False):
		self.question = _questions
		self.keywords = _keywords
		self.children = _children
		self.is_leaf = _is_leaf

	def find_child(self, text):

		text = re.sub('[^0-9a-zA-Z]+', ' ', s)
		words = text.split()
		for child in self.children:
			keywords.append(child.keywords)
		for word in words:


class Graph:
	def __init__(self,_nodes = []):
		self.nodes = _nodes

	def make_graph(self,filename):
		#Reads file with _ separated values and creates graph
		df = pd.read_csv(filename,sep = "_")
