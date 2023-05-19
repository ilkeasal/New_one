# import nltk
import tokenize

from tqdm import tqdm
import pickle
import json
import jsonlines
# nltk.download('punkt')
import numpy as np

# mysentences = '/project/dmg_data/MMdata/COCO-VIST-final.txt_stratified_SENTS_100.filter_size=2278.pickle'
# myvocab = '/project/dmg_data/MMdata/unique-words-filtered-2278.txt'
# myimages = '/project/dmg_data/MMdata/img_ids_all.txt'
# myindexes = '/project/dmg_data/MMdata/COCO-VIST-final.txt_INDEXES_100.filter_size=2278.txt'
# myjsonl = '/project/dmg_data/MMdata/coco-vist_ann.jsonl'

def get_vocab(vocabtxt):
    vlist = []
    with open(vocabtxt, 'r') as vocab:
        content = vocab.readlines()
        for v in content:
            v = v.strip()
            vlist.append(v)
        vlists = set(vlist)
    return vlists

def get_indexes(idxtxt):
    idlist = []
    with open(idxtxt, 'r') as indexes:
        content = indexes.readlines()
        for idx in content:
            idx = idx.strip().split('-')
            if len(idx)==4:
                # print(idx, 'vist')
                mykey = 'v_'
                image = str(idx[2])
            elif len(idx)==3:
                # print(idx, 'coco')
                mykey = 'c_'
                imagef = str(idx[1])
                image = str(imagef.zfill(12))
            fullidx = mykey+image
            idlist.append(fullidx)
    return idlist


def read_sentences(pklfile,sent_idx_list,img_idx_list,save_path):
    data = pickle.load(open(pklfile, 'rb'))
    # freq_list = []
    with jsonlines.open(save_path, mode='w') as writer:
        for elem, s in tqdm(list(enumerate(data))):
            sentences = []
            if sent_idx_list[elem] in img_idx_list:
                # save the datapoint
                # with jsonlines.open(save_path, mode='w') as writer:
                # sentences = []
                sentences.append(s.strip()[1:-1]) # to get rid of double quotes
                img_id = str(sent_idx_list[elem])
                name = str(img_id.split('_')[1])
                d = {'sentences': sentences, 'id': img_id, 'img_path': img_id} # TODO: was img_path: name
                # print(d)
                writer.write(d)
                # we can also compute stats on frequency of words

# def main():
#     vocablist = get_vocab(myvocab)
#     print('length my vocabulary:',len(vocablist))
#     imglist = get_vocab(myimages)
#     print('length my image indexes:',len(imglist))
#     idxlist = get_indexes(myindexes)
#     print('length my sentence indexes:', len(idxlist))
#     read_sentences(mysentences,idxlist,imglist,myjsonl)


# if __name__ == '__main__':
#     main()



def read_file(file):
    texts=[]
    for word in file:
        text=word.rstrip('\n')
        texts.append(text)
    return texts

###MY ADJUSTED GET_INDEXES FUNCTION###

def getting_indexes(idxtxt): #this is the adjusted function.
    idlist = []
    for idx in idxtxt:
        idx = idx.strip().split('-')
        if len(idx)==4:
            # print(idx, 'vist')
            mykey = 'v_'
            image = str(idx[2])
        elif len(idx)==3:
            # print(idx, 'coco')
            mykey = 'c_'
            imagef = str(idx[1])
            image = str(imagef.zfill(12))
        fullidx = mykey+image
        idlist.append(fullidx)
    return idlist
#
# new_idx=getting_indexes(unique_ids_corrected)
# print(new_idx)
#
# print(type(new_idx))

#np.savetxt("c_v_indexes.csv",new_idx,delimiter=",",fmt="%s")
#
# sentence_ids_texts_df=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/sentence_ids_texts_df copy.csv").readlines()
#
#
#
# sentence_ids_texts_corrected=read_file(sentence_ids_texts_df)
#
#
#
# for line in sentence_ids_texts_corrected:
#     print(line)
#
#
# print(len(np.unique(sentence_ids_texts_corrected)))
# print(len(sentence_ids_texts_corrected))
#
# print(len(new_idx))
# print(len(np.unique(sentence_ids_texts_corrected)))
#
# print(type(sentence_ids_texts_corrected))

# import pandas as pd
# coco_vist_pickle =pd.read_pickle(r'/Users/ilkeasal/Downloads/COCO-VIST-final.txt_stratified_SENTS_100.filter_size=2278.pickle')
#
# coco_vist_pickle_corrected=read_file(coco_vist_pickle)

#print(coco_vist_pickle_corrected) #this is just the sentences.

# print(len(coco_vist_pickle_corrected))
#
# coco_vist_indexes_not_mine_delete_later=open("/Users/ilkeasal/Desktop/Coco_Vist_Final_Delete_Later.txt").readlines()
#
# #print(coco_vist_indexes_not_mine_delete_later)
#
# coco_vist_indexes_not_mine_delete_later_corrected=read_file(coco_vist_indexes_not_mine_delete_later)
# print(len(coco_vist_indexes_not_mine_delete_later_corrected))



import nltk

from nltk import word_tokenize

import untokenize
#
# sentences_id=[]
# for line in sentence_ids_texts_corrected:
#     tokenized_line=word_tokenize(line)
#     sentence_id = tokenized_line[:tokenized_line.index(',')]
#     sentence_text = tokenized_line[tokenized_line.index(',') + 4:-3]
#     sentences_id.append(sentence_id)
#
# print(sentences_id)

#np.savetxt("sentences_id.txt",sentences_id,delimiter=",",fmt="%s")

# sentences_may=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/sentences_from_sentence_ids_texts_df.txt").readlines()
#
#
#
# sentences_may_corrected=read_file(sentences_may)
# print(sentences_may_corrected)
# print(len(sentences_may_corrected))
# print(len(np.unique(sentences_may_corrected)))



#I WILL CONVERT MY TOTAL_SUBSET_SENTENCES FILE TO A PICKLE FILE
file=open("/Users/ilkeasal/Desktop/Important_files_for_my_Internship/New_sentences_and_ids/total_subset_sentences.txt").readlines()


sentences_corrected=read_file(file)

#pickling :
print(type(sentences_corrected))

import pickle

with open("total_subset_sentences.pkl","wb") as sentencepickle:
    pickle.dump(sentences_corrected,sentencepickle)