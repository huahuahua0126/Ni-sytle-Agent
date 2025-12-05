# Ni-Style Agent

一个基于通义千问（Qwen）API的AI写作代理，用于生成技术文章并进行风格重铸。

## 功能特性

- **文章大纲生成**：根据标题自动生成结构化的技术文章大纲
- **初稿撰写**：基于大纲生成详细的技术文章内容
- **风格重铸**：将文章重写为冷静、哲学化的技术风格
- **通义千问集成**：使用阿里云通义千问API，支持多种模型

## 安装要求

- Python 3.8+
- pip

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/huahuahua0126/Ni-sytle-Agent.git
cd Ni-sytle-Agent
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置

1. 创建 `.env` 文件：
```bash
cp .env.example .env
```

2. 在 `.env` 文件中配置你的通义千问API密钥：
```
OPENAI_API_KEY=your_qwen_api_key_here
```

> **注意**：需要从[阿里云控制台](https://dashscope.aliyuncs.com/)获取API密钥

## 使用方法

运行服务（FastAPI + 前端）：
```bash
uvicorn main:app --reload
```

## 工作流程

1. **大纲构建**：分析标题，生成5步结构大纲
2. **初稿撰写**：基于大纲写出详细内容
3. **风格重铸**：转换为冷静、逻辑密集的技术哲学风格

## 依赖包

- fastapi
- uvicorn
- openai
- python-dotenv

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 作者

huahuahua0126
