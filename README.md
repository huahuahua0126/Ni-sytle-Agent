# Ni-Style Agent

<div align="center">

![Ni-Style Agent](https://img.shields.io/badge/Ni--Style-Agent-blue?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Python-3.8%2B-green?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688?style=for-the-badge&logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**深度技术文章生成器 · 哲学视角 · 逻辑重构**

[功能特性](#功能特性) • [快速开始](#快速开始) • [工作流程](#工作流程) • [技术栈](#技术栈)

</div>

---

## 📖 简介

**Ni-Style Agent** 是一个基于通义千问（Qwen）API 的 AI 写作代理。它不仅仅是一个文章生成器，更是一个技术思想的重铸者。它能够将普通的技术话题，通过结构化的思考和哲学化的视角，转化为具有深度、逻辑严密且风格独特的“技术哲学”随笔。

## ✨ 功能特性

- **🧠 智能大纲构建**
  - 基于用户输入的标题，自动分析并生成 5 步逻辑结构的详细大纲。
  - 涵盖现状铺垫、核心陷阱、问题根源、破局思路及未来展望。

- **📝 深度初稿撰写**
  - 基于大纲生成内容详实的技术文章。
  - 自动引用行业真实案例，确保内容的落地性与丰富度。

- **🎨 风格重铸 (Ni-Style)**
  - **去情绪化**：剔除冗余的软性连接词，保持冷静客观。
  - **高密度逻辑**：确保每一句话都承载有效信息。
  - **哲学视角**：将技术问题上升到认知模型或熵增等哲学高度。
  - **连续流体验**：减少列表式表达，使用段落推进观点，形成流畅的阅读体验。

- **🤖 多模型支持**
  - 默认集成阿里云通义千问 (Qwen-Max) 模型，支持高并发与长文本处理。

## 🚀 快速开始

### 前置要求

- Python 3.8+
- Git
- [阿里云通义千问 API Key](https://dashscope.aliyuncs.com/)

### 1. 克隆仓库

```bash
git clone https://github.com/huahuahua0126/Ni-sytle-Agent.git
cd Ni-sytle-Agent
```

### 2. 环境配置

建议使用 Python 虚拟环境来管理依赖，以避免污染系统环境：

```bash
# 创建虚拟环境
python3 -m venv .venv

# 激活虚拟环境 (macOS/Linux)
source .venv/bin/activate

# 激活虚拟环境 (Windows)
# .venv\Scripts\activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置 API 密钥

1. 复制示例配置文件：
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env` 文件，填入你的 API 密钥：
   ```env
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   ```

### 5. 运行项目

启动 FastAPI 服务：

```bash
# 确保虚拟环境已激活
uvicorn main:app --reload
```

或者直接使用虚拟环境中的 Python 运行（无需手动激活）：

```bash
.venv/bin/python -m uvicorn main:app --reload
```

服务启动后，打开浏览器访问：[http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🔄 工作流程

1.  **输入主题**：在首页输入你想探讨的技术话题（例如：“微服务架构的熵增困境”）。
2.  **生成大纲**：点击“开始创作”，Agent 会首先生成一份结构化大纲。
3.  **生成初稿**：确认大纲无误后，Agent 会撰写一篇详细的初稿。
4.  **风格润色**：最后，Agent 会对初稿进行“Ni-Style”重写，输出最终的哲学化技术文章。

## 🛠️ 技术栈

- **后端框架**: [FastAPI](https://fastapi.tiangolo.com/) - 高性能 Python Web 框架
- **服务器**: [Uvicorn](https://www.uvicorn.org/) - ASGI 服务器
- **AI SDK**: [OpenAI Python SDK](https://github.com/openai/openai-python) (兼容通义千问 API)
- **前端**: 原生 HTML5 / CSS3 / JavaScript (轻量级交互)

## 📄 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！如果你有更好的 Prompt 策略或功能建议，请随时分享。

## 👨‍💻 作者

**huahuahua0126**

---

<div align="center">
Made with ❤️ by Ni-Style Agent Team
</div>
