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

id_sent_df = pd.DataFrame.from_dict({"sentence_ids": total_sentence_ids,
                        "sentence_texts": totall_sentences})
id_sent_df.to_csv("ids_sentences.csv", index=False)


#print(len(total_sentence_ids))

#print(total_occurances) #this is the Frequency Distribution

ids_sentences_newdf=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/ids_sentences_newdf.csv").readlines()



# ids_sentences_newdf_corrected=read_file(ids_sentences_newdf)
#
#
# unique_ids_sentences_newdf=(np.unique(ids_sentences_newdf_corrected))
#
#
# unique_ids_sentences_newlisted=(list(unique_ids_sentences_newdf))
#
# print(len(unique_ids_sentences_newlisted))
#
# sentence_ids = []
# sentence_texts=[]
# for line in unique_ids_sentences_newlisted:
#     tokenized_line=word_tokenize(line)
#     sentence_id=tokenized_line[1:tokenized_line.index(",")]
#     sentence_text=tokenized_line[tokenized_line.index(",")+4:-7]
#     sentence_ids.append(sentence_id)
#     sentence_texts.append(" ".join(sentence_text))
# #
# #
# #
# from collections.abc import Iterable
# def flatten_list(items,ignore_types=(str,bytes)):
#     for v in items:
#         if isinstance(v,Iterable) and not isinstance(v, ignore_types):
#             yield from flatten_list(v)
#         else:
#             yield v
#
# flattened_texts=list(flatten_list(sentence_texts))
# flattened_ids=list(flatten_list(sentence_ids))
# #
# # print(len(flattened_ids))
# # print(len(flattened_texts))
#
#
# np.savetxt("ids_test_new",flattened_ids,delimiter=",",fmt="%s")
# np.savetxt("sentences_test_new",flattened_texts,delimiter=",",fmt="%s")

