# Backend Scaffold

一个可运行的 FastAPI 后端基础脚手架，内置 PostgreSQL、Redis、LangGraph、LangChain 与 DeepAgents 依赖，并提供健康检查与简易对话接口。

## 快速启动

1. 创建本地环境，并按 `pyproject.toml` 通过阿里云镜像安装依赖：

```powershell
.\scripts\install.ps1
```

2. 启动 PostgreSQL 和 Redis：

```powershell
docker compose up -d
```

3. 复制环境变量：

```powershell
Copy-Item .env.example .env
```

4. 启动服务：

```powershell
.\scripts\run.ps1
```

服务启动后访问：

- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/api/v1/health
- 依赖健康检查：http://localhost:8000/api/v1/health/dependencies

## 对话接口

```powershell
Invoke-RestMethod `
  -Method Post `
  -Uri http://localhost:8000/api/v1/chat `
  -ContentType "application/json" `
  -Body '{"message":"hello","session_id":"demo"}'
```

默认对话模式是 `local`：用 LangGraph 编排流程，用 LangChain `RunnableLambda` 生成本地示例回复，并检测 DeepAgents 依赖是否可用。这样不需要外部 LLM API Key 也能直接运行。

## 依赖版本

项目依赖统一维护在 `pyproject.toml`：

- `[project].dependencies`：运行时依赖
- `[project.optional-dependencies].dev`：测试/开发依赖
- `[tool.pytest.ini_options]`：pytest 配置

运行时依赖固定在阿里云镜像可解析的兼容版本：

- `fastapi==0.136.3`
- `uvicorn[standard]==0.48.0`
- `pydantic-settings==2.14.1`
- `psycopg2-binary==2.9.12`
- `redis==8.0.0`
- `langgraph==1.2.4`
- `langchain==1.3.2`
- `deepagents==0.6.7`

开发依赖：

- `pytest==9.0.3`
- `httpx2==2.3.0`

说明：`langgraph==1.3.0` 当前不在 PyPI/阿里云镜像可用版本中；同时 `deepagents==0.6.x` 需要 `langchain>=1.3.0`，所以这里选择了能成功解析并运行的最新版兼容组合。

## 项目层级

```text
app/
  api/
    deps.py                 # FastAPI 依赖注入入口
    v1/
      router.py             # v1 API 路由聚合
      endpoints/
        health.py           # 健康检查接口
        chat.py             # 对话接口
  ai/
    chat_graph.py           # LangGraph + LangChain 本地对话工作流
    deep_agent.py           # DeepAgents 适配器
  core/
    config.py               # 环境变量与应用配置
  db/
    postgres.py             # psycopg2 PostgreSQL 客户端封装
    redis.py                # Redis 客户端封装
    models/
      chat_turn_record.py   # 数据库表/行记录模型
    migrations/
      001_create_chat_turns.sql
  domain/
    entities/
      chat.py               # 领域实体
  repositories/
    chat_history_repository.py    # 负责业务实体和数据库模型之间的转换与读写
  schemas/
    chat.py                 # 接口请求/响应模型
    health.py
  services/
    chat_service.py         # 应用、业务服务，编排 AI 与持久化
tests/
  test_api.py               # 测试脚本
```

## 分层约定

- `api` 只处理 HTTP 入参、依赖注入和响应模型，不写业务逻辑。
- `schemas` 放 Pydantic 请求/响应模型。
- `services` 放应用业务编排，例如对话流程、仓储调用。
- `domain/entities` 放业务实体，尽量不依赖框架。
- `repositories` 放持久化语义，屏蔽 Redis/PostgreSQL 细节。
- `db` 放具体数据库客户端封装、数据库表模型和迁移 SQL。
- `ai` 放 LangGraph、LangChain、DeepAgents 相关适配代码。
- `core` 放配置与全局基础设施。

## 实体放置规则

项目里有三类“模型/实体”，不要混放：

| 类型 | 放置位置 | 含义 | 示例 |
| --- | --- | --- | --- |
| 接口模型 DTO | `app/schemas/` | HTTP 请求体、响应体、参数校验 | `ChatRequest`、`ChatResponse` |
| 业务实体 | `app/domain/entities/` | 业务概念，不关心数据库怎么存 | `ChatTurn` |
| 数据库表实体/记录模型 | `app/db/models/` | 对应 PostgreSQL 表字段、行记录、SQL 入参 | `ChatTurnRecord` |

所以，如果你问的是“数据库表对应的实体类放哪里”，答案是：

```text
app/db/models/
```

如果你问的是“业务上的实体类放哪里”，答案是：

```text
app/domain/entities/
```

两者关系是：`domain/entities` 代表业务，`db/models` 代表落库结构。仓储层 `repositories` 负责二者转换，例如把 `ChatTurn` 转成 `ChatTurnRecord` 后再用 psycopg2 写入 PostgreSQL。

## 测试

```powershell
.\.venv\Scripts\python.exe -m pytest
```
