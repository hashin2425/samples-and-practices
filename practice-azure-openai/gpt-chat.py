import os
import time

from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_version=os.environ["GPT_CHAT_API_VERSION"],
    api_key=os.environ["GPT_CHAT_API_KEY"],
    azure_endpoint=os.environ["GPT_CHAT_AZURE_ENDPOINT"],
)

started_time = time.time()

response = client.chat.completions.create(
    model=os.environ["GPT_CHAT_MODEL"],
    messages=[
        {"role": "user", "content": "あなたは何の自然言語処理モデルですか？"},
    ],
)

print(response.choices[0].message.content)

print("---------------------------------------------------------")
print(f"処理時間: {time.time() - started_time:.2f} sec")

# 使用トークン数
print(f"プロンプトトークン数: {response.usage.prompt_tokens}")
print(f"完了トークン数: {response.usage.completion_tokens}")
print(f"合計トークン数: {response.usage.total_tokens}")

# 各応答に割り当てられる一意の識別子
print(f"ID: {response.id}")

# 使用されたGPTモデルの名称
print(f"モデル: {response.model}")

# 作成時刻（UNIXタイムスタンプ）
print(f"作成時刻: {response.created}")

# 応答生成が終了した理由（例：'stop'は正常終了）
print(f"終了理由: {response.choices[0].finish_reason}")

# コンテンツフィルター結果（hate, self_harm, sexual, violence）
for category, result in response.choices[0].content_filter_results.items():
    print(f"コンテンツフィルター {category}： {result}")

# プロンプトフィルター結果（hate, self_harm, sexual, violence）
for result in response.prompt_filter_results:
    print(f"プロンプトフィルター結果: {result}")
