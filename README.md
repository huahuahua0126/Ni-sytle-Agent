# Ni-Style Agent

一个基于通义千问（Qwen）API的AI写作代理，用于生成技术文章并进行风格重铸。

## 功能特性

- **文章大纲生成**：根据标题自动生成结构化的技术文章大纲
- **初稿撰写**：基于大纲生成详细的技术文章内容
- **风格重铸**：将文章重写为冷静、哲学化的技术风格
- **通义千问集成**：使用阿里云通义千问API，支持多种模型

## 快速开始

### 前置要求

- Python 3.8+
- Git

### 1. 克隆仓库

```bash
git clone https://github.com/huahuahua0126/Ni-sytle-Agent.git
cd Ni-sytle-Agent
```

### 2. 环境配置

建议使用 Python 虚拟环境来管理依赖：

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

2. 编辑 `.env` 文件，填入你的阿里云通义千问 API 密钥：
   ```
   OPENAI_API_KEY=your_qwen_api_key_here
   ```
   > **注意**：需要从[阿里云控制台](https://dashscope.aliyuncs.com/)获取API密钥

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

## 工作流程

1. **大纲构建**：输入文章标题，AI 分析并生成5步结构大纲。
2. **初稿撰写**：基于生成的大纲，AI 撰写详细的技术文章初稿。
3. **风格重铸**：将初稿转换为冷静、逻辑密集的技术哲学风格（Ni-Style）。

## 技术栈

- **后端**：FastAPI, Uvicorn, OpenAI SDK (适配 Qwen)
- **前端**：HTML, CSS, JavaScript
- **模型**：Qwen-Max (通义千问)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 作者

huahuahua0126
