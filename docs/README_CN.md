# MCP 服务器模板

> 一个用于构建 MCP（模型上下文协议）服务器的 Python 模板。此模板提供了构建 AI 助手的坚实基础，可连接到您的后端系统。

## 特性

- 🔌 **MCP 协议支持** - 基于 MCP Python SDK 2.0 构建
- 🔐 **ApiKey 认证** - 通过 HTTP 请求头进行安全的 API 密钥认证
- 🛠️ **模块化工具** - 易于扩展的工具系统
- 📝 **完整日志** - 内置日志记录和轮转功能
- 🚀 **生产就绪** - 包含中间件、错误处理和配置管理

## 快速开始

### 环境要求

- Python 3.10+
- MCP Python SDK >= 2.0.0

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/mcp-server-template.git
cd mcp-server-template

# 安装依赖
pip install -r requirements.txt

# 复制环境变量模板
cp .env.example .env
```

### 配置

编辑 `.env` 文件，填入您的配置：

```env
# 后端 API 配置
API_BASE_URL=http://your-api-server:port

# 服务器配置
PORT=8001

# 日志配置
LOG_LEVEL=INFO
```

### 启动服务器

```bash
python server.py
```

服务器默认运行在 `http://localhost:8001`，MCP 端点为 `http://localhost:8001/mcp`。

## 项目结构

```
mcp-server-template/
├── server.py          # MCP 服务器入口
├── config.py          # 配置和日志
├── middleware.py       # 认证中间件
├── constants.py       # 常量定义
├── utils.py           # 工具函数
├── tools/             # 工具模块目录
│   ├── __init__.py    # 工具模块初始化
│   ├── example.py     # 示例工具
│   └── ...            # 在此添加您的工具
├── docs/              # 文档
│   ├── README.md      # 英文文档
│   ├── README_CN.md   # 中文文档
│   ├── API.md         # API 文档
│   └── CONTRIBUTING.md # 贡献指南
├── .env.example       # 环境变量模板
├── .gitignore         # Git 忽略文件
├── requirements.txt   # Python 依赖
└── LICENSE            # MIT 许可证
```

## 使用方法

### 配置 MCP 客户端

在您的 AI 客户端中添加 MCP 配置：

```json
{
  "mcpServers": {
    "your-server-name": {
      "url": "http://localhost:8001/mcp",
      "headers": {
        "X-Api-Key": "YOUR_API_KEY"
      }
    }
  }
}
```

### 创建工具

在 `tools/` 目录中创建新工具：

```python
# tools/your_tool.py

from utils import call_api, check_response

def register_your_tools(mcp):
    """注册您的工具到 MCP 服务器"""

    @mcp.tool()
    async def your_tool_name(param1: str = "", param2: int = 0) -> str:
        """工具描述，帮助 AI 理解何时使用此工具。

        Args:
            param1: 参数1的描述
            param2: 参数2的描述

        Returns:
            返回值的描述
        """
        # 调用您的后端 API
        res = await call_api("/api/your-endpoint", body={
            "param1": param1,
            "param2": param2
        })

        # 检查响应
        ok, result = check_response(res, "your action")
        if not ok:
            return f"❌ {result}"

        # 处理并返回结果
        return f"✅ 成功: {result}"
```

在 `tools/__init__.py` 中注册您的工具：

```python
from tools.your_tool import register_your_tools

def register_all_tools(mcp):
    """注册所有工具到 MCP 服务器"""
    register_your_tools(mcp)
```

### 创建资源

资源为 AI 提供只读数据：

```python
@mcp.resource("your-server://resource-name")
async def get_resource():
    """资源描述"""
    return {"key": "value"}
```

## 环境变量

| 变量 | 描述 | 默认值 |
|------|------|--------|
| `API_BASE_URL` | 后端 API 基础 URL | `http://localhost:8000` |
| `PORT` | 服务器端口 | `8001` |
| `LOG_LEVEL` | 日志级别 | `INFO` |

## 技术栈

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - 官方 MCP Python SDK (>= 2.0.0)
- [httpx](https://www.python-httpx.org/) - 异步 HTTP 客户端
- [uvicorn](https://www.uvicorn.org/) - ASGI 服务器

## 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细信息。

1. Fork 仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

本项目基于 MIT 许可证 - 查看 [LICENSE](../LICENSE) 文件了解详情。

## 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - 协议规范
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) - Python 实现