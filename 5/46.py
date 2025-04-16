import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = """
サラリーマン川柳を10個作ってください
"""
response = model.generate_content(prompt)
print(response.text)



# """
# 1. 残業代より　睡眠不足が　体に堪える

# 2. 社内恋愛　噂は風より　早く回る

# 3. 承認待ちの　メール見てはため息　つく毎日

# 4. 年末調整　計算複雑で　頭が痛い

# 5. 新人研修　説明長すぎ　眠気襲う

# 6. ホットコーヒー　冷めるより早く　会議終了

# 7. 忘年会の　景品争奪戦　白熱する

# 8. 定時退社は　夢の中だけ　現実逃避

# 9. プレッシャーで　胃がキリキリと　鳴り響く

# 10.  週末休み　充電完了で　また来週頑張る
# """