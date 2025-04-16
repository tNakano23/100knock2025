import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown
from dotenv import load_dotenv
import os

# def to_markdown(text):
#   text = [_.replace('•', '*') for _ in text.split('\n')]
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


load_dotenv()  # .env ファイルを読み込む
api_key = os.getenv("API_KEY")

genai.configure(api_key=api_key)

# モデルを準備
model = genai.GenerativeModel('gemini-1.5-flash')
prompt = "9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。\
ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。\
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。\
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。\
"

response = model.generate_content(prompt)
print(response.text)


"""
正答は イ→ウ→ア です。

* **イ 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。**  嵯峨天皇の治世は809年から823年。藤原冬嗣は806年に蔵人頭に任命されているため、この出来事は9世紀前半に発生しています。

* **ウ 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。** 承和の変は842年。その後の良房の台頭により北家が優位に立つようになったので、イより後の出来事です。

* **ア 藤原時平は，策謀を用いて菅原道真を政界から追放した。**  菅原道真の左遷は894年。これは承和の変や藤原冬嗣の蔵人頭就任より後の出来事です。


よって、年代順に並べると イ→ウ→ア となります。
"""