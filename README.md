# 🚀 SocialPoster.AI

让 AI 自动登录、生成并发布你的社交内容。  
集成 GPT（生成）+ Skyvern（浏览器执行）= 一键自动发帖机器人。

---

## 🌟 核心功能
- ✍️ AI 自动生成社交文案（支持 Twitter、LinkedIn、小红书等风格）
- 🌐 Skyvern 浏览器执行器自动登录网页并发布内容
- 📅 支持定时发布、草稿保存、发帖日志
- 🧠 可扩展为多平台内容调度系统

---

## ⚙️ 安装步骤

```bash
git clone https://github.com/<yourname>/socialposter-ai.git
cd socialposter-ai
pip install -r requirements.txt
```

---

## 🧩 运行示例

```bash
python run_task.py
```

示例输出：
```
[SocialPoster] Generated post for Twitter:
"今日学习笔记：AI 执行器真的能替你发帖了 🤖✨"
[Skyvern] Executing browser workflow...
✅ Post published successfully!
```

---

## 🌐 环境变量配置

```bash
OPENAI_API_KEY=sk-xxxx
SKYVERN_API_KEY=sky-xxxx
CHROME_EXECUTABLE_PATH=/Applications/Google Chrome.app/Contents/MacOS/Google Chrome
TARGET_PLATFORM=twitter
```

---

## 💡 技术栈
- Python 3.11+
- OpenAI / Claude / Gemini API
- Skyvern (browser executor)
- JSON prompt templates
- Docker (可选)

---

## 🧭 路线图
- ✅ MVP：支持单平台（Twitter）
- ⏳ v0.2：LinkedIn / 小红书发帖
- 🔁 v0.3：定时任务 + Web 控制台
- ☁️ v1.0：云部署 + 团队管理后台

---

> © 2025 Yuxun Du (James)  
> Open Source License: MIT
