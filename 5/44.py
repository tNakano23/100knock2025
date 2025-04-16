import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。
"""

response = model.generate_content(prompt)
print(response.text)




# """
# 出力
# つばめちゃんが間違えて急行に乗車し、自由が丘の次の急行停車駅で降りたということは、それは大井町線では**二子玉川**駅です。そこから反対方向の電車で一駅戻ると、目的地の駅は**九品仏**駅になります。
# """