from nltk.corpus import wordnet as wn
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer


def get_similarity(keywords, sentence):
	# Returns score by matching keywords to sentence (including synonyms)

	score_cutoff = 0.3 #Minimum similarity to consider in score

	tokens1 = word_tokenize(sentence)
	tagged_words1 = pos_tag(tokens1)
	tagged_words1 = lemmatize(tagged_words1)

	tokens2 = keywords
	tagged_words2 = pos_tag(tokens2)
	tagged_words2 = lemmatize(tagged_words2)

	synsets_list1 =  synsets_from_pos(tagged_words1)

	synsets_list2 = synsets_from_pos(tagged_words2)


	score, count = 0.0, 0


	for synsets in synsets_list2:

		max2 = []
		for synsets2 in synsets_list1:
			max1 = []
			for synset in synsets:
				max3 = 0
				for synset2 in synsets2:
					similarity = synset.path_similarity(synset2)
					if similarity is not None:
						if (similarity>max3):
							max3 = similarity

							# Uncomment this print statement to see matching :
							# print(synset, synset2, similarity)

				max1.append(max3)
			max2.append(max(max1))


		if max2 == []:
			best_score = 0
		else:
			best_score = max(max2)

		if best_score is not None and best_score >= score_cutoff:
			score += best_score
			count += 1


	return score




def lemmatize(tagged_words):
	lemmatizer = WordNetLemmatizer()
	ret_list = []
	for tup in tagged_words:
		word = tup[0]
		pos = tup[1]
		wn_tag = wordnet_tag(pos)
		if (wn_tag is None):
			ret_list.append((lemmatizer.lemmatize(word),pos))
		else :
			ret_list.append((lemmatizer.lemmatize(word,wn_tag), pos))
	return ret_list

def synsets_from_pos(tagged_words):
	ret_list =[]
	for tagged_word in tagged_words:
		synset = tag_to_synset(tagged_word[0],tagged_word[1])
		if synset is not None and synset != []:
			ret_list.append(synset)
	return ret_list

def tag_to_synset(word,tag):
	wn_tag = wordnet_tag(tag)

	if wn_tag is None:
		return None


	synsets = wn.synsets(word,wn_tag)

	if (len(synsets)>0):
		return synsets

def wordnet_tag(tag):
    if tag.startswith('N'):
        return wn.NOUN

    if tag.startswith('V'):
        return wn.VERB

    if tag.startswith('J'):
        return wn.ADJ

    if tag.startswith('CD'):
        return wn.ADJ

    if tag.startswith('R'):
        return wn.ADV


    return None

def generate_key(passage):
    pos_tagged_stream = pos_tag(word_tokenize(passage))
    wordNet_tagged_stream = [(word,wordnet_tag(tag)) for (word,tag) in pos_tagged_stream if ((wordnet_tag(tag) != None) )]
    keywords = list(set([ (word,tag) for (word,tag) in wordNet_tagged_stream]))

    return keywords




if __name__=="__main__":
	print(get_similarity(["steal"], "Someone stole my music"))
