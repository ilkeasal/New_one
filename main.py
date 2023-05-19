# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import nltk
from nltk import word_tokenize
import numpy as np
import pandas as pd


vico_sentences=open("/Users/ilkeasal/Desktop/Internship_project/multimodal-evaluation-main/data/VICO.txt","r").readlines()

Pereira_concept_words=open("/Users/ilkeasal/Desktop/Internship_project/multimodal-evaluation-main/data/stimuli_180concepts copy.txt","r").readlines()

#now I will create a function to get rid of the '\n'

def read_file(file):
    texts=[]
    for word in file:
        text=word.rstrip('\n')
        texts.append(text)
    return texts
#
Pereira_concept_corrected=read_file(Pereira_concept_words)

Vico_sentences_corrected=read_file(vico_sentences)



total_occurances={concept:0 for concept in Pereira_concept_corrected}
sentence_ids={concept:[] for concept in Pereira_concept_corrected}
total_sentences={concept:[] for concept in Pereira_concept_corrected}
totall_sentences=[]
total_sentence_ids=[]
#Looping Over VICO sentences and counting :
#
for line in Vico_sentences_corrected:
    tokenized_line = word_tokenize(line)
    sentence_id = tokenized_line[:tokenized_line.index(',')]
    sentence_text = tokenized_line[tokenized_line.index(',')+1:]
    for sentence_word in sentence_text:
        for pereira_concepts in Pereira_concept_corrected:
            if sentence_word == pereira_concepts:
                total_occurances[pereira_concepts]+=1
                total_sentences[pereira_concepts].append(" ".join(sentence_text))
                sentence_ids[pereira_concepts].append(sentence_id)#works for ids and word_occurances
                total_sentence_ids.append(sentence_id[0])
                totall_sentences.append(" ".join(sentence_text))

#id_sent_df = pd.DataFrame.from_dict({"sentence_ids": total_sentence_ids,
                        #"sentence_texts": totall_sentences})
#id_sent_df.to_csv("ids_sentences.csv", index=False)


print(len(total_sentence_ids))

print(total_occurances) #this is the Frequency Distribution