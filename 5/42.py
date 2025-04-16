import google.generativeai as genai
from dotenv import load_dotenv
import os
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')

# プロンプトの準備
df = pd.read_csv("./JMMLU/JMMLU/high_school_geography.csv",names=["ques","A","B","C","D","ans"], header=None, encoding="utf-8")
all_label = list(df["ans"])

def main(i):
    prompt = f"次の150個の問いに答えなさい。選択肢から正しいものを1つ選び、回答はA/B/C/Dのいずれかのみとしてください。\n"
    for ind,row_dict in enumerate(df.to_dict(orient="records")):
        prompt_mono = f"{ind+1}：{row_dict["ques"]}  A：{row_dict["A"]}  B：{row_dict["B"]}  C：{row_dict["C"]}  D：{row_dict["D"]}\n"
        prompt += prompt_mono

    # レスポンスの取得
    response = model.generate_content(prompt)
    print(response.text)

    # 正解率の計算
    all_pred = [_[-1] for _ in response.text.strip().split("\n")]
    accuracy = accuracy_score(all_pred, all_label)
    print(f"正解率: {accuracy:.2%}")

    with open(f"42_result_{i}.txt", "w") as f:
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

# 結果
# 0:accuracy:0.8733333333333333
# 1:accuracy:0.88
# 2:accuracy:0.8666666666666667
# 3:accuracy:0.88
# 4:accuracy:0.8666666666666667
# average:0.8733333333333334