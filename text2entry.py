from nltk import word_tokenize, sent_tokenize

from tqdm import tqdm

import pandas as pd


with open('brewers_trim.txt', 'rb') as fi:
    file_txt = fi.readlines()

text = ''.join(file_txt)

# remove page headers
text_pages = text.split('\r\n\r\n\r\n')

body_groups = []
word_tokenset =[]
for idx, item in tqdm(enumerate(text_pages)):
    words = word_tokenize(item)
    word_tokenset.append(words)
    if len(words) > 8:

        # use page headers to tell if page begins with new definition or not
        if idx>4:
            if len(word_tokenset[idx-3])>0:
    
                if words[0]==word_tokenset[idx-3][0]:
                    body_groups.append(item)

                else:

                    body_groups[-1] = body_groups[-1] + ' ' + item

        else:
            body_groups.append(item)

                
# use some heuristics to find definitions in corpus
rough_defs = ''.join(body_groups).split('\r\n\r\n')

def_set = []
for candidate in tqdm(rough_defs):
    sents = sent_tokenize(candidate)

    words = [word_tokenize(sent) for sent in sents]
    word_group = [len(group) for group in words]

    if word_group[0] <= 8 and len(word_group)>=2:

        if words[0][0][0].isdigit():
            def_set[-1] = def_set[-1] + ' ' + candidate

        elif candidate[0] == '(':
            if ')' in words[0]:
                if words[0].index(')')==1:
                    def_set.append(candidate)

            else:
                def_set[-1] = def_set[-1] + ' ' + candidate

        else:
            def_set.append(candidate)

    else:
        def_set[-1] = def_set[-1] + ' ' + candidate
        
    
# clean definitions
clean_defs ={}
for definition in def_set:
    definition = definition.replace('\r\n', ' ')
    sents = sent_tokenize(definition)    
    clean_defs[sents[0]]=''.join(sents[1:])

df = pd.Series(clean_defs).transpose()
df.index.name='Entry'
df.name = 'Definition'
df.sort_index().to_csv('clean_brewers.csv',header=True)

