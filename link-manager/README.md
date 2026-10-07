# cs2-link-manager 插件管理工具（link-manager）

为 CS2 精简服务端附带 **cs2-link-manager**（`cs2lm`）插件管理 CLI。它不安装 CSS/Metamod 核心框架，而是用**符号链接**从中央仓库把插件映射进服务器：支持插件启用/停用、profile 一键切换、反向导入（adopt）、`.cs2pkg` 打包、Web UI 等。

## 依赖

- **Python 3.11+**（仅标准库，宿主机需预装）。
- 建议同时安装 `metamod`（+ `css`）功能，否则没有可管理的插件框架。Windows 建议以管理员/开发者模式运行以创建真实符号链接，否则自动回退 junction/复制。

## 安装

```bash
# Linux: 和 CSS 一起装
export CS2_MODE=prebuilt CS2_FEATURES=metamod,css,link-manager
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

```powershell
# Windows
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "metamod-win,css-win,link-manager"
irm https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.ps1 | iex
```

拼装后服务器根目录出现：

- `cs2lm`（Linux/bash 启动器）
- `cs2lm.bat`（Windows 启动器）
- `tools/cs2lm/`（cs2lm 源码 + README + pyproject.toml）

## 快速开始

```bash
cd <服务器根目录>   # 含 game/ 的目录
./cs2lm init --server . --repo plugins-repo
./cs2lm add MyPlugin ./path/to/MyPlugin/
./cs2lm install MyPlugin
./cs2lm list
./cs2lm doctor
```

Windows 用 `cs2lm.bat` 代替 `./cs2lm`。更多命令见 `tools/cs2lm/README.md`。

## 简幻欢等面板：单端口双服务（UDP CS2 + TCP 管理 Web）

简幻欢只分配一个随机端口（`SERVER_PORT`）。CS2 走 **UDP**，cs2lm 的 Web 管理走 **TCP**——两个协议在同一端口号上互不冲突，已实测可行。

`start_panel.sh` / `start_server.sh` / Windows `start_server.bat` 已内置该逻辑（需已安装本功能；**可选配置，默认不启动 Web**）：

- **面板（简幻欢等）**：设置环境变量 `CS2LM_WEB=1` 才会启动 Web，端口 = `SERVER_PORT`（CS2 同端口）。
- **本地 Linux**：`CS2LM_WEB=1 bash start_server.sh`。
- **本地 Windows**：在环境变量中配置 `CS2LM_WEB=1`，`start_server.bat` 自动启用（需 `cs2lm.bat` 位于服务器根目录）。
- **端口**：优先级 `SERVER_PORT`（面板注入）> `CS2_PORT`（用户变量）> 默认 `27015`。CS2 UDP 与管理 Web TCP 共用该端口。
- **Token**：
  - 设置 `CS2LM_WEB_TOKEN` 环境变量则使用它；
  - **无论是否设置，token 都会写入服务器根目录 `web_token.txt`**（未设置时随机生成 16 位十六进制，权限 600）。
- **访问**：`http://<服务器IP>:<端口>/?token=<TOKEN>`
- **运行中查看 token**：CS2 控制台手动执行 `exec cs2slim_token.cfg`（启动时已生成在 `game/csgo/cfg/cs2slim_token.cfg`，不自动加入启动参数）。
- **进程管理**：PID 写入 `web.pid`；重启时自动清理旧进程；日志在 `web.log`（Windows 另存 `web.err.log`）；启动失败会在控制台打印警告。

**一次性启动菜单**：三个启动脚本均内置一次性交互菜单（首次交互启动显示；选项：`1` 完整启动 / `2` 只启动 Web / `3` 只启动 CS2 / `4` 查看 token / `5` 停止 Web / `6` 退出；15 秒无输入默认选 `1`）。选择后 CS2 前台运行、日志正常显示，菜单不会反复出现。想再次打开菜单：`bash start_server.sh menu`（Windows `start_server.bat menu`）；面板场景可在 `start.sh` 顶部加 `export CS2LM_MENU=1` 或在面板环境变量设 `CS2LM_MENU=1`。面板自动重启建议设 `CS2LM_AUTO=1`（或启动命令加 `auto`）跳过菜单。

```bash
# 面板/本地：设置 CS2LM_WEB=1 才启用单端口 Web（面板在环境变量里配置，默认关闭）
export CS2_MODE=prebuilt CS2_FEATURES=metamod,css,link-manager
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash

# 本地 Linux：想开 Web 时加 CS2LM_WEB=1（token 仍会写入 web_token.txt）
CS2LM_WEB=1 CS2LM_WEB_TOKEN=my-secret bash start_server.sh

# 本地 Windows：设置环境变量后运行 start_server.bat
set CS2LM_WEB=1
set CS2LM_WEB_TOKEN=my-secret
start_server.bat
```

## 包内结构

```text
cs2lm               # bash 启动器
cs2lm.bat           # Windows 启动器
tools/cs2lm/        # cs2lm Python 源码（src/cs2lm）+ README + pyproject.toml
README.md
```

## 注意

- 本功能**不安装** Metamod/CSS 核心框架，请搭配 `metamod`/`css`（或 `metamod-win`/`css-win`）使用。
- 需要宿主机有 Python 3.11+。
- 源码来自 https://github.com/cyqmq/cs2-link-manager （MIT）。打包版本以构建时 main 分支为准，重新构建可更新。