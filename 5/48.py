import google.generativeai as genai
from dotenv import load_dotenv
import os
import numpy as np
import pandas as pd
from sklearn.preprocessing  import StandardScaler

# -----------------------------------------------------------------------------
# 実験設定
# replace("A","ア").replace("B","イ").replace("C","ウ").replace("D","エ")
# -----------------------------------------------------------------------------


load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')
score = [[] for _ in range(10)]

# print(score)
def main(i):
    prompt = """
    あなたはサラリーマン川柳の評価者（ジャッジ）です。次の10個の川柳の面白さをそれぞれ10段階で評価せよ。
    なお、回答は1~10のいずれかのみとしてください。

    1. 残業代より　睡眠不足が　体に堪える

    2. 社内恋愛　噂は風より　早く回る

    3. 承認待ちの　メール見てはため息　つく毎日

    4. 年末調整　計算複雑で　頭が痛い

    5. 新人研修　説明長すぎ　眠気襲う

    6. ホットコーヒー　冷めるより早く　会議終了

    7. 忘年会の　景品争奪戦　白熱する

    8. 定時退社は　夢の中だけ　現実逃避

    9. プレッシャーで　胃がキリキリと　鳴り響く

    10.  週末休み　充電完了で　また来週頑張る
    """
    response = model.generate_content(prompt)
    print(response.text)
    response_text = [int(_.split(". ")[-1]) for _ in response.text.strip().split("\n")]
    return response_text

if __name__ == "__main__":
    score = []
    for i in range(10):
        score_mono = main(i)
        score.append(score_mono)

        # for ind,score_sub in enumerate(score):
        #     score_sub.append(score_mono[ind])

    print(score)
    X = np.array(score)
    print("分散:", np.var(X, axis=0, ddof=0))


# """

# [[7, 6, 8, 5, 7, 8, 6, 9, 7, 4],
#  [7, 6, 8, 5, 7, 9, 6, 8, 7, 4], 
#  [7, 6, 8, 5, 7, 9, 6, 8, 7, 4], 
#  [7, 6, 8, 5, 7, 8, 6, 9, 7, 4], 
#  [7, 6, 8, 5, 7, 9, 6, 8, 7, 4], 
#  [7, 6, 8, 5, 7, 8, 6, 9, 7, 4], 
#  [7, 6, 8, 5, 7, 9, 6, 8, 7, 4], 
#  [8, 7, 9, 6, 7, 8, 6, 9, 7, 5], 
#  [7, 6, 8, 5, 7, 8, 6, 9, 7, 4], 
#  [7, 6, 8, 5, 7, 9, 6, 8, 7, 4]]


# 分散: [0.09 0.09 0.09 0.09 0.   0.25 0.   0.25 0.   0.09]


# """