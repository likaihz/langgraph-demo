# LangGraph Demo

这是一个使用 `uv` 初始化的最小 LangGraph Python 项目。当前只包含一个简单 agent，并绑定了一个 stub 工具，适合作为后续扩展业务工具、模型配置和部署配置的起点。

## 技术栈

- Python 3.12+
- uv
- LangGraph 1.x
- LangChain 1.x
- langchain-openai

## 项目结构

```text
.
├── .env.example
├── langgraph.json
├── pyproject.toml
├── src/
│   └── langgraph_demo/
│       ├── agents/
│       │   └── simple_agent.py
│       ├── middleware/
│       │   └── prompts.py
│       └── tools/
│           └── stub.py
└── uv.lock
```

- `src/langgraph_demo/agents/simple_agent.py`：定义 LangGraph agent、模型节点、工具节点和图编译入口。
- `src/langgraph_demo/tools/stub.py`：定义当前绑定到 agent 的 stub 工具。
- `src/langgraph_demo/middleware/prompts.py`：定义当前 agent 的系统提示词注入逻辑。
- `langgraph.json`：LangGraph CLI / Studio 使用的项目配置，暴露的 graph 名称是 `agent`。
- `.env.example`：环境变量模板，包含 OpenAI 和 LangSmith 相关配置。

## 安装依赖

```bash
uv sync --dev
```

## 配置环境变量

复制 `.env.example` 为 `.env`，然后填写实际密钥：

```bash
cp .env.example .env
```

常用配置项：

```env
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key-here
LANGSMITH_PROJECT=langgraph-demo
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

OPENAI_MODEL=gpt-4.1-mini
OPENAI_API_KEY=your-api-key-here
OPENAI_BASE_URL=
```

如果暂时不需要 LangSmith 追踪，可以把 `LANGSMITH_TRACING` 改为 `false`。
如果使用 OpenAI-compatible 服务，可以把 `OPENAI_BASE_URL` 配置为对应服务地址。

## 启动本地 LangGraph 服务

```bash
uv run langgraph dev
```

启动后可以在命令输出中看到本地 API 地址、Studio 地址和 API Docs 地址。

## 当前 Agent 行为

当前 graph 入口为：

```json
{
  "graphs": {
    "agent": "./src/langgraph_demo/agents/simple_agent.py:graph"
  }
}
```

agent 会调用 OpenAI chat model，并在模型发起工具调用时进入 `ToolNode`。当前工具是 `lookup_stub(query: str)`，只返回占位字符串：

```text
Stub result for '<query>'. Replace lookup_stub with real tool logic.
```

后续可以直接替换 `src/langgraph_demo/tools/stub.py` 中的 stub 实现，或添加更多 `@tool` 函数后放入 `tools` 包导出的 `tools` 列表。

## 快速验证

```bash
uv run python -m compileall src
uv run python -c "from langgraph_demo.agents.simple_agent import graph; print(sorted(graph.nodes.keys()))"
uv run python -c "from langgraph_demo.tools import lookup_stub; print(lookup_stub.invoke({'query': 'demo'}))"
```
