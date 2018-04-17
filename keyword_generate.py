from nltk import word_tokenize, pos_tag


def penn_to_wn(tag):
    if tag.startswith('N'):
        return 'n'

    if tag.startswith('V'):
        return 'v'

    if tag.startswith('J'):
        return 'a'

    if tag.startswith('CD'):
        return 'c'


    return None

def generate_key(passage):
    reqdWords = ['not']
    pos_tagged_stream = pos_tag(word_tokenize(passage))
    #print pos_tagged_stream
    wordNet_tagged_stream = [(word,penn_to_wn(tag)) for (word,tag) in pos_tagged_stream if ((penn_to_wn(tag) != None) or (word in reqdWords) )]
    keywords = list(set([ word for (word,tag) in wordNet_tagged_stream]))

    return keywords

if __name__ == '__main__':
    print generate_key("Imprisonment for a term which shall not not be less than six months and may extend to three years and with fine which shall not be less than fifty thousand rupees but which may extend to two lakh rupees")
