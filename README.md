# Basic Framework

前后端基础框架。前端基于 Vite + React + TypeScript，后端基于 FastAPI，目录按 `src/backend`、`src/frontend/client`、`src/frontend/platform` 拆分。

## 技术栈

- React 19
- TypeScript
- Vite
- React Router
- Zustand
- Axios
- Ant Design
- Tailwind CSS
- ECharts
- ESLint
- code-inspector-plugin
- FastAPI
- PostgreSQL
- Redis
- LangGraph / LangChain / DeepAgents

## 启动命令

### 前端

前端工程位于 `src/frontend`，现有 C 端应用位于 `src/frontend/client`：

```bash
cd src/frontend
npm install
npm run dev
npm run build
npm run lint
npx tsc --noEmit
```

开发服务默认地址：

```text
http://127.0.0.1:5173/
```

### 后端

后端工程位于 `src/backend`，详细说明见 `src/backend/README.md`：

```bash
cd src/backend
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m pytest
```

本地启动服务：

```bash
cd src/backend
docker compose up -d
cp .env.example .env
.venv/bin/python -m uvicorn app.main:app --reload
```

## 环境变量

前端工程目录按环境拆分：

```text
.env.development
.env.production
.env.test
```

当前约定：

```text
VITE_APP_ENV=development
VITE_API_BASE_URL=/api
```

新增前端环境变量必须以 `VITE_` 开头，并在 `src/frontend/client/src/env.d.ts` 中补充类型声明。

## 目录结构

```text
.
├── .github/                 # GitHub Actions 等配置
├── docker/                  # 工程级 Docker 编排或部署配置
├── docs/                    # 项目文档
├── src/
│   ├── backend/             # 后端服务目录
│   └── frontend/            # 前端工程目录
│       ├── client/          # C 端前端应用
│       │   └── src/
│       │       ├── api/     # 后端接口定义，按业务模块拆分
│       │       ├── assets/  # 需要参与构建的资源
│       │       ├── components/
│       │       ├── hooks/
│       │       ├── layout/
│       │       ├── pages/
│       │       ├── request/
│       │       ├── routes/
│       │       ├── store/
│       │       ├── types/
│       │       ├── utils/
│       │       ├── App.tsx
│       │       ├── main.tsx
│       │       └── env.d.ts
│       ├── platform/        # 管理端 / 平台端前端应用占位
│       ├── public/          # 原样输出的静态资源
│       ├── Dockerfile
│       ├── nginx.conf
│       ├── package-lock.json
│       ├── package.json
│       ├── tailwind.config.js
│       ├── tsconfig.json
│       └── vite.config.ts
└── README.md
```

## 模块职责

### `src/frontend/client/src/api`

只放接口函数，不写页面逻辑。

推荐写法：

```ts
import { request } from '@/request'

export function getExampleList() {
  return request('/example/list')
}
```

### `src/frontend/client/src/request`

统一维护 Axios 实例、baseURL、timeout、请求拦截器和响应拦截器。业务代码不要直接 `axios.create`，统一从这里导出的 `request` 调用。

### `src/frontend/client/src/routes`

集中维护路由表。新增页面后，需要在 `src/frontend/client/src/routes/index.tsx` 注册路由。

### `src/frontend/client/src/pages`

页面按业务模块建目录：

```text
src/frontend/client/src/pages/Example/
├── index.tsx
└── style.scss
```

页面组件只负责页面编排。可复用逻辑下沉到 `hooks`、`components`、`store` 或 `utils`。

### `src/frontend/client/src/components`

只放业务无关的公共组件，例如 Button、Modal、Table 二次封装。业务强相关组件应放在对应页面目录内部。

### `src/frontend/client/src/store`

使用 Zustand 管理全局状态。每个业务状态建议单独文件维护，并从 `src/frontend/client/src/store/index.ts` 统一导出。

### `src/frontend/client/src/layout`

放通用页面布局，例如 `MainLayout`、`AuthLayout`、Header、Sidebar、Footer。

### `src/frontend/client/src/assets`

- `images/`：图片
- `icons/`：图标
- `fonts/`：字体
- `styles/`：全局样式和样式变量

无业务资源时保留 `.gitkeep` 作为目录占位。

## 开发规范

1. 优先使用 TypeScript，新增组件使用 `.tsx`，普通工具文件使用 `.ts`。
2. 统一使用 `@/` 路径别名引用 `src/frontend/client/src` 下文件。
3. 页面放在 `src/frontend/client/src/pages`，公共组件放在 `src/frontend/client/src/components`，不要混放。
4. API 请求必须通过 `src/frontend/client/src/request` 封装，不在页面里直接调用 `fetch` 或 `axios`。
5. 全局状态使用 Zustand，不再引入其他状态机或状态库，除非有明确架构评审。
6. UI 优先使用 Ant Design 组件，局部布局和间距可用 Tailwind。
7. 图表统一使用 ECharts，图表初始化要在组件卸载时 `dispose`。
8. 工具函数必须是纯函数优先，放在 `src/frontend/client/src/utils`。
9. hooks 文件以 `use` 开头，例如 `useAuth.ts`、`useFetch.ts`。
10. 提交前至少运行 `npm run lint`、`npx tsc --noEmit`、`npm run build`。

## 新增页面流程

1. 在 `src/frontend/client/src/pages` 下创建页面目录。
2. 编写 `index.tsx`。
3. 如有页面私有样式，新增 `style.scss`。
4. 在 `src/frontend/client/src/routes/index.tsx` 注册路由。
5. 如需要侧边栏入口，在 `src/frontend/client/src/layout/components/Sidebar.tsx` 添加导航项。

## 新增接口流程

1. 在 `src/frontend/client/src/api` 下按业务模块新增或补充接口文件。
2. 在 `src/frontend/client/src/types` 中声明请求和响应类型。
3. 使用 `request` 调用接口。
4. 从 `src/frontend/client/src/api/index.ts` 统一导出。

## 当前保留 Demo

- 首页 Ant Design demo
- 首页 ECharts demo
- 首页 Zustand demo
- MainLayout / AuthLayout / React Router demo

这些 demo 用于验证框架基础能力，正式业务开发时可以删除或替换。
