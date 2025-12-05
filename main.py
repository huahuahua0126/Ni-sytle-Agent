import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

# Configuration
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL_NAME = "qwen3-max"

# Initialize FastAPI
app = FastAPI(title="Ni Style Agent API")

# Initialize OpenAI Client
try:
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
        base_url=QWEN_BASE_URL
    )
except Exception as e:
    print(f"Warning: OpenAI client initialization failed: {e}")
    client = None

# --- Data Models ---

class TopicRequest(BaseModel):
    topic: str

class DraftRequest(BaseModel):
    topic: str
    outline: str

class PolishRequest(BaseModel):
    draft: str

# --- Prompts ---

OUTLINE_PROMPT = """
你是一个技术文章架构师。用户给出了一个标题，请根据以下逻辑结构，生成一份详细的文章大纲。

用户标题：{topic}

请严格按照以下 5 个步骤拆解：
1. **现状铺垫**：描述该技术/话题目前的宏观发展情况。
2. **核心陷阱**：指出当前遇到的核心问题或痛点。
3. **问题根源**：深度剖析为什么会出现这个问题。
4. **破局思路**：探讨目前的解决方案或方向调整。
5. **未来展望**：预测接下来的演变趋势。

输出要求：只输出大纲内容，不要寒暄。
"""

DRAFT_PROMPT = """
你是一个资深的技术观察者。请根据提供的【标题】和【大纲】，撰写一篇内容详实的技术文章。

标题：{topic}
大纲：
{outline}

写作要求：
1. **结合真实场景**：文中请引用行业内真实存在的框架或技术作为论据。
2. **内容丰富**：要有具体的逻辑推演。
3. **篇幅适中**：覆盖大纲所有点。
"""

STYLE_PROMPT = """
你是一个擅长“技术哲学”写作的编辑。
请对以下文章进行【完全重写】，使其符合特定的文体风格。

【原文内容】：
{draft}

【重写风格指令】：
"将这部分的内容改成冷静、连续、无情绪赘语，但逻辑收束要紧；每一句都能承载信息与结构，像是一篇技术哲学论文的随笔体。"

【核心执行标准】：
1. **去情绪化**：删除所有软性连接词。
2. **高密度逻辑**：每一句话都必须承载信息量。
3. **连续流**：减少列表，用段落推进观点。
4. **哲学视角**：上升到认知模型或熵增的高度。
5. **词汇降温**：使用冷峻、客观的词汇。

直接输出重写后的正文。
"""

# --- API Endpoints ---

@app.post("/api/outline")
async def generate_outline(request: TopicRequest):
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI client not initialized")
    
    async def generate():
        try:
            stream = client.chat.completions.create(
                model=QWEN_MODEL_NAME,
                messages=[
                    {"role": "system", "content": "你是一个专业的文章架构师。"},
                    {"role": "user", "content": OUTLINE_PROMPT.format(topic=request.topic)}
                ],
                temperature=0.7,
                stream=True
            )
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
        except Exception as e:
            yield f"Error: {str(e)}"

    return StreamingResponse(generate(), media_type="text/plain")

@app.post("/api/draft")
async def generate_draft(request: DraftRequest):
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI client not initialized")
    
    try:
        completion = client.chat.completions.create(
            model=QWEN_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个资深技术观察者。"},
                {"role": "user", "content": DRAFT_PROMPT.format(topic=request.topic, outline=request.outline)}
            ],
            temperature=0.7
        )
        return {"content": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/polish")
async def polish_article(request: PolishRequest):
    if not client:
        raise HTTPException(status_code=500, detail="OpenAI client not initialized")
    
    try:
        completion = client.chat.completions.create(
            model=QWEN_MODEL_NAME,
            messages=[
                {"role": "system", "content": "你是一个技术哲学编辑。"},
                {"role": "user", "content": STYLE_PROMPT.format(draft=request.draft)}
            ],
            temperature=0.7
        )
        return {"content": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Serve Static Files (Frontend)
# We mount this last so API routes take precedence
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Fallback for root to index.html (optional, but good for safety)
@app.get("/")
async def read_root():
    return FileResponse('static/index.html')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)