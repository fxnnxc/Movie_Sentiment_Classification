import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np

def calculateSent(script_list):
    sent_list = []
    senti_analyzer = SentimentIntensityAnalyzer()
    for i in script_list:
        score = senti_analyzer.polarity_scores(i)['compound']
        sent_list.append(score)
    return sent_list


def moving_average(sent_list):
    averaged = []
    for index, sent in enumerate(sent_list):
        if (index > 3):
            averaged.append(np.mean(sent_list[index - 3] * 0.25
                                    + sent_list[index - 2] * 0.35
                                    + sent_list[index - 1] * 0.5
                                    + sent_list[index]))
        else:
            averaged.append(sent)
    return averaged


def get_main_actors(script):

    Actor_count = {}
    remove_list = ['CAMERA', 'END', 'DISSOLVE']
    for s in script:
        actor = re.findall('[A-Z]{3,}', s)
        if len(actor) == 1:
            if actor[0] in Actor_count:
                Actor_count[actor[0]] += 1
            else:
                Actor_count[actor[0]] = 1
    return [key for key in Actor_count.keys() if Actor_count[key] >10 and key not in remove_list ]


def get_flow(script, actor_list):
    speaker = []
    saying = []
    isSaying = False
    findNewOne = True
    temp = ""
    cur_actor = ""
    for s in script:
        if isSaying:
            if "<b>" in s:
                temp = re.sub('[\t\n(<b/>)\'\"]' ,"" ,temp)
                temp = re.sub('\s{2,' ," ", temp)
                speaker.append(cur_actor)
                saying.append(temp)
                isSaying = False
                findNewOne = True
                temp = ""
            else:
                temp = temp + s

        if findNewOne:
            actor = re.findall('[A-Z]{3,}', s)
            if actor and actor[0] in actor_list:
                cur_actor = actor[0]
                isSaying = True
                findNewOne = False
    return speaker, saying


from os import listdir
from os.path import isfile, join
from pandas import HDFStore
import pandas as pd

def make_df_file():
    path = '../data/'
    remove_list = ['CAMERA', 'END', 'DISSOLVE', 'CUT']
    files = [f for f in listdir(path) if isfile(join(path, f))]
    for f in files:
        script = list(open(path+f, 'r', encoding='utf-8'))
        act_list = get_main_actors(script)
        speaker, sentence = get_flow(script, act_list)
        # Evaluate Sentimet
        value = calculateSent(sentence)
        value = moving_average(value)
        hdf = HDFStore('../processed_data/'+f[0:-4]+'.h5')
        hdf.put('d1', pd.DataFrame({'speaker':speaker, 'value':value}), format='table', data_columns=True)
        hdf.close()
        print("Store ", f)

make_df_file()