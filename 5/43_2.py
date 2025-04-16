import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from dotenv import load_dotenv
import os

# -----------------------------------------------------------------------------
# 実験設定
# replace("A","ア").replace("B","イ").replace("C","ウ").replace("D","エ")
# かつ
# "temperature": 1.6, 
# -----------------------------------------------------------------------------

# def to_markdown(text):
#   text = [_.replace('•', '*') for _ in text.split('\n')]
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')

# プロンプトの準備
df = pd.read_csv("./JMMLU/JMMLU/high_school_geography.csv",names=["ques","A","B","C","D","ans"], header=None, encoding="utf-8")
all_label = list(df["ans"])

def main(i):
    prompt = f"次の150個の問いに答えなさい。選択肢から正しいものを1つ選び、回答はア/イ/ウ/エのいずれかのみとしてください。\n"
    for ind,row_dict in enumerate(df.to_dict(orient="records")):
        prompt_mono = f"{ind+1}：{row_dict["ques"]}  ア：{row_dict["A"]}  イ：{row_dict["B"]}  ウ：{row_dict["C"]}  エ：{row_dict["D"]}\n"
        prompt += prompt_mono

    # レスポンスの取得
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 1.6,   # ← ここで設定
            # "top_p": 1.0,         # （任意）確率のカットオフ
            # "top_k": 0,           # （任意）上位何トークンに絞るか
            }
        )
    print(response.text)

    # 正解率の計算
    response_text = response.text.replace("ア","A").replace("イ","B").replace("ウ","C").replace("エ","D")
    all_pred = [_[-1] for _ in response_text.strip().split("\n")]
    accuracy = accuracy_score(all_pred, all_label)
    print(f"正解率: {accuracy:.2%}")

    with open(f"43_2_result_{i}.txt", "w") as f:
        for pred, label in zip(all_pred, all_label):
            f.write(f"{pred}\t{label}")
            if pred == label :
                f.write(f"\tTrue")
            f.write(f"\n")
        f.write(f"accuracy:{accuracy}")


    return accuracy


if __name__ == "__main__":
    all_acc = []
    for i in range(5):
        acc = main(i)
        all_acc.append(acc)

    for ind,_ in enumerate(all_acc):
        print(f"{ind}:accuracy:{_}")
    print(f"average:{np.mean(all_acc)}")



# 正解率: 86.67%
# 0:accuracy:0.8733333333333333
# 1:accuracy:0.8733333333333333
# 2:accuracy:0.8666666666666667
# 3:accuracy:0.8733333333333333
# 4:accuracy:0.8666666666666667
# average:0.8706666666666667