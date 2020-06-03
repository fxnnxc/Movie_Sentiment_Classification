# Movie_Sentiment_Classification




-----------------------------------------------

## Intro 

영화에 대하여 사람들은 리뷰를 적고 거기에는 긍정 혹은 부정으로 평가할 수 있는 요소가 있습니다. 여기서는 영화리뷰 데이터에 대하여
Domain-Specific Dictionary를 생성하는 방법을 알아보고 데이터에 대한 모델을 만들어 자연어에 대한 긍정 혹은 부정으로 분류하는 모델을
만들어보겠습니다. 

## 1. Data

Kaggle에서는 IMDB 영화 사이트에서 제공하는 영화 리뷰에 대한 5 만개의 리뷰가 있습니다. 
[데이터 이미지]


## 2. Domain-specific dictionary

도메인 맞춤 사전을 만들기 위한 알고리즘은 다음과 같습니다. 

1. 문장을 정제합니다.  
2. 문장별로 단어를 카운팅해서 전체 딕셔너리를 만듭니다. 
3. 전체 단어에 대한 Counting 사전은 사이즈가 크기 때문에 나타난 빈도가 일정범위에 들어가는 Small 사전을 만듭니다. 
4. Small 단어 사전을 통해서 50000개의 문장을 다시 Count해서 X Matrix를 만듭니다. 
5. X metrix와 y_label에 대하여 OLS(Ordinal Least Square)를 합니다. 
6. 해당 계수는 단어의 가중치를 나타내며, 긍정에 가까울 경우 값이 큰 양수로, 부정에 가까울 경우 값이 작은 음수로 나타납니다. 


* Counting of words by smaller Dictionary

|| happy | sad| ... | Good| y|
|---|---|---|---|---| ---|
 X1| 4 |3|2|0|  0
 X2| 0 |2|5|1| 1
 X3| 2 |3|8|9|   0
 X4| 1 |2|2|1| 0
 

## 3. Train 



## 4. Results

![image](training.png)

|Hypothesis| Number Of Words |SVC | GNB |DT|RF |
|---|---|---|---|---|---|
|All words|223234|NaN|NaN|NaN|NaN| 
|0.001S ~ S|10959|0.865|0.732|0.721|0.849|
|0.002S ~ S|6769|0.870|0.748|0.718|0.844|
|0.003S ~ S|5042|0.873|0.763|0.718|0.844|
|0.004S ~ S|4052|0.874|0.779|0.716|0.844|
|0.005S ~ S|3355|0.874|0.778|0.711|0.841|
|0.006S ~ S|2911|0.874|0.788|0.715|0.838|
|0.007S ~ S|2592|0.872|0.788|0.715|0.833|
|0.008S ~ S|2307|0.870|0.785|0.713|0.833|
|0.009S ~ S|2095|0.868|0.789|0.713|0.836|
|0.010S ~ S|1901|0.868|0.789|0.715|0.834|
|0.011S ~ S|1751|0.868|0.796|0.712|0.833|
|0.012S ~ S|1635|0.866|0.799|0.710|0.831|
|0.013S ~ S|1529|0.869|0.803|0.708|0.832|
|0.014S ~ S|1426|0.866|0.808|0.709|0.834|
|0.015S ~ S|1346|0.864|0.810|0.708|0.827|
|0.016S ~ S|1272|0.861|0.811|0.709|0.830|
|0.017S ~ S|1206|0.860|0.813|0.710|0.825|
|0.018S ~ S|1148|0.858|0.815|0.708|0.826|
|0.020S ~ S|1057|0.856|0.813|0.710|0.825|
|0.023S ~ S|947 |0.855|0.814|0.705|0.829|
|0.025S ~ S|876 |0.852|0.811|0.703|0.821|
|0.030S ~ S|739 |0.846|0.804|0.701|0.814|
|0.040S ~ S|550 |0.837|0.802|0.697|0.809|
|0.050S ~ S|450 |0.828|0.790|0.696|0.799|
