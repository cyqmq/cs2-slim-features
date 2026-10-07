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