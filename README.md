# cs2-slim-features

CS2 Slim 服务端的**功能组件仓库**（选配组件）。
配合主仓库 [cs2-slim-replica](https://github.com/cyqmq/cs2-slim-replica) 使用，按需为精简服务端添加功能。

## 功能列表

| 功能 | 目录 | 说明 |
|------|------|------|
| 人机 (bots) | `bots/` | 服务端 `bot_add` 人机玩法 + 客户端离线练习配置 |
| 插件框架 (metamod) | `metamod/` | Metamod:Source 基础插件框架（CS2 Linux），自动补 `gameinfo.gi` |
| 插件框架 Windows (metamod-win) | `metamod-win/` | Metamod:Source 基础插件框架（CS2 Windows/win64），自动补 `gameinfo.gi` |
| CSS Linux (css) | `css/` | CounterStrikeSharp C# 插件框架（CS2 Linux/linuxsteamrt64，带 .NET 运行时），依赖 `metamod` |
| CSS Windows (css-win) | `css-win/` | CounterStrikeSharp C# 插件框架（CS2 Windows/win64，带 .NET 运行时），依赖 `metamod-win` |

## 使用方法

### 配置驱动

在 `slim.yaml` 添加：

```yaml
features:
  - bots
```

```bash
python cs2slim.py download --config slim.yaml
python cs2slim.py extract  --config slim.yaml
python cs2slim.py build    --config slim.yaml
```

### 命令行参数

```bash
python cs2slim.py download --platform linux --maps de_dust2 --features bots
```

### 部署配置（source 模式）

构建完成后，把 `bots/config/` 下的 cfg 文件复制到服务端：

```bash
cp bots/config/server_bot.cfg        <精简树>/game/csgo/cfg/server_bot.cfg
cp bots/config/offline_practice.cfg  <精简树>/game/csgo/cfg/offline_practice.cfg
```

然后在 `server.cfg` 末尾加 `exec server_bot`，重启服务端即可。

## 预构建包（prebuilt 模式）

功能已发布为预构建包，可直接拉取并**自动拼装**进精简树：

```bash
# 在精简服务端工作目录执行（slim / slim-win 树根目录）
curl -fsSL -o bots-pack.zip https://github.com/cyqmq/cs2-slim-features/releases/latest/download/bots-pack.zip
# Linux / Windows 通用: 包内为 game/csgo/cfg/ 结构，直接解压到树根
unzip -o bots-pack.zip -d <精简树>
```

包内结构（与 CS2 目录一致，解压即完成拼装）：

```text
game/csgo/cfg/server_bot.cfg
game/csgo/cfg/offline_practice.cfg
README.md
```

也可以使用主仓库一键脚本的 prebuilt 模式，自动完成拼装：

```bash
# 一键脚本（Linux，先 export 再 curl|bash）
export CS2_MODE=prebuilt CS2_FEATURES=bots
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

## Metamod:Source 插件框架（metamod / metamod-win）

CS2 基础插件加载框架。安装后控制台可用 `meta version` / `meta list`，并可在 `game/csgo/addons/metamod/metaplugins.ini` 里加载其他插件（如 CounterStrikeSharp）。

- **Linux**：使用 `metamod`（linuxsteamrt64）
- **Windows**：使用 `metamod-win`（win64）

prebuilt 模式自动完成（以 Linux 为例，Windows 用 `get-cs2slim.ps1` + `CS2_FEATURES=metamod-win`）：

```bash
export CS2_MODE=prebuilt CS2_FEATURES=metamod
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

拼装时自动在 `game/csgo/gameinfo.gi` 的 SearchPaths 中加入 `Game csgo/addons/metamod`。详见 [`metamod/README.md`](metamod/README.md) 和 [`metamod-win/README.md`](metamod-win/README.md)。

## CounterStrikeSharp 插件框架（css / css-win）

CSS 是 CS2 服务端最常用的 C# 插件框架，运行在 Metamod 之上（Linux 版依赖 `metamod`，Windows 版依赖 `metamod-win`）。一键安装会自动带上依赖：

```bash
# Linux
export CS2_MODE=prebuilt CS2_FEATURES=metamod,css
curl -fsSL https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.sh | bash
```

```powershell
# Windows
$env:CS2_MODE = "prebuilt"; $env:CS2_FEATURES = "metamod-win,css-win"
irm https://raw.githubusercontent.com/cyqmq/cs2-slim-replica/main/scripts/get-cs2slim.ps1 | iex
```

安装后把插件 dll 放入 `game/csgo/addons/counterstrikesharp/plugins/`，重启服务端即可。详见 [`css/README.md`](css/README.md) 和 [`css-win/README.md`](css-win/README.md)。

## Release

- **v1.4.0**：`css-pack.zip`（CounterStrikeSharp 1.0.376，linuxsteamrt64，带 .NET 运行时）
- **v1.3.0**：`css-pack-win.zip`（CounterStrikeSharp 1.0.376，win64，带 .NET 运行时）
- **v1.2.0**：`metamod-pack-win.zip`（Metamod:Source 2.0.0-git1473，win64，Windows 版插件框架）
- **v1.1.0**：`metamod-pack.zip`（Metamod:Source 2.0.0-git1473，linuxsteamrt64，Linux 版插件框架）
- **v1.0.0**：`bots-pack.zip`（含 `game/csgo/cfg/` 结构，自动拼装）

## 组件格式

每个功能组件包含：

- `filelist.txt` — 追加到核心下载清单的片段（纯配置类功能通常为空）
- `metadata.json` — 元数据（说明、配置路径、更新时间）
- `config/` — 配置文件模板

```json
{
  "name": "bots",
  "description": "人机功能包",
  "filelist": [],
  "config": {
    "server_bot": "config/server_bot.cfg",
    "offline_practice": "config/offline_practice.cfg"
  },
  "updated": "2026-10-06"
}
```

## 更新流程

CS2 更新后，检查配置是否仍适用，更新 `metadata.json` 的 `updated` 字段即可。