# day 41

## 자연어 생성

### 준단어 토큰화

#### BPE 알고리즘 (Byte Pair Encoding)

준단어를 이용하여 자주 나오지 않는(rare) 단어에 대한 훈련을 하는 알고리즘

기존 번역에서는 고정된 단어집을 사용하여 새로운 단어(미등록어)가 계속해서 나오는 단점을 가진다.

간단하고 효과적인 방법으로, 준단어로 바꾼다. 이름이나 복합어는 다양한 단어를 기존의 단어보다 작은 단위로 번역이 가능하다. 이를 분리하여 각각 따로 번역을 하고 합치는 방식을 사용한다. 동적어나 빌려온 단어를 모두 준단어를 사용한다.

다른 방법들과 비교하여 보았을 때 번역 성능이 향상된다.

+ BPE 알고리즘

  1. 공백을 기준으로 단어를 구분
  2. 각 단어의 빈도를 계산
  3. 가장 많이 나오는 글자 조합을 세어 어휘에 추가
  4. 어휘 수가 정해진 크기에 도달할 때까지 반복

+ 예

  다음과 같이 데이터가 있다.

  | 단어    | 빈도 |
  | ------- | ---- |
  | h u g   | 10   |
  | p u g   | 5    |
  | p u n   | 12   |
  | b u n   | 4    |
  | h u g s | 5    |

  토큰은 : b, g, h, n, p, s, u 총 7개

  1. 토큰 개수를 총 10개까지로 설정한다면, u+g는 10 + 5 + 5 = 20 이므로 ug를 추가

  2. 토큰은 b, g, h, n, p, s, u, ug 총 8개

     | 단어   | 빈도 |
     | ------ | ---- |
     | h ug   | 10   |
     | p ug   | 5    |
     | p u n  | 12   |
     | b u n  | 4    |
     | h ug s | 5    |

  3. u + n 은 12 + 4 = 16 이므로, un을 추가

     | 단어   | 빈도 |
     | ------ | ---- |
     | h ug   | 10   |
     | p ug   | 5    |
     | p un   | 12   |
     | b un   | 4    |
     | h ug s | 5    |

  4. 토큰 : b, g, h, n, p, s, u, ug, un 총 9개

  5. h + ug 는 10 + 5 = 15 이므로 hug를 추가

     | 단어  | 빈도 |
     | ----- | ---- |
     | hug   | 10   |
     | p ug  | 5    |
     | p un  | 12   |
     | b un  | 4    |
     | hug s | 5    |

  6. 토큰 : b, g, h, n, p, s, u, ug, un, hug 총 10개

#### Byte-Level BPE

+ 다국어 처리를 할 경우에는 글자가 매우 다양하다.
+ 유니코드에서 2~3바이트로 구성
+ 글자 대신 바이트를 기본 토큰으로 준단어토큰화를 할 경우 모든 문자를 256개의 토큰의 조합으로 표시할 수 있다.

+ 예) A = U+0041, 한 =>U+D55C (U+는 유니코드라는 의미)

  16진수 2자리 = 8비트 = 1바이트

+ BPE와 기본 알고리즘은 같으나, 토큰의 개수가 256개로 줄어든다. 아무리 많은 나라의 언어를 지원한다 하더라도 모든 언어에 처리가능하다.

+ 1바이트는 데이터로서 의미가 없을 수 있기 때문에 성능저하를 일으키는 요인이 될 수도 있다.

#### WordPiece

+ 구글 음성 검색과 번역기에 사용

+ 데이터의 우도(likelihood)를 가장 높이는 조합을 찾는다.

+ 우도란 주어진 조건에서 데이터가 발생할 확률이다.

+ 데이터 : a b a b c

  | 토큰 | a    | b    | c    |
  | ---- | ---- | ---- | ---- |
  | 확률 | 0.4  | 0.4  | 0.2  |

  우도 : 0.00512

+ 데이터 : a b a b c

  | 토큰 | a    | b    | c    | ab   |
  | ---- | ---- | ---- | ---- | ---- |
  | 확률 |      |      | 0.33 | 0.66 |

  우도 : 0.148

+ 토큰을 만들어 데이터의 조합을 만드는 것이 우도를 높이는 방법이다.

#### SentencePiece

BPE나 WordPiece는 토큰화 전에 단어 단위로 구분되어있다고 가정한다. 이 경우 단어 구분이 어려우면 문제가 발생한다.

SentencePiece는 단어 구분이 어려운 언어 적용에 문제를 해결한다. 빈 칸을 별개의 토큰으로 취급한다, `_` 로 표시한다.



### 준단어 토큰화 실습

토크나이저 패키지를 설치한다. `!pip install tokenizers` 

#### 데이터 로드

챗봇 데이터를 활용하여 실습한다.

```python
import wget
wget.download("https://github.com/songys/Chatbot_data/raw/master/ChatbotData.csv")

import os
os.rename("ChatbotData.csv","chatbot.csv")

import pandas as pd
df = pd.read_csv("chatbot.csv")
```

#### BPE

+ 데이터를 `txt` 파일로 저장한다

  ```python
  with open("sample.txt","w",encoding="utf8") as f:
      for row in df.itertuples():
          f.write(row.Q + "\n")
          f.write(row.A + "\n")
  ```

+ 글자 단위의 토크나이징을 하는 패키지를 가져온다.

  ```python
  from tokenizers import CharBPETokenizer # 글자단위의 bpe 토크나이저
  ```

+ 토크나이징

  `lowercase` 가 `True` 이면 대소문자를 구분하지 않는다.

  `min_frequency` 는 단어가 최소 몇번 나와야 사전에 포함시킬지 결정하는 파라미터

  ```python
  bpe = CharBPETokenizer(lowercase=True)
  bpe.train(files="sample.txt",min_frequency=1, vocab_size=5000)
  ```

+ 자연어 인코딩

  ```python
  enc = bpe.encode("마스터듀얼은 재밌다")
  ```

  단어가 토큰화된다. 토큰화된 단어를 확인할 수 있다.

  `BPE` 는 단어 단위로 끊기 때문에 `</w>` 는 단어가 끝나는 지점을 의미한다.

  ```python
  enc.ids # [2659, 873, 620, 1031, 2250, 1006]
  enc.tokens # ['마스', '터', '얼', '은</w>', '재밌', '다</w>']
  ```

#### 풀어쓰기

`BPE` 와 같은 순서를 따른다.

```python
# 풀어쓰기, NFD를 사용한다.
import unicodedata
with open("decomposed.txt","w",encoding="utf8") as f:
    for row in df.itertuples():
        q = unicodedata.normalize("NFD",row.Q)
        f.write(q+"\n")
        a = unicodedata.normalize("NFD",row.A)
        f.write(a+"\n")
       
# bpe 모델 생성/학습    
bpe = CharBPETokenizer(lowercase=True)
bpe.train(files="decomposed.txt",min_frequency=1,vocab_size=5000)

# 인코딩
text = unicodedata.normalize("NFD","마스터듀얼은 재밌다")
enc = bpe.encode(text)

enc.ids # [1895, 667, 37, 70, 589, 208, 819, 1365]
enc.tokens # ['마스', '터', 'ᄃ', 'ᅲ', '얼', '은</w>', '재미', 'ᆻ다</w>']
```

#### Byte Level BPE

```python
from tokenizers import ByteLevelBPETokenizer

byte = ByteLevelBPETokenizer(lowercase=True)
byte.train(files = "sample.txt",min_frequency=1,vocab_size=5000)

enc = byte.encode("마스터듀얼은 재밌다")

enc.ids # [2115, 849, 2564, 222, 1684, 311, 2276, 294]
enc.tokens
```

#### WordPiece

```python
from tokenizers import BertWordPieceTokenizer

wp = BertWordPieceTokenizer(lowercase=True)
wp.train(files="sample.txt",min_frequency=1,vocab_size=5000)
enc = wp.encode("마스터듀얼은 재밌다")

enc.ids # [225, 293, 720, 135, 166, 3696, 229, 3349, 216]
enc.tokens # ['마', '##스', '##터', '##ᄃ', '##ᅲ', '##얼', '##은', '재밌', '##다']
```

#### Sentencepiece

```python
from tokenizers import SentencePieceBPETokenizer

sp = SentencePieceBPETokenizer()
sp.train(files="sample.txt", min_frequency = 1, vocab_size=5000)
enc = sp.encode("마스터듀얼은 재밌다")

enc.ids  # [1017, 558, 875, 623, 687, 1944, 227]
enc.tokens # ['▁마', '스', '터', '얼', '은', '▁재밌', '다']
```

