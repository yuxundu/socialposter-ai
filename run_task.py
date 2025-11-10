import os
import json
from openai import OpenAI
from skyvern import Skyvern

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
SKYVERN_API_KEY = os.getenv("SKYVERN_API_KEY")
TARGET_PLATFORM = os.getenv("TARGET_PLATFORM", "twitter")

openai_client = OpenAI(api_key=OPENAI_API_KEY)
skyvern = Skyvern(api_key=SKYVERN_API_KEY)

with open("prompts/social_post_templates.json", "r", encoding="utf-8") as f:
    templates = json.load(f)

def generate_post(prompt_topic: str, platform: str = "twitter") -> str:
    system_prompt = templates[platform]["system"]
    user_prompt = templates[platform]["user"].replace("{topic}", prompt_topic)

    completion = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return completion.choices[0].message.content.strip()

def execute_post_with_skyvern(post_text: str, platform: str):
    task_prompt = f"Open {platform}.com, log in, and post the following text:\n\n{post_text}"
    task = skyvern.run_task(prompt=task_prompt)
    print("[Skyvern] Executing browser task...")
    print(task)

if __name__ == "__main__":
    topic = input("💡 请输入发帖主题: ")
    print(f"[SocialPoster] Generating post for {TARGET_PLATFORM}...")
    post = generate_post(topic, TARGET_PLATFORM)
    print(f"\n✅ 生成的文案:\n{post}\n")

    confirm = input("是否让 Skyvern 自动发帖？(y/n): ")
    if confirm.lower() == "y":
        execute_post_with_skyvern(post, TARGET_PLATFORM)
    else:
        print("已取消执行。")
