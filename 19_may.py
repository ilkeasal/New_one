
import numpy as np
import nltk
from nltk import word_tokenize
def read_file(file):
    texts=[]
    for word in file:
        text=word.rstrip('\n')
        texts.append(text)
    return texts
ids_sentences_newdf=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/ids_sentences_newdf.csv").readlines()



ids_sentences_newdf_corrected=read_file(ids_sentences_newdf)


unique_ids_sentences_newdf=(np.unique(ids_sentences_newdf_corrected))


unique_ids_sentences_newlisted=(list(unique_ids_sentences_newdf))

print(len(unique_ids_sentences_newlisted))


unique_ids_new_df=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/Newly_created_files/unique_ids_from_new_df").readlines()

print(len(unique_ids_new_df))

unique_texts_new_df=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/Newly_created_files/unique_sentences_from_new_df").readlines()

print(len(unique_texts_new_df))


print(len(np.unique(unique_ids_sentences_newlisted)))


sent = open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/sentences_test_new").readlines()
id=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/ids_test_new").readlines()

print(len(sent))
print(len(id))