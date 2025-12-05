// Global state to store intermediate results
let currentOutline = "";
let currentDraft = "";

async function startGeneration() {
    const topicInput = document.getElementById('topicInput');
    const generateBtn = document.getElementById('generateBtn');
    const statusArea = document.getElementById('statusArea');
    const statusText = document.getElementById('statusText');
    
    const topic = topicInput.value.trim();
    if (!topic) {
        alert("请输入文章主题");
        return;
    }

    // Reset UI
    resetUI();
    
    // Disable input
    topicInput.disabled = true;
    generateBtn.disabled = true;
    statusArea.classList.remove('hidden');

    try {
        // --- Step 1: Generate Outline (Streaming) ---
        statusText.innerText = "正在构建大纲 (1/3)...";
        
        // Show the outline card immediately for streaming
        const step1Card = document.getElementById('step1');
        step1Card.classList.remove('hidden');
        step1Card.classList.add('active');
        const content1 = document.getElementById('content1');
        
        currentOutline = "";
        
        const response = await fetch('/api/outline', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ topic: topic })
        });

        if (!response.ok) throw new Error('Outline generation failed');

        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            const chunk = decoder.decode(value, { stream: true });
            currentOutline += chunk;
            content1.innerHTML = marked.parse(currentOutline);
        }
        
        // --- Step 2: Generate Draft (Hidden) ---
        statusText.innerText = "正在撰写初稿 (2/3)...";
        // We still need the draft for the next step, but we don't show it
        const draftData = await callAPI('/api/draft', { topic: topic, outline: currentOutline });
        currentDraft = draftData.content;
        
        // --- Step 3: Polish Article ---
        statusText.innerText = "正在风格重铸 (3/3)...";
        const polishData = await callAPI('/api/polish', { draft: currentDraft });
        
        showResult('step3', 'content3', polishData.content);
        
        statusText.innerText = "创作完成！";
        document.querySelector('.loader').style.display = 'none';

    } catch (error) {
        console.error(error);
        statusText.innerText = "发生错误: " + error.message;
        statusText.style.color = "red";
        document.querySelector('.loader').style.display = 'none';
    } finally {
        topicInput.disabled = false;
        generateBtn.disabled = false;
    }
}

async function callAPI(endpoint, data) {
    const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || 'API request failed');
    }

    return await response.json();
}

function showResult(cardId, contentId, markdownText) {
    const card = document.getElementById(cardId);
    const contentDiv = document.getElementById(contentId);
    
    // Render Markdown
    contentDiv.innerHTML = marked.parse(markdownText);
    
    // Show card
    card.classList.remove('hidden');
    
    // Auto-expand the card (add 'active' class)
    card.classList.add('active');
}

function toggleCard(contentId) {
    const contentDiv = document.getElementById(contentId);
    const card = contentDiv.parentElement;
    card.classList.toggle('active');
}

function resetUI() {
    document.getElementById('step1').classList.add('hidden');
    // Step 2 is removed from UI
    document.getElementById('step3').classList.add('hidden');
    
    document.getElementById('content1').innerHTML = '';
    document.getElementById('content3').innerHTML = '';
    
    document.querySelector('.loader').style.display = 'block';
    document.getElementById('statusText').style.color = '#666';
}

function copyToClipboard() {
    const content = document.getElementById('content3').innerText;
    navigator.clipboard.writeText(content).then(() => {
        const btn = document.querySelector('.copy-btn');
        const originalText = btn.innerText;
        btn.innerText = "已复制！";
        setTimeout(() => {
            btn.innerText = originalText;
        }, 2000);
    });
}