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
 
 * 가중치
 
  || happy | sad| ... | Good|
 |---|---|---|---|---| 
 weight| 2 |-2|...|3|



## 3. Train 



## 4. Results
