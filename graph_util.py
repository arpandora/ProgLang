import pandas as pd
import re

class Node:
	def __init__(self,_question="",_keywords=[], _children=[], _is_leaf=False):
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
		max_matches = 0
		status = True
		text_words = text.split()
		for child in self.children :
			count = 0
			for word in child.keywords:
				if word in text_words:
					count+=1
			if count > max_matches:
				max_matches = count
				max_child = child
		if max_matches==0:
			status = False

		return max_child, status



class Graph:
	def __init__(self,_nodes = []):
		self.nodes = _nodes
		self.root_index = 0

	def make_graph(self,filename):
		#Reads file with _ separated values and creates graph
		df = pd.read_csv(filename,sep = "_")